# Stix Scripts and Data
This folder contains mappings of sensor data to STIX along with the parsing tool

| File                                   | Description                                                                                                       |
| :------------------------------------- | :---------------------------------------------------------------------------------------------------------------- |
| [generate_stix.py](#generate_stix)     | Script to build the raw STIX data from the input spreadsheets. Generates a file for each sensor source            |

## parse.py
### Description
Script to build the raw STIX data from the input spreadsheets to generate STIX data. Exports STIX relationship objects and utilizes the CustomObject decorator in STIX2 for the creation of new Data Source, Data Component and Sensor Mapping STIX objects. The script pulls the specified ATT&CK domain data down in STIX format, using the specified ATT&CK version from the given config_location. A file for referencing all created STIX objects is created in output_folder to avoid overwriting STIX IDs when regenerating outputs.

### Use
| Argument            | Description                                                                          | Default Value                                                                             |
| :------------------ | :----------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| attack_domain       | attack domain we are mapping. i.e. 'enterprise-attack', 'mobile-attack', 'ics-attack'| enterprise-attack                                                                         |
| config_location     | filepath to the configuration file for the framework                                 | `../../mappings/input/config.json`                                                        |
| mappings_location   | filepath to the CSV spreadsheets to write the mappings                               | `../../mappings/input/enterprise/csv`                                                     |
| output_folder       | folder where STIX bundle files will be saved.                                        | `../../mappings/stix/enterprise`                                                          |
| groups              | flag for making mappings to group objects                                            | N/A                                                                                       |


Generate STIX data from Enterprise ATT&CK
```
python generate_stix.py -attack_domain enterprise-attack
```