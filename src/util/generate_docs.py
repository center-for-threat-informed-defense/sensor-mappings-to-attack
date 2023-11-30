import argparse
import csv
from datetime import datetime
import os
from pathlib import Path
import re


def insert_docs(old_doc, doc_lines, tag):
    start_tag = re.compile(r"\.\. " + tag)
    end_tag = re.compile(r"\.\. /" + tag)
    output = list()

    for line in old_doc:
        if start_tag.search(line):
            break
        output.append(line.rstrip("\n"))
    else:
        raise RuntimeError("Did not find start tag")

    now = datetime.now().isoformat()
    output.append(f".. {tag} Generated at: {now}Z")
    output.append("")
    output.extend(doc_lines)
    output.append(f".. /{tag}")

    for line in old_doc:
        if end_tag.search(line):
            break
    else:
        raise RuntimeError("Did not find end tag")

    for line in old_doc:
        output.append(line.rstrip("\n"))
    output.append("")

    return "\n".join(output)


def write_doc_files(sensor_tables:dict, docs_location:Path):
    for sensor in sensor_tables:
        old_doc = Path(docs_location, f"mapping_{sensor.lower()}.rst")
        tables = sensor_tables[sensor]
        with open(old_doc) as file:
            new_doc = insert_docs(file, tables, "MAPPINGS_TABLE")
        with open(old_doc, "w") as out:
            out.write(new_doc)


def generate_table_from_csv(csv_file):
    """Parse out table data from `csv_file`."""
    obj_lines = []
    with csv_file.open("r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            obj_lines.append({"EVENT ID": row["EVENT ID"],
                              "EVENT DESCRIPTION": row["EVENT DESCRIPTION"],
                              "ATT&CK DATA SOURCE": row["ATT&CK DATA SOURCE"],
                              "ATT&CK DATA COMPONENT": row["ATT&CK DATA COMPONENT"]
                              })
    return obj_lines


def csv_to_tables(attack_types, mappings_location):
    """Goes through the CSV files for `attack_types` and extracts data for Sphinx tables."""
    
    sensor_table_lists = {}
    # Key = Sensor, Value = [{Attack_Type1: obj_lines}, {Attack_Type2: obj_lines}, ...]
    for attack_type in attack_types:
        current_dir = Path(mappings_location, attack_type, "csv")
        csv_files = [filename for filename in current_dir.iterdir() if filename.is_file()]

        # Work on each CSV file
        for _csv in csv_files:
            _sensor_ = _csv.name.split(f"-sensors-mappings-{attack_type}")[0]
            obj_lines = generate_table_from_csv(_csv)
            
            if _sensor_ in sensor_table_lists:
                sensor_table_lists[_sensor_].append({attack_type: obj_lines})
            else:
                sensor_table_lists[_sensor_] = [{attack_type: obj_lines}]
    return sensor_table_lists


def generate_mappings_table(sensor_table_lists):
    """Consolidates output from `csv_to_tables` and returns it as a dictionary. Key is a sensor name, Value is a list of table data."""
    sensor_tables = {}
    for sensor in sensor_table_lists:
        attack_types: list = sensor_table_lists[sensor]
        # attack_types is a List of Dictionaries. 
        # Key is the attack_type, Value is a list of rows (dictionaries)
        obj_lines = []
        for attack_type_dict in attack_types:
            attack_type = list(attack_type_dict.keys())[0]
            if attack_type == "ics":
                attack_type = attack_type.upper()
            else:
                attack_type = attack_type.title()

            obj_lines.extend(header_generator(attack_type, "-"))
            
            # Add table header
            obj_lines.extend(table_start(sensor))

            rows = attack_type_dict[attack_type.lower()]
            for row in sorted(rows, key=lambda i: i['EVENT ID']):
                obj_lines.extend(extract_row_data(row))
            
        sensor_tables[sensor] = obj_lines
    return sensor_tables


def extract_row_data(row: dict):
    result = []
    result.append(f"  * - {row['EVENT ID']}")

    # Handle potential multi-line inputs
    description = "".join(row['EVENT DESCRIPTION'].splitlines())
    result.append(f"    - {description}")

    result.append(f"    - {row['ATT&CK DATA SOURCE']}")
    result.append(f"    - {row['ATT&CK DATA COMPONENT']}")
    result.append("")

    return result


def header_generator(variable_name: str, symbol: str):
    """Generates reusable underline for documents based on `variable_name`"""
    _header = []
    _header.append(variable_name)
    _header.append("".join(f"{symbol}" for _ in range(len(variable_name))))
    return _header


def table_start(sensor):
    """Helper function to create the start of a table"""
    custom_widths = {
        "cloudtrail": 40,
        "osquery": 40,
        "sysmon": 10,
        "winevtx": 10,
        "zeek": 40
    }
    table_header = []
    table_header.append(".. list-table::")
    table_header.append(f"  :widths: {custom_widths.get(sensor.lower(), 35)} 30 20 25")
    table_header.append("  :header-rows: 1")
    table_header.append("")
    table_header.append("  * - EVENT ID")
    table_header.append("    - EVENT DESCRIPTION")
    table_header.append("    - ATT&CK DATA SOURCE")
    table_header.append("    - ATT&CK DATA COMPONENT")
    table_header.append("")
    return table_header


def _parse_args():
    ROOT_DIR = Path(__file__).parent.parent.parent
    parser = argparse.ArgumentParser(description="Generate docs for mappings")
    parser.add_argument("-docs",
                        dest="docs_location",
                        help="Path to documentation files to edit",
                        type=Path,
                        default=Path(ROOT_DIR, "docs", "levels"))
    parser.add_argument("-mappings",
                        dest="mappings_location",
                        help="Path to mapping files directory",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input"))
    return parser.parse_args()


def main():
    args = _parse_args()

    attack_types = [i for i in os.listdir(args.mappings_location) if Path(args.mappings_location, i).is_dir()]
    sensor_table_lists = csv_to_tables(attack_types, args.mappings_location)
    sensor_table_data = generate_mappings_table(sensor_table_lists)
    write_doc_files(sensor_table_data, args.docs_location)


if __name__ == "__main__":
    main()
