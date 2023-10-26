import argparse
import dateutil.parser
import json
from pathlib import Path
import re
import requests

from stix2 import Filter, MemoryStore
from tqdm import tqdm

from stix_schemas import data_component_schema, data_source_schema, sensor_mapping_schema


TYPES = {
    "x-mitre-data-component": data_component_schema, 
    "x-mitre-data-source": data_source_schema, 
    "x-mitre-sensor-mapping": sensor_mapping_schema
} # Global to map schemas to STIX object type


def load_attack_data(version, attack_domain, groups):
    """Load pre-existing ATT&CK STIX data as references for validation."""
    def merge_lists(l1, l2):
        for item in l2:
            if item not in l1:
                l1.append(item)
        return l1


    if groups:
        enterprise_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/enterprise-attack/enterprise-attack.json"
        ics_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/ics-attack/ics-attack.json"
        mobile_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/mobile-attack/mobile-attack.json"
        attack_data = requests.get(enterprise_url, verify=True).json()["objects"]
        attack_data = merge_lists(attack_data, requests.get(ics_url, verify=True).json()["objects"])
        attack_data = merge_lists(attack_data, requests.get(mobile_url, verify=True).json()["objects"])
    else:
        attack_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/{attack_domain}/{attack_domain}.json"
        attack_data = requests.get(attack_url, verify=True).json()["objects"]

    # Now filter attack_data to only have the information we require
    attack_objects = []

    # Find the already-existing SDO's to avoid duplication
    for attack_object in attack_data:
        types = ["x-mitre-data-source", "x-mitre-data-component"]

        if attack_object["type"] in types:
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects
            attack_objects.append(attack_object)
    return attack_objects


def validate_timestamp(instance):
    """
    Ensure timestamps contain sane months, days, hours, minutes, seconds. Sourced from the oasis stix2validator library.
    """
    ts_re = re.compile(r"^[0-9]{4}-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])T([01][0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9]|60)(\.[0-9]+)?Z$")
    timestamp_props = ['created', 'modified']
    for tprop in timestamp_props:
        if tprop in instance and ts_re.match(instance[tprop]):
            # Don't raise an error if schemas will catch it
            try:
                dateutil.parser.parse(instance[tprop])
            except ValueError as e:
                raise SyntaxError("'%s': '%s' is not a valid timestamp: %s"
                                % (tprop, instance[tprop], str(e)), instance['id'])
            

def validate_bundle_completeness(bundle, attack_objects):
    # Load STIX data into MemoryStore for faster searching
    bundle_objects = MemoryStore(stix_data=bundle["objects"])
    
    # Start by validating the SensorMapping items, and the corresponding relationship
    for sro in bundle_objects.query([Filter("type", "=", "x-mitre-sensor-mapping")]):
        data_source_name = sro.get("data_source")

        # Verify that the associated relationship is in the bundle with this mapping

        # Find the STIX ID associated with the data source
        filters = [Filter("type", "=", "x-mitre-data-source"), Filter("name", "=", data_source_name)]

        local_query_results = bundle_objects.query(filters)
        if not local_query_results:
            # Check if the data source is newly created
            if sro.get("x_mitre_data_source_id") == -1:
                raise LookupError(f"Bundle is missing an entry for {data_source_name}, which should be present for validation of object {sro['id']}")
            else:
                # Check in ATT&CK MemoryStore
                query_results = attack_objects.query(filters)
                if not query_results:
                    raise LookupError(f"Bundle is missing an entry for {data_source_name}, which should be bundled with object {sro['id']}")
                else:
                    ds_id = query_results[0]["id"]
        else:
            ds_id = local_query_results[0]["id"]
        
        # Find the STIX ID associated with the data component
        data_component_name = sro.get("data_component")

        filters = [Filter("type", "=", "x-mitre-data-component"), Filter("name", "=", data_component_name)]

        local_query_results = bundle_objects.query(filters)
        if not local_query_results:
            # Check if it is present in ATT&CK data
            query_results = attack_objects.query(filters)
            if query_results:
                dc_id = query_results[0]["id"]
            else:
                raise LookupError(f"Bundle is missing an entry for {data_component_name}, which should be bundled with object {sro['id']}")
        else:
            dc_id = local_query_results[0]["id"]

        # Look for the relationship in the bundle
        relationship_type = sro.get("relationship")

        filters = [Filter("type", "=", "relationship"), Filter("source_ref", "=", ds_id), Filter("target_ref", "=", dc_id), Filter("relationship_type", "=", relationship_type)]

        local_query_results = bundle_objects.query(filters)
        if not local_query_results:
            # Check if it is present in ATT&CK data
            query_results = attack_objects.query(filters)
            if not query_results:
                print(data_source_name, ds_id, data_component_name, dc_id, relationship_type)
                raise LookupError(f"Bundle is missing relationship entry for object {sro['id']}")
        # Else - valid bundle


def validate_schemas(bundle, bundle_name):
    for stix_obj in tqdm(bundle["objects"], desc=f"validating {bundle_name} schemas..."):
        stix_type = stix_obj.get("type")
        if stix_type == 'relationship':
            continue
        schema_ = TYPES.get(stix_type)
        if not schema_:
            raise ValueError(f"This type is not supported for object {stix_type}")
        
        # Verify that it contains necessary properties
        schema_.validate(stix_obj)
        
        # Verify dates
        validate_timestamp(stix_obj)


def validate(bundle, bundle_name, attack_objects):
    """Validates a bundle by testing schema correctness and 'completeness' of the bundle, which tests that every Sensor Mapping has its mapping (SRO) and newly created objects."""
    print(f"validating {bundle_name}... ", end="")
    
    validate_schemas(bundle, bundle_name)
    validate_bundle_completeness(bundle, attack_objects)

    print("done!")


def _parse_args():
    # Reuses a lot of parameters used for creating mappings (for obvious reasons)
    ROOT_DIR = Path(__file__).parent.parent.parent
    parser = argparse.ArgumentParser(description="validate STIX bundles")
    parser.add_argument("-mappings_location",
                        dest="mappings_location",
                        type=Path,
                        help="filepath to folder of STIX bundle mappings",
                        default=Path(ROOT_DIR, "mappings", "stix", "enterprise"))
    parser.add_argument("-config_location",
                        dest="config_location",
                        help="filepath to the configuration for the framework. If none is provided, module assumes the bundle was made from the config file in the mappings input folder.",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input", "config.json"))
    parser.add_argument("-attack_domain",
                        dest="attack_domain",
                        help="Attack domain of mapping files",
                        type=str,
                        choices=["enterprise-attack", "ics-attack", "mobile-attack"],
                        default="enterprise-attack")
    parser.add_argument("-groups",
                        action="store_true",
                        help="If specified, mappings contain group objects")
    
    return parser.parse_args()


def main():
    args = _parse_args()

    # Process the config file
    with args.config_location.open("r", encoding="utf-8") as f:
        config = json.load(f)
        version = config["attack_version"]

    mapping_data = [file for file in args.mappings_location.glob('*mappings*.json') if file.is_file()]

    json_to_validate = []
    for file in mapping_data:
        with file.open("r", encoding="utf-8") as f:
            json_to_validate.append((json.load(f), file.name))
    
    # Store the ATT&CK data for reference
    attack_objects = MemoryStore(stix_data=load_attack_data(version, args.attack_domain, args.groups))

    for bundle in json_to_validate:
        validate(*bundle, attack_objects)


if __name__ == '__main__':
    main()