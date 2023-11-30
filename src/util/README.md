# Utility Scripts
Contains scripts used to create auxiliary data for mappings and validating mappings.

| Script                                   | Purpose                                                                                                                                                                                                                               |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_mappings.py](#create_mappingspy) | From the master excel spreadsheet, generate CSVs for sensor data mappings to be used with the parsing tool.                                                                                                                           |
| [create_heatmaps.py](#create_heatmapspy) | Enables visualization of the sensor mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers from mappings_location. These layers can also be found in the `layers` folder of the attack type in the stix output folder. |
| [stix_schemas.py](#stix_schemaspy)       | Schema definition file.                                                                                                                                                                                                               |
| [cli_validator.py](#cli_validatorpy)     | Validates mappings to ensure bundles are packaged properly with all necessary objects                                                                                                                                                 |
| [generate_docs.py](#generate_docspy)     | Create mapping tables in Sphinx pages from CSV files generated from (#create_mappingspy)                                                                                                                                              |

## create_mappings.py
### Description
From the master excel spreadsheet, separate data by sensor, standardize it and generate CSVs. These will be used to generate STIX data.
### Use
| Argument             | Description                                              | Default Value                                                                   |
| :------------------- | :------------------------------------------------------- | :------------------------------------------------------------------------------ |
| config_location      | filepath to the configuration for the framework          | `../../mappings/input/config.json`                                              |
| spreadsheet_location | filepath to the Excel spreadsheet for the mappings       | `../../mappings/input/enterprise/xlsx/Sensor ID to Data Source to API v2.xlsx`  |
| mappings_location    | filepath to the folder to write CSV spreadsheets         | `../../mappings/input/enterprise/csv`                                           |

Use with default arguments
```
python create_mappings.py
```


## create_heatmaps.py
### Description
Enables visualization of the sensor mappings in the ATT&CK Matrix. The script builds ATT&CK Navigator heatmap layers from the mappings_location folder. These layers can also be found in the `layers` folder of the attack domain in the stix output folder.
### Use
| Argument          | Description                                                                                             | Default Value                     |
| :--------------   | :------------------------------------------------------------------------------------------------------ | :-------------------------------- |
| mappings_location | filepath to the STIX Bundle mappings folder                                                             | `../../mappings/stix/enterprise`  |
| domain            | the domain of ATT&CK to visualize (options: enterprise-attack, ics-attack, mobile-attack)               | enterprise-attack                 |
| output            | folder to write output layers to                                                                        | `../../mappings/stix/layers`      |
| version           | which ATT&CK version to use                                                                             | 13.1                              |
| clear             | if flag is specified, will remove the contents of the output folder before writing layers               | N/A                               |
| map_subtechniques | if flag is specified, will map down to sub-techniques                                                   | N/A                               |


To build layers from project root:
```
$ python src/util/create_heatmaps.py -clear -domain enterprise-attack \
    -mappings_location mappings/stix/enterprise
```

## stix_schemas.py
### Description
Defines schemas for the cli_validator tool using the [schema library](https://github.com/keleshev/schema).


## cli_validator.py
### Description
The mapping CLI tool provides functionality to validate STIX bundles generated by `parse/generate_stix.py` script. Validity is defined as:
- Containing valid timestamps that follow the format in STIX
- Follows its object schema in `stix_schemas.py`
- "Bundle completeness" to ensure there aren't any missing objects
    - Check if a sensor mapping entry references a newly created Data Source
        - Make sure the STIX entry for this newly created Data Source is present in the bundle
    - Check if a sensor mapping entry references a newly created Data Component
        - If the Data Component is not present in the bundle, check in the ATT&CK dataset
    - Check that the SRO between these two STIX objects
        - If it is not present in the bundle, check if it has already been defined in the ATT&CK dataset

### Use
| Argument             | Description                                                                           | Default Value                            |
| :------------------- | :------------------------------------------------------------------------------------ | :--------------------------------------- |
| attack_domain        | attack domain of the mappings (options: enterprise-attack, ics-attack, mobile-attack) | enterprise-attack                        |
| config_location      | filepath to the configuration for the framework                                       | `../../mappings/input/config.json`       |
| mappings_location    | filepath to folder of STIX bundle mappings                                            | `../../mappings/input/enterprise/csv`    |
| groups               | flag for if mappings to group objects                                                 | N/A                                      |


## generate_docs.py
### Description
A script to update website mapping tables from the CSVs generated by (#create_mappingspy)

### Use
| Argument             | Description                               | Default Value            |
| :------------------- | :---------------------------------------- | :----------------------- |
| docs_location        | filepath to documentation files to edit   | `../../docs/levels/`     |
| mappings_location    | filepath to mapping files directory       | `../../mappings/input/`  |
