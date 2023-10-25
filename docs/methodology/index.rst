.. _Methodology Pages: 

=========================
Mapping Methodology
=========================

Philosophy
----------
..
   Develop graphic for this section.

Mappings are created by analyzing each in-scope sensor in relation to ATT&CK Data Sources. Sensor's triggered events and ATT&CK are at different levels of abstraction and cannot always perfectly detect the adversary behaviors that they are meant to represent. Some amount of analyst judgement is required and, whenever judgement is involved, there can be differences in opinion. These design decisions document our judgement and rationale.

The methodology consists of the following steps:

- **Identify the Sensor's Events/Telemetry** - Identify the *native* event logs available to the sensor.
- **Definition Correlation** - For each identified event, understand the security capabilities it provides.
- **Relationship Correlation** - Identify the ATT&CK Data Sources mappable to event IDs.

An important goal of ATT&CK was to bridge offensive actions with potential defensive countermeasures starting in the v9 release. They achieved this by tagging each (sub-)technique with defensive-focused fields/properties, such as what data to collect (data sources) and how to analyze that data in order to potentially identify specific behaviors (detections). 

`ATT&CK's Data Sources <http://attack.mitre.org/datasources/>`_ usually fall into one of the following buckets: 

- Granular basic system artifacts (e.g., process, file, registry)
- Granular basic user activities (e.g., logon session)
- Abstract types of system artifacts, with children as sub-types (e.g., scheduled jobs)
- Associated network traffic (e.g., wmi and registry), in such cases, it's important to capture the set of protocols that encompasses this traffic, so that users may understand where they need to look in their logs/PCAPs/DPI appliances/etc.
- Associated cloud (e.g. Instance, Container, Cloud Storage, Cloud Service)

Process
-------
.. toctree::
	:maxdepth: 1

    step1
    step2
    step3