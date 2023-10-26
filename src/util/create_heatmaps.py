import json
from pathlib import Path
import argparse
import shutil

import requests
from stix2 import Filter, MemoryStore


def create_comparison_layer(input_dir, domain, version):
    """Take all created layers and create a single sheet that combines comments."""
    files_to_combine = [file for file in input_dir.glob("*heatmap.json") if file.is_file() and "comparison" not in file.name.lower()]
    
    # Combine all the technique dictionaries
    layers = []
    for file in files_to_combine:
        with file.open("r", encoding="utf-8") as f:
            layers.append(json.load(f))

    # Each object in all_techniques is a list of technique dictionaries
    all_techniques = {}
    
    sensor_names = [layer["name"] for layer in layers]
    for layer in layers:
        technique_dicts = layer["techniques"]
        for technique in technique_dicts:
            attack_id = technique["techniqueID"]
            comment = technique["comment"]
            if attack_id not in all_techniques:
                all_techniques[attack_id] = {
                    "score": 1,
                    "comment": comment
                }
            else:
                all_techniques[attack_id]["comment"] += f"\n\n{comment}"

    # Calculate score at the end
    for technique in all_techniques:
        val = 0
        comment = all_techniques[technique]["comment"]
        for name in sensor_names:
            if name in comment:
                val += 1
        all_techniques[technique]["score"] = val

    # Convert all_techniques to a list of technique dictionaries
    techniques = []
    for technique_dict in all_techniques:
        techniques.append({
            "techniqueID": technique_dict,
            "score": all_techniques[technique_dict]["score"],
            "comment": all_techniques[technique_dict]["comment"]
        })

    compared_layer = create_layer("Sensor Comparisons", domain, techniques, version)
        
    output_path = Path(input_dir, "sensor-comparison-heatmap.json")
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(compared_layer, f, indent=4)


def create_layer(name, domain, techniques, version, description=""):
    """create a Layer"""
    min_mappings = min(map(lambda t: t["score"], techniques)) if len(techniques) > 0 else 0
    max_mappings = max(map(lambda t: t["score"], techniques)) if len(techniques) > 0 else 100
    gradient = ["#ff6666", "#ffe766ff", "#8ec843"]
    # check if all the same count of mappings
    if max_mappings - min_mappings == 0:
        min_mappings = 0  # set low end of gradient to 0

    # convert version to just major version
    if version.startswith("v"):
        version = version[1:]
    version = version.split(".")[0]

    return {
        "name": name,
        "versions": {
            "navigator": "4.8.2",
            "layer": "4.4",
            "attack": version
        },
        "sorting": 0,
        "description": description,
        "domain": domain,
        "techniques": techniques,
        "gradient": {
            "colors": gradient,
            "minValue": min_mappings,
            "maxValue": max_mappings
        },
    }


def layer_technique_field(attack_id, event_ids, sensor_name):
    """create a technique for a layer"""
    return {
        "techniqueID": attack_id,
        "score": 1, 
        "comment": f"{sensor_name}: {', '.join(sorted(event_ids))}",  # list of mapped event IDs
    }


def to_technique_list(mappings, attack_data):
    """
    Take `mappings` MemoryStore object and `attack_data` MemoryStore object. Query the x_mitre_data_source field and return found techniques as a dictionary(attack id -> set of event IDs).
    """
    techniques = {}
    for mapping in mappings.query():
        if mapping["type"] != "x-mitre-sensor-mapping":
            continue
        attack_data_source_query = f"{mapping['data_source']}: {mapping['data_component']}"
        atk_patterns = attack_data.query(Filter("x_mitre_data_sources", "contains", attack_data_source_query))
        if not atk_patterns:
            continue  # Skip new data source & data component combinations
        event_id = mapping["event_id"]
        _techniques = [attack_id["external_references"][0]["external_id"] for attack_id in atk_patterns if not attack_id["x_mitre_is_subtechnique"]]
        for attack_id in _techniques:
            if attack_id in techniques:
                techniques[attack_id].add(event_id)
            else:
                techniques[attack_id] = set([event_id])
    return techniques


def create_mappings_heatmap(files_to_visualize, out_dir, attack_data, domain, version, clear):
    for current_file in files_to_visualize:
        sensor_name = current_file.name[:current_file.name.find("-mappings")]
        print(f"loading mappings from {current_file} ... ", end="", flush=True)
        with current_file.open("r", encoding="utf-8") as f:
            mappings = MemoryStore(stix_data=json.load(f)["objects"])
        print("done")

        print(f"generating layer for {sensor_name}... ", end="", flush=True)
        tech_dict = to_technique_list(mappings, attack_data)
        techs = [layer_technique_field(attack_id, tech_dict[attack_id], sensor_name) for attack_id in tech_dict]
        layer = create_layer(name=sensor_name, domain=domain, techniques=techs, version=version)
        
        if clear:
            print("clearing layers directory...", end="", flush=True)
            shutil.rmtree(out_dir, ignore_errors=True)
            print("done")

        # make path if it does not exist
        print(f"writing layers for {sensor_name}... ", end="", flush=True)
        layer_path = Path(out_dir, f"{sensor_name}-heatmap.json")
        layer_path.parent.mkdir(parents=True, exist_ok=True)
        with layer_path.open("w", encoding="utf-8") as f:
            json.dump(layer, f, indent=4)
        print("done\n")


def _parse_args():
    ROOT_DIR = Path(__file__).parent.parent.parent

    parser = argparse.ArgumentParser(description="Create ATT&CK Navigator layers from sensor data mappings")
    parser.add_argument("-mappings_location",
                        dest="mappings_location",
                        help="filepath to the STIX Bundle mappings",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "stix",
                            "enterprise"))
    parser.add_argument("-domain",
                        dest="domain",
                        help="The domain of ATT&CK to visualize",
                        type=str,
                        choices=["enterprise-attack", "ics-attack", "mobile-attack"],
                        default="enterprise-attack")
    parser.add_argument("-output",
                        dest="output_location",
                        help="The folder where layers will be saved to.",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "stix", "layers"))
    parser.add_argument("-version",
                        dest="version",
                        help="which ATT&CK version to use",
                        default="13.1")
    parser.add_argument("-clear",
                        action="store_true",
                        help="if flag specified, will remove the contents the output folder before writing layers")

    return parser.parse_args()


def main():
    args = _parse_args()
    domain_dirs = {
        "enterprise-attack": "enterprise",
        "ics-attack": "ics",
        "mobile-attack": "mobile",
    }
    out_dir = Path(args.output_location, domain_dirs[args.domain])

    url = f"https://raw.githubusercontent.com/mitre/cti/ATT%26CK-v{args.version}/{args.domain}/{args.domain}.json"
    print(f"downloading ATT&CK data from {url} ... ", end="", flush=True)
    attack_data = MemoryStore(stix_data=requests.get(url, verify=True).json()["objects"])
    print("done")

    files_to_visualize = [file for file in args.mappings_location.glob('*mappings*.json') if file.is_file() and domain_dirs[args.domain] in file.name and 'reference' not in file.name.lower()]

    create_mappings_heatmap(files_to_visualize, out_dir, attack_data, args.domain, args.version, args.clear)
    create_comparison_layer(out_dir, args.domain, args.version)


if __name__ == "__main__":
    main()