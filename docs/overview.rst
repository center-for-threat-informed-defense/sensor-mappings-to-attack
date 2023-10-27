Overview
========
Cyber threat detection starts with understanding the data sources and sensors that can be used to detect a given adversary behavior. Sensor Mappings to ATT&CK (SMAP) helps cybersecurity defenders understand whether specific ATT&CK techniques can be detected in their environment given the sensors, logs, tools, and other security capabilities available to them or, if they can't, what they can do to change that. This information can be used to answer questions such as:
- What's my coverage for ATT&CK techniques given my current tools? 
- If I were to add Tool X, how does that coverage change?
- I'm concerned about a particular technique in a recent threat report. Can I see it if it were to happen in my environment and, if so, where do I look?

Background
----------
ATT&CK Data Sources do not describe fully the specific events or sensors that can provide visibility into each individiual data source. This leaves the users with significant work to understand how their tools map to the generic data sources and inhibits automated analysis to easily answer the questions cyber defenders need to ask. SMAP builds on ATT&CK Data Sources, extending them to connect the conceptual data sources to specific security events captured by concrete sensors, logs, tools, and other security capabilities. This allows the users of ATT&CK to more easily go from adversary techniques they're concerned about to capabilities they might have or could acquire to detect them.

STIX Representation and Mapping Tools 
-------------------------------------
To make the mapping between sensor events and ATT&CK easily accessible to cyber defenders that use STIX, the mappings are also published in a machine-readable STIX 2 representation. This format uses STIX Relationships to represent the mappings between sensor events and ATT&CK. 

A set of Python tools is provided to support data manipulation, including the creation of new mappings and the customization of existing mappings. A command line interface (CLI) tool is available for validation of mapping file syntax, ensuring conformity to the data format specification, and accurate references of ATT&CK Data Sources. The CLI tool also supports the production of ATT&CK Navigator layers and Markdown Summary visualizations from mapping files. 

Users can easily refine and extend the mappings for their needs and locally rebuild the full set of supporting artifacts using the scripts in this repository. Note: If you are simply ingesting the data from this repository, you will not need to install or run any of the provided scripts.

Get Involved
------------
We encourage you to review the mappings, use them, and tell us what you think. Please see the guidance for contributors if you are interested in `contributing <https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/blob/main/CONTRIBUTING.md>`_. You are also welcome to submit issues for any technical questions/concerns or contact `ctid@mitre-engenuity.org <mailto:ctid@mitre-engenuity.org>`_ directly for more general inquiries. 

Notice
------
<!-- TODO Add PRS prior to publication. -->

© 2023 MITRE Engenuity. Approved for public release. Document number PRS_NUMBER.
This project makes use of ATT&CK®: `ATT&CK Terms of Use <https://attack.mitre.org/resources/terms-of-use/>`__
