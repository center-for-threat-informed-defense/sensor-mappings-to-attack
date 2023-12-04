import uuid
import json
from pathlib import Path
import argparse

import requests
from tqdm import tqdm
import pandas as pd
from stix2.properties import StringProperty, ReferenceProperty, EnumProperty, ListProperty, BooleanProperty
from stix2.v21 import Bundle, CustomObject, ExternalReference, Relationship


@CustomObject(
    'x-mitre-data-source', [
        ("name", StringProperty()),
        ("description", StringProperty()),
        ("x_mitre_platforms", ListProperty(StringProperty())),
        ("x_mitre_domains", ListProperty(EnumProperty(allowed=['enterprise-attack', 'mobile-attack', 'ics-attack']))),
        ("x_mitre_contributors", ListProperty(StringProperty())),
        ("x_mitre_collection_layers", ListProperty(StringProperty())),
        ("object_marking_refs", ListProperty(ReferenceProperty(valid_types=['marking-definition']))),
        ("created_by_ref", ReferenceProperty(valid_types=['identity'])),
        ("external_references", ListProperty(ExternalReference)),
        ("x_mitre_version", StringProperty()),
        ("x_mitre_attack_spec_version", StringProperty()),
        ("x_mitre_modified_by_ref", ReferenceProperty(valid_types=['identity'])),
        ("x_mitre_deprecated", BooleanProperty())
    ]
)


class DataSource():
    """Custom MITRE Data Source STIX object."""
    def __init__(self, **kwargs):
        # Intentionally left blank.
        pass


@CustomObject(
    'x-mitre-data-component', [
        ('name', StringProperty()),
        ('description', StringProperty()),
        ('x_mitre_data_source_ref', ReferenceProperty(valid_types=['x-mitre-data-source'])),
        ("x_mitre_version", StringProperty()),
        ("x_mitre_attack_spec_version", StringProperty()),
        ("x_mitre_domains", ListProperty(EnumProperty(allowed=['enterprise-attack', 'mobile-attack', 'ics-attack']))),
        ("x_mitre_modified_by_ref", ReferenceProperty(valid_types=['identity'])),
        ("created_by_ref", ReferenceProperty(valid_types=['identity'])),
        ("object_marking_refs", ListProperty(ReferenceProperty(valid_types=['marking-definition']))),
        ("x_mitre_deprecated", BooleanProperty())
    ]
)


class DataComponent():
    """Custom MITRE Data Component STIX object."""
    def __init__(self, **kwargs):
        # Intentionally left blank.
        pass


@CustomObject(
    'x-mitre-sensor-mapping', [
        ("event_id", StringProperty()),
        ("description", StringProperty()),
        ("data_source", StringProperty()),
        ("data_component", StringProperty()),
        ("source", StringProperty()),
        ("relationship", StringProperty()),
        ("target", StringProperty()),
        ("x_mitre_data_source_id", StringProperty())
    ]
)


class SensorMapping():
    """Custom MITRE sensor data mapping STIX object."""
    def __init__(self, **kwargs):
        # Intentionally left blank.
        pass


    def equals(self, properties):
        """Returns if a SensorMapping is equivalent to the given `properties` dictionary or SensorMapping."""
        prop_map = {
            "EVENT ID": "event_id", 
            "EVENT DESCRIPTION": "description", 
            "ATT&CK DATA SOURCE ID": "x_mitre_data_source_id", 
            "ATT&CK DATA SOURCE": "data_source", 
            "ATT&CK DATA COMPONENT": "data_component", 
            "SOURCE": "source", 
            "RELATIONSHIP": "relationship",
            "TARGET": "target"
        }  # Keys are for DataFrame keys. Values are for the corresponding STIX keys.
        for key in properties:
            if self[prop_map[key]] != properties[key]:
                return False
            
        return True


