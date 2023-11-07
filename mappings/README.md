# Mappings
The mappings folder contains inputs and outputs related to the tool suite.


## Input
Contains files used as input for running tool suite.

### `attack-domain`
Inputs for creating mappings to different domains should be organized by the attack-domain.
e.g., to create mappings to the 'enterprise' attack domain, input files would be stored in `mappings/input/enterprise`

---

## STIX
Contains STIX bundle files output from running the `src/parse/generate_stix.py` file. Outputs will be stored in corresponding `attack-domain` folders.

---

## layers
Contains ATT&CK Navigator files output from running the `src/util/create_heatmaps.py` file.Outputs will be stored in corresponding `attack-domain` folders.

e.g., to create ATT&CK Navigator layers for the `enterprise` attack domain, use STIX bundle files stored in `mappings/stix/enterprise` to generate Navigator layers in the folder `mappings/layers/enterprise`