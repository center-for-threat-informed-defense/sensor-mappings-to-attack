# Tools for Sensor Mappings to MITRE ATT&CK®

This directory contains a Python package of tools for working with data generated from sensors mappings to ATT&CK.

## Set up

You will need the following prerequisites to run the tools:

1. [Python (≥3.10)](https://www.python.org/downloads/)
2. [Python Poetry](https://python-poetry.org/docs/#installation)

Once you have the repository cloned, run the following one-time command to initialize a virtual environment and install dependencies:

```
poetry install
```

Once the dependencies are installed, you will need to activate the [virtual environment](https://python-poetry.org/docs/basic-usage/#activating-the-virtual-environment) in each terminal window prior to using the Python tools.

```
poetry shell
```

## Tools

The tools are organized into the following subdirectories. Click the link to view detailed instructions for working with those tools.

| Directory                     | Description                                                                         |
| ----------------------------- | ----------------------------------------------------------------------------------- |
| [`parse/`](./parse)           | Script for parsing sensor data and mappings spreadsheets.                           |
| [`util/`](./util)             | Utility scripts to process mappings data, such as Navigator layers, CSV files, etc. |

## Creating mappings
To use the tool suite, execution the files in the following order:
1. Create the auxilary files by running `util/create_mappings.py`
2. Create mappings by running `parse/generate_stix.py`
3. (Optional) Validate bundles by running `util/cli_validator.py`
4. Create ATT&CK Navigation layers by running `util/create_heatmaps.py`


## Customization

To create customized mappings, edit the input data in the [`inputs/`](../mappings/input) directory and then use the tools above to regenerate the outputs.