def load_attack_data(version, attack_domain, groups):
    """Load ATT&CK STIX data to create reference dictionaries to use when building STIX Bundles."""
    def merge_lists(l1, l2):
        for item in l2:
            if item not in l1:
                l1.append(item)
        return l1

    # load ATT&CK STIX data
    print("downloading ATT&CK data... ", end="", flush=True)
    if groups:
        enterprise_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/enterprise-attack/enterprise-attack.json"
        ics_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/ics-attack/ics-attack.json"
        mobile_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/mobile-attack/mobile-attack.json"
        attack_data = requests.get(enterprise_url, verify=True).json()["objects"]
        attack_data = merge_lists(attack_data, requests.get(ics_url, verify=True).json()["objects"])
        attack_data = merge_lists(attack_data, requests.get(mobile_url, verify=True).json()["objects"])
    else:
        attack_url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{version}/{attack_domain}/{attack_domain}.json"
        print(attack_url)
        attack_data = requests.get(attack_url, verify=True).json()["objects"]
    print("done")

    # Now filter attack_data to only have the information we require
    source_ids_references = {}
    component_ids = {}
    tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    # Find the already-existing SDO's to avoid duplication
    for attack_object in tqdm(attack_data, desc=f"parsing v{version} {attack_domain} data", bar_format=tqdm_format):
        type_data_source = "x-mitre-data-source"
        type_data_component = "x-mitre-data-component"

        if attack_object["type"] == type_data_source:
            if "external_references" not in attack_object:
                continue  # skip objects without sources_reference
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            for reference in attack_object["external_references"]:
                if reference["source_name"] == "mitre-attack":
                    # Map the ATT&CK Data Source ID to its STIX ID
                    source_ids_references[reference["external_id"]] = attack_object["id"]

        elif attack_object["type"] == type_data_component:
            component_ids[attack_object["name"]] = attack_object["id"]
    return (source_ids_references, component_ids)


def bundle_append(bundle, object_to_add):
    """Checks to see if `object_to_add` has already been added to `bundle`. If it has not,
    it is added."""
    simple_bundle = [item["id"] for item in bundle]
    
    if object_to_add["id"] not in simple_bundle:
        bundle.append(object_to_add)


def check_mapping_sdo(search_target, obj_list):
    """
    Check if `search_target` is in `obj_list`. Return a SensorMapping STIX ID iff all properties of `search_target` are identical to the SensorMapping object's properties from `obj_list.
    
    Parameters:
    `search_target` (Dict): Mapping data for a Sensor Mapping SDO.
    `obj_list` (List): List of created SDOs.
    """

    for sdo in obj_list:
        if sdo.equals(search_target):
            return sdo
        
    return None


