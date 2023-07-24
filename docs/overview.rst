Overview
========
Cyber threat detection starts with understanding the data sources and sensors that can be used to detect a given adversary TTP. 

Background
----------
Sensor Mappings to ATT&CK helps security operations centers (SOCs) and security leaders understand whether specific ATT&CK techniques can be detected given the sensors, logs, tools, and other security capabilities available to them or, if they can't, what they can do to change that. This information can be used to answer questions such as:
- What's my coverage for ATT&CK techniques given my current tools? 
- If I were to add Tool X, how does that coverage change?
- I'm concerned about a particular technique in a recent threat report. Can I see it if it were to happen in my environment and, if so, where do I look?

ATT&CK Data Sources do not describe fully the specific events or sensors that can provide visibility into each individiual data source. This leaves the users with significant work to understand how their tools map to the generic data sources and inhibits automated analysis to easily answer the questions SOCs need to ask. This project is intended to build on ATT&CK Data Sources, extending them to connect conceptual data sources to concrete sensors, logs, tools, and other security capabilities, allowing the users of ATT&CK to easily go from a technique they're concerned about to capabilities they might have or could acquire to detect it.

STIX Representation and Mapping Tools 
-------------------------------------
To make the mapping between sensors and ATT&CK easily accessible to defenders that use STIX, the mappings are also published in a machine-readable STIX 2 representation. This format uses STIX representation to represent the mappings between events and ATT&CK. 

A set of Python tools is provided to support data manipulation, including the creation of new mappings and the customization of existing mappings. A command line interface (CLI) tool is available for validation of mapping file syntax, ensuring conformity to the data format specification and accurate references of ATT&CK Data Sources. The CLI tool also supports the production of ATT&CK Navigator layers and Markdown Summary visualizations from mapping files. 

Users can easily refine and extend the mappings for their needs and locally rebuild the full set of supporting artifacts using the scripts in this repository. 

Get Involved
------------
The resulting mapping between Events and ATT&CK allow cyber defenders to create a fuller and more deteailed picture of cyber incidents, including the threat actor, technical bahvior, telemetry collection, and impact. These improvements can be used to develop better predictions and insights into how we might be attacked in the future by better understanding how and why were attacked in the past. 

We encourage you to review the mappings, use them, and tell us what you think. Please see the guidance for contributors if you are interested in `contributing <https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/blob/main/CONTRIBUTING.md>`_. You are also welcome to submit issues for any technical questions/concerns or contact `ctid@mitre-engenuity.org <mailto:ctid@mitre-engenuity.org>`_ directly for more general inquiries. 

Notice
------
© 2023 MITRE Engenuity. Approved for public release. Document number PRS_NUMBER.
This project makes use of ATT&CK®: `ATT&CK Terms of Use <https://attack.mitre.org/resources/terms-of-use/>`__
