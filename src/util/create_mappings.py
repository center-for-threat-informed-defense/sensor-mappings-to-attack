import argparse
import csv
import json
from pathlib import Path

import numpy as np
import pandas as pd

def standardize(sheet):
        """Helper method to standardize columns used for STIX data."""
        for col in sheet.columns:
            # Remove whitespace
            for idx, row in sheet.iterrows():
                # Pandas does not have a good way to select only string values in a column, so we iterate by row to do our replacements.
                if isinstance(row[col], str):
                    sheet.loc[:, col] = sheet.loc[:, col].str.strip()
                    if col in ["Worksheet Name", "Event Description", "ID"]:
                        # Avoid modifying these columns
                        continue
                    # Match case
                    sheet.loc[:, col] = sheet.loc[:, col].str.replace(" ", "_")
                    sheet.loc[:, col] = sheet.loc[:, col].str.lower()
        sheet.drop_duplicates(inplace=True, ignore_index=True)


def get_sheets(spreadsheet_location):
    """Helper method to separate combined Excel sheet into individual Dataframes"""
    df = pd.read_excel(spreadsheet_location, header=1, sheet_name="Combined Events", usecols="A,C:I")
    standardize(df)

    # Merge in the Data Source ID's from the ATT&CK Data Source CSV
    datasource_csv_location = spreadsheet_location.parent.parent.parent
    data_source_ids = pd.read_csv(Path(datasource_csv_location, "enterprise-attack-v13.1-datasources.csv"), usecols=[0, 1])
    standardize(data_source_ids)
    
    df = df.merge(data_source_ids, how="left", left_on="Data Source", right_on="name")
    df.drop(columns=["name"], inplace=True)
    df.rename(columns={"ID":"Data Source ID"}, inplace=True)
    df = df[['Worksheet Name', 'Data Source', 'Data Source ID', 'Data Component', 'Event Description',
        'Event ID', 'Source', 'Relationship', 'Target']]
    df["Data Source ID"] = df["Data Source ID"].apply(lambda n: -1 if pd.isna(n) else n)
    # Where a value of `-1` indicates that there is no Data Source

    worksheet_names = df["Worksheet Name"].unique()
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
        with mappings_location.joinpath(f"{name}-sensors-mappings-enterprise.csv").open('w', newline='\n', encoding='utf-8') as csvfile:
            fieldnames = ['EVENT ID', 'EVENT DESCRIPTION', 'ATT&CK DATA SOURCE ID', 'ATT&CK DATA SOURCE', 'ATT&CK DATA COMPONENT', 'SOURCE', 'RELATIONSHIP', 'TARGET']
            dataframe_fields = ['Event ID', 'Event Description', 'Data Source ID', 'Data Source', 'Data Component', 'Source', 'Relationship', 'Target']

            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            
            for idx, row in sheet.iterrows():
                csv_row = {}
                for i in range(len(fieldnames)):
                    if pd.isna(row[dataframe_fields[i]]):
                           continue
                    csv_row[fieldnames[i]] = row[dataframe_fields[i]]
                is_mapped = (pd.notna(row["Data Source"])) and (pd.notna(row["Data Component"])) and (pd.notna(row["Relationship"]))
                if is_mapped:
                    writer.writerow(csv_row)
                # Skip any rows without mappable fields


def generate_supporting_csv(spreadsheet_location):
    """This is a helper script to intake the ATT&CK framework relating to Data Sources."""
    
    output_folder = spreadsheet_location.parent.parent.parent
    _input = Path(spreadsheet_location.parent, f"enterprise-attack-v13.1-datasources.xlsx")

    all_data_sources = pd.read_excel(_input, sheet_name="datasources", usecols="A:J")

    # Split the dataframes
    data_components_df = all_data_sources.loc[all_data_sources["type"] == "datacomponent"].reset_index(drop=True)
    data_sources_df = all_data_sources.loc[all_data_sources["type"] == "datasource"].reset_index(drop=True)

    # Save to `output_folder`
    data_sources_df.to_csv(Path(output_folder, f"enterprise-attack-v13.1-datasources.csv"), index=False)
    data_components_df.to_csv(Path(output_folder, f"enterprise-attack-v13.1-datacomponents.csv"), index=False)


def _parse_args():
    ROOT_DIR = Path(__file__).parent.parent.parent

    parser = argparse.ArgumentParser(description="Create useful info from sensors mappings")
    parser.add_argument("-config-location",
                        dest="config_location",
                        help="filepath to the configuration for the framework",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input", "config.json"))
    parser.add_argument("-spreadsheet-location",
                        dest="spreadsheet_location",
                        help="filepath to the Excel spreadsheet for the mappings",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input", 
                            "enterprise", f"xlsx", f"Sensor ID to Data Source to API v2.xlsx"))
    parser.add_argument("-mappings-location",
                        dest="mappings_location",
                        help="filepath to the CSV spreadsheet to write the mappings",
                        type=Path,
                        default=Path(ROOT_DIR, "mappings", "input",
                            "enterprise", "csv"))
    return parser.parse_args()


def main():
    args = _parse_args()
    generate_supporting_csv(args.spreadsheet_location)
    sheets = get_sheets(args.spreadsheet_location)
    generate_csv_spreadsheet(sheets, args.mappings_location)


if __name__ == '__main__':
    main()

