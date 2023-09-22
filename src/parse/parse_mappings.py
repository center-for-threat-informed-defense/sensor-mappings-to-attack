import json
import uuid
from pathlib import Path

from colorama import Fore
from stix2 import AttackPattern, Bundle, Relationship
from tqdm import tqdm
import pandas as pd
import requests


# What fields do each SDO need?
# This is determined by the Data Component

# Would it be easier to create a custom one first?
def main():
    # build mapping ID helper lookup to avoid overwriting STIX IDs
    mapping_relationship_ids = {}


def dict_lookup(lookup_dict, term):
    """:return item from dictionary if present. Exits otherwise."""
    if term not in lookup_dict:
        import pdb
        print(f"Term: {term}")
        pdb.set_trace()
        message = f"ERROR: cannot find '{term}' in lookup dictionary..."
        print(Fore.RED + message,  Fore.RESET)
        exit()
    return lookup_dict[term]


def parse_mappings(mappings_path, relationship_ids, config_location, attack_domain="enterprise-attack"):
    """
    Parse the sensor mappings and return a STIX Bundle with relationship objects conveying the mappings in STIX format.

    :param mappings_path the filepath to the mappings TSV file
    :param relationship_ids is a dict of format
        {relationship-source-id---relationship-target-id -> relationship-id} which
        maps relationships to desired STIX IDs
    :param config_location: the filepath to the JSON configuration file.
    :return stix2 Bundle
    """
    print("reading framework config...", end="", flush=True)
    # load the mapping config
    with config_location.open("r", encoding="utf-8") as f:
        config = json.load(f)
        version = config["attack_version"]
    print("done")

    tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    # load ATT&CK STIX data
    print("downloading ATT&CK data... ", end="", flush=True)
    attack_url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{attack_domain}/{attack_domain}-{version}.json"
    print(attack_url)
    attack_data = requests.get(attack_url, verify=True).json()["objects"]
    print("done")

    # Now filter attack_data to only have the information we require
    datasourceid_to_stix = {}
    datacomponent_to_stix = {}
    tqdm_format = tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    attack_url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{attack_domain}/{attack_domain}-{version}.json"
    print(attack_url)
    attack_data = requests.get(attack_url, verify=True).json()["objects"]

    for attack_object in tqdm(attack_data, desc=f"parsing v{version} {attack_domain} data", bar_format=tqdm_format):
        type_check_data_source = "x-mitre-data-source"
        type_check_data_component = "x-mitre-data-component"
        if attack_object["type"] == type_check_data_source:
            if "external_references" not in attack_object:
                continue  # skip objects without IDs
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            for reference in attack_object["external_references"]:
                if reference["source_name"] == "mitre-attack":
                    datasourceid_to_stix[reference["external_id"]] = attack_object

        elif attack_object["type"] == type_check_data_component:
            datacomponent_to_stix[attack_object["name"]] = attack_object

    # build mapping relationships
    stix_relationships = {}
    mappings_df = pd.read_csv(mappings_path, sep=",", keep_default_na=False, header=0)

    for index, row in tqdm(list(mappings_df.iterrows()), desc="parsing mappings", bar_format=tqdm_format):
        from_id = dict_lookup(veris_path_to_stix_id, row["VERIS PATH"])
        to_id = dict_lookup(attackid_to_stixid, row["TECHNIQUE ID"])
        joined_id = f"{from_id}---{to_id}"

        if joined_id in relationship_ids:
            relationship_id = relationship_ids[joined_id]
        else:
            relationship_id = f"relationship--{uuid.uuid4()}"

        # build the mapping relationship
        relationship = Relationship(
            id=relationship_id,
            source_ref=from_id,
            target_ref=to_id,
            relationship_type="related-to",
        )
        if joined_id not in stix_relationships:
            stix_relationships[joined_id] = relationship

    # construct and return the bundle with relationships
    return Bundle(*stix_relationships.values())


def read_dataframes(mappings_location, attack_type="enterprise"):
    # Read the dataframes row by row
    # Extract the data source & component 
    # Create SDOs
    ROOT_DIR = Path(__file__)
    spreadsheets = [f for f in mappings_location.glob('*.csv') if f.is_file() and attack_type in f.name]
    
    for _csv in spreadsheets:
        mappings_df = pd.read_csv(_csv, keep_default_na=False, header=0)
        for idx, row in mappings_df.iterrows():
            data_src = row["Data Source"]
            data_cmp = row["Data Component"]
            

# - create STIX objects and link them to Data Source and Data Component fields
# - SDO object for Data Source
# - Reference to SDO for Data Component -- refer to enterprise-data.13.1.json
#             - SRO object for Relationship: https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_cqhkqvhnlgfh
#         - Will have to handle all enumerations -- 5 sources (Sysmon, WinEvtx, Zeek, Auditd, OSQuery) and ATT&CK variations (Enterprise, Mobile, ICS)

def create_stix_dicts():
    datasource_attackid_to_stixid = {}
    datacomponent_attackid_to_stixid = {}
    version = "13.1"
    attack_domain = "enterprise-attack"
    tqdm_format = tqdm_format = "{desc}: {percentage:3.0f}% |{bar}| {elapsed}<{remaining}{postfix}"

    attack_url = f"https://raw.githubusercontent.com/mitre-attack/attack-stix-data/master/{attack_domain}/{attack_domain}-{version}.json"
    print(attack_url)
    attack_data = requests.get(attack_url, verify=True).json()["objects"]

    for attack_object in tqdm(attack_data, desc=f"parsing v{version} {attack_domain} data", bar_format=tqdm_format):
        type_check_data_source = "x-mitre-data-source"
        type_check_data_component = "x-mitre-data-component"
        if attack_object["type"] == type_check_data_source:
            if "external_references" not in attack_object:
                continue  # skip objects without IDs
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            for reference in attack_object["external_references"]:
                if reference["source_name"] == "mitre-attack":
                    datasource_attackid_to_stixid[reference["external_id"]] = attack_object["id"]

        elif attack_object["type"] == type_check_data_component:
            if "external_references" not in attack_object:
                continue  # skip objects without IDs
            if attack_object.get("revoked", False):
                continue  # skip revoked objects
            if attack_object.get("x_mitre_deprecated", False):
                continue  # skip deprecated objects

            # map attack ID to stix ID
            for reference in attack_object["external_references"]:
                if reference["source_name"] == "mitre-attack":
                    datacomponent_attackid_to_stixid[reference["external_id"]] = attack_object["id"]