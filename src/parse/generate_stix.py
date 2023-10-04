import uuid
import json
from pathlib import Path
import argparse
import datetime

import requests
from tqdm import tqdm
import pandas as pd
from stix2.properties import StringProperty, ReferenceProperty, EnumProperty, ListProperty
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
        ("x_mitre_modified_by_ref", ReferenceProperty(valid_types=['identity']))
    ]
)


class DataSource():
    """Custom MITRE Data Source STIX object."""
    def __init__(self, **kwargs):
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
        ("object_marking_refs", ListProperty(ReferenceProperty(valid_types=['marking-definition'])))
    ]
)


class DataComponent():
    """Custom MITRE Data Component STIX object."""
    def __init__(self, **kwargs):
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
        ("x_mitre_data_source_id", StringProperty()),
        ("external_references", ListProperty(ExternalReference))
    ]
)


class SensorMapping():
    """Custom MITRE sensor data mapping STIX object."""
    def __init__(self, **kwargs):
        pass



def load_attack_data(version, attack_domain="enterprise-attack"):
    """Load ATT&CK STIX data to create reference dictionaries to use when building STIX Bundles."""

    tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    # load ATT&CK STIX data
    print("downloading ATT&CK data... ", end="", flush=True)
    attack_url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{attack_domain}/{attack_domain}-{version}.json"
    print(attack_url)
    attack_data = requests.get(attack_url, verify=True).json()["objects"]
    print("done")

    # Now filter attack_data to only have the information we require
    source_ids_references = {}
    component_ids = {}
    tqdm_format = tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

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
                    # Map the ATT&CK Data Source ID to tuple (data source stixID, external references dict)
                    source_ids_references[reference["external_id"]] = (attack_object["id"], attack_object["external_references"])

        elif attack_object["type"] == type_data_component:
            component_ids[attack_object["name"]] = attack_object["id"]
    return (source_ids_references, component_ids)


