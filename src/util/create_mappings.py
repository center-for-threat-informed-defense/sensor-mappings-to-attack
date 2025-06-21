import argparse
import csv
import json
from pathlib import Path

import pandas as pd


def standardize(sheet, *columns_to_exclude):
    """Helper method to standardize columns used for STIX data."""
    skip = ["Worksheet Name", "Event Description", "Event ID"] + list(*columns_to_exclude)

    for idx, row in sheet.iterrows():
        # Pandas does not have a good way to select only string values in a column, so we iterate by row to do our replacements.
        for col in sheet.columns:
            if pd.isna(row[col]):
                continue
            elif isinstance(row[col], str):
                sheet.loc[idx, col] = sheet.loc[idx, col].strip()
                if col in skip:
                    # Only strip out the whitespace from this column, iff row[col] is a string
                    continue
                else:
                    # Match case
                    sheet.loc[idx, col] = sheet.loc[idx, col].replace(" ", "_")
                    sheet.loc[idx, col] = sheet.loc[idx, col].lower()
            # Skip non-string rows
    sheet.drop_duplicates(inplace=True, ignore_index=True)
    # After dropping duplicates, revert changes
    for idx, row in sheet.iterrows():
        for col in sheet.columns:
            if pd.isna(row[col]):
                continue
            elif isinstance(row[col], str):
                if col in skip:
                    continue
                else:
                    sheet.loc[idx, col] = sheet.loc[idx, col].replace("_", " ")
                    sheet.loc[idx, col] = sheet.loc[idx, col].title()
                    sheet.loc[idx, col] = sheet.loc[idx, col].replace("Wmi", "WMI")
            # Skip non-string rows


def get_sheets(spreadsheet_location, config_location):
    """Helper method to separate combined Excel sheet into individual Dataframes"""
    with config_location.open("r", encoding="utf-8") as f:
        config = json.load(f)
        version = config["attack_version"]

    df = pd.read_excel(spreadsheet_location, sheet_name="Combined Events", usecols="A,C:I")
    standardize(df)

    # Merge in the Data Source ID's from the ATT&CK Data Source CSV
    datasource_csv_location = spreadsheet_location.parent.parent.parent
    data_source_ids = pd.read_csv(Path(datasource_csv_location, f"enterprise-attack-v{version}-datasources.csv"), usecols=[0, 1])

    df = df.merge(data_source_ids, how="left", left_on="Data Source", right_on="name")
    df.drop(columns=["name"], inplace=True)
    df.rename(columns={"ID":"Data Source ID"}, inplace=True)
    df = df[['Worksheet Name', 'Data Source', 'Data Source ID', 'Data Component', 'Event Description',
        'Event ID', 'Source', 'Relationship', 'Target']]
    df["Data Source ID"] = df["Data Source ID"].apply(lambda n: -1 if pd.isna(n) else n)
    # Where a value of `-1` indicates that this is a new ATT&CK Data Source

    worksheet_names = df["Worksheet Name"].dropna().unique()
    sheets = []
    for _worksheet in worksheet_names:
        _df = df[df["Worksheet Name"] == _worksheet].reset_index(drop=True)
        sheets.append((_df, _worksheet))
    return sheets


def generate_csv_spreadsheet(sheets, mappings_location):
    """Reads the main XSLX mappings file and creates a spreadsheet for the mappings in CSV"""
    if not mappings_location.exists():
        mappings_location.mkdir(parents=True)

    for sheet, name in sheets:
        with mappings_location.joinpath(f"{name}-sensors-mappings-enterprise.csv").open('w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['EVENT ID', 'EVENT DESCRIPTION', 'ATT&CK DATA SOURCE ID', 'ATT&CK DATA SOURCE', 'ATT&CK DATA COMPONENT', 'SOURCE', 'RELATIONSHIP', 'TARGET']
            dataframe_fields = ['Event ID', 'Event Description', 'Data Source ID', 'Data Source', 'Data Component', 'Source', 'Relationship', 'Target']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for idx, row in sheet.iterrows():
                is_mapped = (pd.notna(row["Data Source"])) and (pd.notna(row["Data Component"])) and (pd.notna(row["Relationship"]))
                if not is_mapped:
                    # Skip this row
                    continue
                csv_row = {}
                for i in range(len(fieldnames)):
                    if pd.isna(row[dataframe_fields[i]]):
                        csv_row[fieldnames[i]] = None
                    else:
                        csv_row[fieldnames[i]] = row[dataframe_fields[i]]
                writer.writerow(csv_row)
                # Skip any rows without mappable fields


def _parse_args():
    ROOT_DIR = Path(__file__).parent.parent.parent

    parser = argparse.ArgumentParser(description="Create mappings from sensors data")
    parser.add_argument("-config_location",
                        dest="config_location",
                        help="filepath to the configuration for the framework",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input", "config.json"))
    parser.add_argument("-spreadsheet_location",
                        dest="spreadsheet_location",
                        help="filepath to the Excel spreadsheet for the mappings",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input",
                            "enterprise", "xlsx", "Sensor ID to Data Source to API v2.xlsx"))
    parser.add_argument("-mappings_location",
                        dest="mappings_location",
                        help="filepath to the folder to write CSV spreadsheets",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input",
                            "enterprise", "csv"))
    return parser.parse_args()


def main():
    args = _parse_args()
    sheets = get_sheets(args.spreadsheet_location, args.config_location)
    generate_csv_spreadsheet(sheets, args.mappings_location)


if __name__ == '__main__':
    main()

