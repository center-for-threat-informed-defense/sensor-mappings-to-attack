.. _Methodology Pages:

=========================
Mapping Methodology
=========================

Philosophy
----------

Mappings are created by analyzing each in-scope sensor in relation to ATT&CK Data Sources. Events collected 
by sensors and ATT&CK objects are at different levels of abstraction and cannot always perfectly detect 
the adversary behaviors that they are meant to represent. By completing the connection of conceptual data 
sources and components to concrete logs, sensors, and other security capabilities, cyber defenders have a
information to help identify relevant security data to collect for specific behaviors and environments.

Process
-------

The Sensor Mappings to ATT&CK mapping methodology consists of the following steps:

- **Identify the Sensor's Events/Telemetry** - Identify the event logs available to the sensor.
- **Definition Correlation** - For each identified event, understand the security capabilities it provides.
- **Relationship Correlation** - Identify the ATT&CK Data Sources mappable to event IDs.

<img src="./docs/_static/methodology.png" width="900px">

.. toctree::

    step1
    step2
    step3

    