def create_stix_object(reference_dict, created_objects, object_type, object_details):
    """
    Creates an SDO according to the logic:
    - Is it already created within the reference dictionary?
    - If not, has it already been created and stored?
    - If neither, create an entirely new SDO

    Parameters:
    reference_dict (dict): Dictionary of STIX objects details created from an already existing JSON.
    created_objects (dict): Dictionary of STIX objects that have already been created thus far. Key <object name>: Value <STIX objects>
    object_type (str): Type of SDO object being created
    object_details (dict): Attributes for the object. Varies on `object_type`

    Returns:
    Custom STIX Object
    """
    id_to_reuse = None

    if object_type == "Sensor Mapping":  # It's more complicated since these custom objects are stored as lists
        # Check reference_dict first
        if object_details["EVENT ID"] in reference_dict:
            potential_matches = reference_dict[object_details["EVENT ID"]]
            id_to_reuse =  check_mapping_sdo(object_details, potential_matches)
            if id_to_reuse:
                # There is no need to continue, the object has already been created.
                return id_to_reuse
        # Check created_objects next
        elif object_details["EVENT ID"] in created_objects:
            potential_matches = created_objects[object_details["EVENT ID"]]
            id_to_reuse = check_mapping_sdo(object_details, potential_matches)
            if id_to_reuse:
                # There is no need to continue, the object has already been created.
                return id_to_reuse

        if not id_to_reuse:  # If there are no matches, create a new ID for the custom object.
            id_to_reuse = f"x-mitre-sensor-mapping--{uuid.uuid4()}"

        new_sdo = SensorMapping(
            id=id_to_reuse,
            event_id=object_details["EVENT ID"],
            description=object_details["EVENT DESCRIPTION"],
            data_source=object_details["ATT&CK DATA SOURCE"],
            data_component=object_details["ATT&CK DATA COMPONENT"],
            source=object_details["SOURCE"],
            relationship=object_details["RELATIONSHIP"],
            target=object_details["TARGET"],
            x_mitre_data_source_id=object_details["ATT&CK DATA SOURCE ID"]
        )
        # Keep a reference for the new object
        if object_details["EVENT ID"] not in created_objects:
            created_objects[object_details["EVENT ID"]] = [new_sdo]
        else:
            created_objects[object_details["EVENT ID"]].append(new_sdo)

    else:
        # Check reference_dict first
        if object_details["name"] in reference_dict:
            # Extract the SDO ID
            id_to_reuse = reference_dict[object_details["name"]]
        # Check created_objects next
        elif object_details["name"] in created_objects:
            # There is no need to continue, the object has already been created.
            return created_objects[object_details["name"]]
        # If neither contain new object, create a new STIX object according to the object_type
        
        if not id_to_reuse:
            ref = {
                "Data Source": "x-mitre-data-source",
                "Data Component": "x-mitre-data-component"
            }
            id_to_reuse = f"{ref[object_type]}--{uuid.uuid4()}"

        match object_type:
            case "Data Source":
                new_sdo = DataSource(
                    id=id_to_reuse,
                    name=object_details["name"],
                    x_mitre_contributors=["Center for Threat-Informed Defense (CTID)"],
                    object_marking_refs=["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                    x_mitre_version="1.0",
                    x_mitre_attack_spec_version="2.1.0",
                    x_mitre_domains=object_details["domain"],
                    created_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                    x_mitre_modified_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                    external_references = [],
                    x_mitre_deprecated=False
                )
            case "Data Component":
                new_sdo = DataComponent(
                    id=id_to_reuse,
                    name=object_details["name"],
                    x_mitre_data_source_ref=object_details["source ref"],
                    x_mitre_version="1.0",
                    x_mitre_attack_spec_version="2.1.0",
                    x_mitre_domains=object_details["domain"],
                    x_mitre_modified_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                    created_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                    object_marking_refs=["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                    allow_custom=True,
                    x_mitre_deprecated=False
                )
            case _:
                raise NotImplementedError("Unexpected object type.")
        # Update input parameters
        created_objects[object_details["name"]] = new_sdo
    return new_sdo


def parse_mappings(mappings_location, config_location, attack_domain, data_sdo_ids, relationship_ids, mapped_sensor_sdos, groups=False):
    """
    Parse the sensor mappings and return a STIX Bundle with relationship objects conveying the mappings in STIX format.

    :param mappings_location the filepath to the mappings CSV file
    :param config_location: the filepath to the JSON configuration file.
    :param relationship_ids is a dict of format {relationship-source-id---relationship-target-id -> (relationship-id, relationship-type)} which maps relationships to desired STIX IDs
    :return List of tuples: (Source Mappings, stix2 Bundle)
    """
    print("reading framework config... ", end="", flush=True)
    # load the mapping config
    with config_location.open("r", encoding="utf-8") as f:
        config = json.load(f)
        version = config["attack_version"]
    print("done")

    attack_data_sources, attack_data_components = load_attack_data(version, attack_domain, groups)

    tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    # build STIX objects
    stix_new_sdo = {}  # Holds all new SDO items
    bundle_tuples = []

    attack_type = attack_domain.split('-')[0]
    mapping_data = [f for f in mappings_location.glob('*.csv') if f.is_file() and attack_type in f.name]

    stix_relationships = {}
    for _csv in mapping_data:
        source = _csv.name[:_csv.name.find("-sensors")]

        curr_bundle_objects = []
        mappings_df = pd.read_csv(_csv, keep_default_na=False, header=0)
        for idx, row in tqdm(list(mappings_df.iterrows()), desc=f"parsing {source} mappings", bar_format=tqdm_format):
            # Check if the data source is already defined in STIX
            # If not, create a new SDO
            data_source_name = row["ATT&CK DATA SOURCE"]
            data_source_id = row["ATT&CK DATA SOURCE ID"]
            if data_source_id == "-1":
                # A new data source
                sdo_details = create_stix_object(
                    reference_dict=data_sdo_ids,
                    created_objects=stix_new_sdo,
                    object_type="Data Source",
                    object_details={
                        "name": data_source_name,
                        "domain": attack_domain
                    }
                )
                # A new custom SDO. Add the new object to the current bundle
                # The newly created SDO will not have all of its fields filled out. Missing fields may be added in the next version.
                # Update the SDO with the missing properties using the following command:
                    # NEW_SDO.new_version(PROPERTY=PROPERTY_VALUE)
                data_source_stix_ID = sdo_details.id
                bundle_append(curr_bundle_objects, sdo_details)
            else:
                data_source_stix_ID = attack_data_sources[data_source_id]

            # Check if the data component is already defined in STIX
            # If not, create a new SDO
            data_component = row["ATT&CK DATA COMPONENT"]
            if data_component in attack_data_components:
                data_component_stix_ID = attack_data_components[data_component]
            else:
                sdo_details = create_stix_object(
                    reference_dict=data_sdo_ids,
                    created_objects=stix_new_sdo,
                    object_type="Data Component",
                    object_details={
                        "name": data_component,
                        "source ref": data_source_stix_ID,
                        "domain": attack_domain
                    }
                )
                if isinstance(sdo_details, DataComponent):
                    # A new custom SDO. The newly created SDO will not have all of its fields filled out. Missing fields may be added in the next version.
                    # Update the SDO with the missing properties using the following command:
                        # NEW_SDO.new_version(PROPERTY=PROPERTY_VALUE)
                    data_component_stix_ID = sdo_details.id
                    bundle_append(curr_bundle_objects, sdo_details)
                
            # Make the mappings SDO
            sdo_details = create_stix_object(
                reference_dict=mapped_sensor_sdos,
                created_objects=stix_new_sdo,
                object_type="Sensor Mapping",
                object_details=row.to_dict()
            )
            bundle_append(curr_bundle_objects, sdo_details)

            # Create a STIX SRO between the Data Source and Data Component
            relation = row["RELATIONSHIP"]
            joined_id = f"{data_source_stix_ID}---{data_component_stix_ID}-{relation}"
            if joined_id in relationship_ids:
                relationship_id = relationship_ids[joined_id]
            else:
                relationship_id = f"relationship--{uuid.uuid4()}"

            relationship = Relationship(
                id = relationship_id,
                source_ref = data_source_stix_ID,
                target_ref = data_component_stix_ID,
                relationship_type = relation,
                allow_custom=True
            )
            bundle_append(curr_bundle_objects, relationship)
            if joined_id not in stix_relationships:
                stix_relationships[joined_id] = relationship

        # Create a bundle for each CSV. Format: (Source Name, Bundle)
        bundle = Bundle(
            objects = curr_bundle_objects,
            allow_custom = True  # Needed since ATT&CK data has custom objects
        )
        bundle_tuples.append((source, bundle))

    # Report on new SDOs created
    print("\nNew STIX Objects:")
    for object in dict(sorted(stix_new_sdo.items(), key=str)):
        if isinstance(stix_new_sdo[object], list):
            # Indicates a SensorMapping
            continue
        print(f"\t{object}\t\t {stix_new_sdo[object]['id'] : >100}")
        
    # Split the objects that will be written to the reference file.
    data_sdos = {_tuple_: stix_new_sdo[_tuple_] for _tuple_ in stix_new_sdo if not isinstance(stix_new_sdo[_tuple_], list)}
    _sensor_sdos = {_tuple_: stix_new_sdo[_tuple_] for _tuple_ in stix_new_sdo if isinstance(stix_new_sdo[_tuple_], list)}
    # Flatten these dictionaries of lists for bundling
    mappings = []
    for _, sdo_list in _sensor_sdos.items():
        mappings.extend(sdo_list)
    
    bundle_tuples.append(("Reference-for", Bundle(
            objects = list(stix_relationships.values()) + list(data_sdos.values()) + mappings,
            allow_custom = True
        )))
    return bundle_tuples


def to_stix_json(bundle_list, output_path):
    """Helper function to write a STIX bundle to a file"""
    for bundle_tuple in bundle_list:
        source, bundle = bundle_tuple
        print(f"Bundling and serializing {source} mappings data to JSON file...")

        output_fname = Path(f"{source}-mappings-enterprise.json")
        path = output_path.joinpath(output_fname)
        with path.open('w', encoding="utf-8") as outfile:
            bundle.fp_serialize(outfile, pretty=False, ensure_ascii=False, sort_keys=True, indent=4, include_optional_defaults=True)
    print(f'\nDone! See {output_path}\n')


def _parse_args():
    ROOT_DIR = Path(__file__).parent.parent.parent

    parser = argparse.ArgumentParser(description="Create STIX files from sensor mapping data")
    parser.add_argument("-attack_domain",
                        dest="attack_domain",
                        help="Attack domain we are mapping. i.e. 'enterprise-attack', 'mobile-attack', 'ics-attack'",
                        type=str,
                        choices=["enterprise-attack", "ics-attack", "mobile-attack"],
                        default="enterprise-attack")
    parser.add_argument("-output_folder",
                        dest="output_location",
                        help="The folder where STIX bundle file will be saved.",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "stix", "enterprise"))
    parser.add_argument("-config_location",
                        dest="config_location",
                        help="filepath to the configuration for the framework",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input", "config.json"))
    parser.add_argument("-groups",
                        action="store_true",
                        help="If specified, create mappings for group objects")
    parser.add_argument("-mappings_location",
                        dest="mappings_location",
                        help="The folder to the CSV spreadsheets to write the mappings",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input",
                            "enterprise", "csv"))
    return parser.parse_args()


def use_reference_file(reference_file):
    """Helper method extract information about STIX objects from a file on disk. Intended to avoid duplication of SDOs."""
    with reference_file.open("r", encoding="utf-8") as f:
        bundle = json.load(f)
    
    relationship_ids = {}
    data_sdo_ids = {}
    mapping_objects = {}

    for sdo in bundle["objects"]:
        if sdo["type"] in ["x-mitre-data-component", "x-mitre-data-source"]:
            data_sdo_ids[sdo["name"]] = sdo["id"]
        elif sdo["type"] == "relationship":
            from_id = f"{sdo['source_ref']}---{sdo['target_ref']}-{sdo['relationship_type']}"
            to_id = sdo["id"]
            relationship_ids[from_id] = to_id
        elif sdo["type"] == "x-mitre-sensor-mapping":
            # Sensor Mapping objects can share the 'event_id' field. 
            # Need to store the entire SDO in order to validate all properties (to reuse the ID)
            if sdo["event_id"] not in mapping_objects:
                mapping_objects[sdo["event_id"]] = [sdo]
            else:
                mapping_objects[sdo["event_id"]].append(sdo)
    # For every Sensor Mapping SDO stored, it should be converted to a SensorMapping custom object for comparison.
    for event_key in mapping_objects:
        for index, sdo_dict in enumerate(mapping_objects[event_key]):
            mapping_objects[event_key][index] = SensorMapping(
                id=sdo_dict["id"],
                event_id=sdo_dict["event_id"],
                description=sdo_dict["description"],
                data_source=sdo_dict["data_source"],
                data_component=sdo_dict["data_component"],
                relationship=sdo_dict["relationship"],
                target=sdo_dict["target"],
                source=sdo_dict["source"],
                x_mitre_data_source_id=sdo_dict["x_mitre_data_source_id"]
            )
    return data_sdo_ids, relationship_ids, mapping_objects


if __name__ == "__main__":
    """Main entry point to STIX file generation for Sensor data."""
    args = _parse_args()

    # Create output directories as needed
    output_location = Path(args.output_location)
    output_location.mkdir(parents=True, exist_ok=True)

    # Check if there are already existing STIX files so STIX IDs don't get replaced on rebuild
    reference_file = [f for f in output_location.glob('Reference-for*.json') if f.is_file() and args.attack_domain.split('-')[0] in f.name]
    if reference_file:
        mapping_data_sdo_ids, relationship_ids, mapped_sensor_sdos = use_reference_file(*reference_file)
    else:
        mapping_data_sdo_ids, relationship_ids, mapped_sensor_sdos = ([] for _ in range(3))
    

    bundles = parse_mappings(
        mappings_location=args.mappings_location,
        config_location=args.config_location,
        attack_domain=args.attack_domain,
        data_sdo_ids=mapping_data_sdo_ids,
        relationship_ids=relationship_ids,
        mapped_sensor_sdos=mapped_sensor_sdos,
        groups= True if args.groups else False)

    to_stix_json(bundles, output_location)
    