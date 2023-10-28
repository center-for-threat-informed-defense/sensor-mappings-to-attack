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

## Customization

To create customized mappings, edit the input data in the [`inputs/`](../mappings/input) directory and then use the tools above to regenerate the outputs.
