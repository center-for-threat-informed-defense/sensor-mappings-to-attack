# Utility Scripts
Contains scripts used to create auxiliary data for mappings

| Script                                   | Purpose                                                                                                                                                                                                       |
| :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_mappings.py](#create_mappingspy) | From the master excel spreadsheet, generate CSVs for sensor data mappings to be used with the parsing tool.                                  |
| [create_heatmaps.py](#create_heatmapspy) | Enables visualization of the sensor mappings in the ATT&CK Matrix. Builds ATT&CK Navigator heatmap layers from mappings_location. These layers can also be found in the `layers` folder of the attack type in the stix output folder. |                                                                                                                                              |

## create_mappings.py
### Description
From the master excel spreadsheet, separate data by sensor, standardize it and generate CSVs. These will be used to generate STIX data.
### Use
| Argument             | Description                                              | Default Value                                                                                  |
| :------------------- | :------------------------------------------------------- | :--------------------------------------------------------------------------------------------- |
| config_location      | filepath to the configuration for the framework          | `../../mappings/input/config.json`                                                             |
| spreadsheet_location | filepath to the Excel spreadsheet for the mappings       | `../../mappings/input/enterprise/xlsx/Sensor ID to Data Source to API v2.xlsx`                 |
| mappings_location    | filepath to the folder to write CSV spreadsheets         | `../../mappings/input/enterprise/csv`                                                          |

Use with default arguments
```
python create_mappings.py
```


## create_heatmaps.py
### Description
Enables visualization of the sensor mappings in the ATT&CK Matrix. The script builds ATT&CK Navigator heatmap layers from the mappings_location folder. These layers can also be found in the `layers` folder of the attack domain in the stix output folder.
### Use
| Argument          | Description                                                                                             | Default Value                                                                           |
| :--------------   | :------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------- |
| mappings_location | filepath to the STIX Bundle mappings folder                                                             | `../../mappings/stix/enterprise`                                                        |
| domain            | the domain of ATT&CK to visualize (options: enterprise-attack, ics-attack, mobile-attack)               | enterprise-attack                                                                       |
| output            | folder to write output layers to                                                                        | `../../mappings/stix/layers`                                                            |
| version           | which ATT&CK version to use                                                                             | 13.1                                                                                    |
| clear             | if flag is specified, will remove the contents of the output folder before writing layers               | N/A                                                                                     |
| map_subtechniques | if flag is specified, will map down to sub-techniques                                                   | N/A                                                                                     |


To build layers from project root:
```
$ python src/util/create_heatmaps.py -clear -domain enterprise-attack \
    -mappings_location mappings/stix/enterprise
```