def parse_mappings(mappings_location, config_location, relationship_ids={}, attack_domain="enterprise-attack"):
    """
    Parse the sensor mappings and return a STIX Bundle with relationship objects conveying the mappings in STIX format.

    :param mappings_location the filepath to the mappings CSV file
    :param config_location: the filepath to the JSON configuration file.
    :param relationship_ids is a dict of format {relationship-source-id---relationship-target-id -> relationship-id} which maps relationships to desired STIX IDs
    :return List of tuples: (Source Mappings, stix2 Bundle)
    """
    print("reading framework config...", end="", flush=True)
    # load the mapping config
    with config_location.open("r", encoding="utf-8") as f:
        config = json.load(f)
        version = config["attack_version"]
    print("done")

    data_source_info, data_component_info = load_attack_data(version, attack_domain)

    # Match case of attack_data for Data Components to the mappings
    data_component_info = {k.replace(" ", "_").lower(): v for k,v in data_component_info.items()}
    tqdm_format = tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    # build STIX objects
    stix_new_objects = {}
    bundle_tuples = []

    attack_type = attack_domain.split('-')[0]
    mapping_data = [f for f in mappings_location.glob('*.csv') if f.is_file() and attack_type in f.name]

    sources_reference = pd.read_csv(Path(mappings_location.parent.parent, f'{attack_domain}-v{version}-datasources.csv'))

    for _csv in mapping_data:
        stix_relationships = {}
        stix_objects = []  # Holds all new data component SDOs, mappings SDOs and new data source SDOs.
        mappings_df = pd.read_csv(_csv, keep_default_na=False, header=0)
        for idx, row in tqdm(list(mappings_df.iterrows()), desc="parsing mappings", bar_format=tqdm_format):
            # Check if the data source is already defined in STIX
            # If not, create a new SDO
            data_source_name = row["ATT&CK DATA SOURCE"]
            data_source_id = row["ATT&CK DATA SOURCE ID"]
            if data_source_id == "-1":
                # Check if it has already been created
                if data_source_name in stix_new_objects:
                    data_source_stix_ID = stix_new_objects[data_source_name].id
                    data_source_ext_refs = []
                else:
                    data_source_sdo = DataSource(
                        name=data_source_name,
                        x_mitre_contributors=["Center for Threat-Informed Defense (CTID)"],
                        object_marking_refs=["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                        x_mitre_version="1.0",
                        x_mitre_attack_spec_version="2.1.0",
                        x_mitre_domains=attack_domain,
                        created_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                        x_mitre_modified_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5"
                        )
                    stix_objects.append(data_source_sdo)
                    # This SDO will not have all of its fields filled out. They may be added in the next version.
                    # Update the SDO with the missing properties using the following command:
                        # data_source_sdo.new_version(x_mitre_platforms=[""])
                    
                    # Create a new Data Source ID
                    highest_ds_id = sources_reference["ID"].apply(lambda id: int(id[-2:]) if pd.notna(id) else id).max()
                    new_ds_id = f"DS{highest_ds_id+1:04}"
                    # Add it to sources_reference as a new row to avoid duplication as we continue to parse mappings.
                    sources_reference.loc[len(sources_reference)] = {
                        "name": data_source_name,
                        "ID": new_ds_id,
                        "type": "datasource"
                    }
                    data_source_stix_ID = data_source_sdo.id
                    data_source_ext_refs = []
                    stix_new_objects[data_source_name] = data_source_sdo
            else:
                data_source_stix_ID, data_source_ext_refs = data_source_info[data_source_id]

            # Check if the data component is already defined in STIX
            # If not, create a new SDO
            data_component = row["ATT&CK DATA COMPONENT"]
            if data_component not in data_component_info and data_component not in stix_new_objects:
                data_component_sdo = DataComponent(
                    name=data_component,
                    # This SDO will not have a description available. One may be added in the next version.
                    x_mitre_data_source_ref=data_source_stix_ID,
                    x_mitre_version="1.0",
                    x_mitre_attack_spec_version="2.1.0",
                    x_mitre_domains=attack_domain,
                    x_mitre_modified_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                    created_by_ref="identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
                    object_marking_refs=["marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"],
                    allow_custom=True
                )
                stix_new_objects[data_component] = data_component_sdo
                stix_objects.append(data_component_sdo)

                data_component_stix_ID = data_component_sdo.id
            elif data_component not in data_component_info and data_component in stix_new_objects:
                stix_objects.append(stix_new_objects[data_component])
                data_component_stix_ID = stix_new_objects[data_component].id
            else:
                data_component_stix_ID = data_component_info[data_component]

            # Make the mappings SDO
            mapping = SensorMapping(
                event_id=row["EVENT ID"],
                description=row["EVENT DESCRIPTION"],
                data_source=row["ATT&CK DATA SOURCE"],
                data_component=row["ATT&CK DATA COMPONENT"],
                source=row["SOURCE"],
                relationship=row["RELATIONSHIP"],
                target=row["TARGET"],
                x_mitre_data_source_id=row["ATT&CK DATA SOURCE ID"],
                external_references=data_source_ext_refs,
            )
            stix_objects.append(mapping)

            # Create a STIX SRO between the Data Source and Data Component
            relation = row["RELATIONSHIP"]

            joined_id = f"{data_source_stix_ID}---{data_component_stix_ID}"
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
            if joined_id not in stix_relationships:
                stix_relationships[joined_id] = relationship

        # Create a bundle for each CSV.
        # Format: (Source Name, Bundle)
        source = _csv.name.find("-sensors")
        source = _csv.name[:source]
        bundle = Bundle(
            objects = stix_objects + list(stix_relationships.values()),
            allow_custom=True  # Needed since ATT&CK data has custom objects
        )
        bundle_tuples.append((source, bundle))
    # Report on new SDOs created
    print("New STIX Objects:")
    for object in stix_new_objects:
        print(f"\t{object}\t-- {stix_new_objects[object].id}")
    return bundle_tuples


def to_stix_json(bundle_list, output_path, pretty=False):
    for bundle_tuple in bundle_list:
        source, bundle = bundle_tuple
        print(f"Bundling and serializing {source} mappings data to JSON file...")

        stix_json = json.loads(bundle.serialize())
        output_fname = Path(f"{source}-mappings-enterprise.json")
        with open(output_path.joinpath(output_fname), 'w') as f:
            if pretty:
                _indent = 4
            else:
                _indent = None
            json.dump(stix_json, f, indent=_indent)

    print(f'Done! See {output_path}\n')


def _parse_args():
    ROOT_DIR = Path(__file__).parent.parent.parent

    parser = argparse.ArgumentParser(description="Create STIX files from sensor mapping data")
    parser.add_argument("-attack_domain",
                        dest="attack_domain",
                        help="Attack domain we are mapping. i.e. 'enterprise-attack', 'mobile-attack', 'ics-atack'",
                        type=str,
                        choices=["enterprise-attack", "ics-attack", "mobile-attack", "groups-attack"],
                        default="enterprise-attack")
    parser.add_argument("-output_folder",
                        dest="output_location",
                        help="The folder where STIX bundle file will be saved.",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "stix", "enterprise"))
    parser.add_argument("-config-location",
                        dest="config_location",
                        help="filepath to the configuration for the framework",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input", "config.json"))
    parser.add_argument("-mappings-location",
                        dest="mappings_location",
                        help="filepath to the CSV spreadsheet to write the mappings",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input",
                            "enterprise", "csv"))
    parser.add_argument("-pretty-json",
                        dest="pretty_json",
                        help="Pretty printing for JSON STIX file output.",
                        action="store_true",
                        default=False)
    
    return parser.parse_args()


if __name__ == "__main__":
    """Main entry point to STIX file generation for Sensor data."""

    args = _parse_args()

    # Create output directories as needed
    output_location = Path(args.output_location)
    output_location.mkdir(parents=True, exist_ok=True)

    bundles = parse_mappings(mappings_location=args.mappings_location, config_location=args.config_location, attack_domain=args.attack_domain)

    to_stix_json(bundles, output_location, pretty=args.pretty_json)