Overview
========

Cyber threat detection starts with understanding the data sources and sensors that can
be used to detect a given adversary tactic, technique, or procedure (TTP).

The Sensor Mappings to ATT&CK Project (SMAP) extends MITRE ATT&CK® Data Sources to map
out how sensors and tools provide visibility into specific adversary TTPs. This helps
cyber defenders understand whether their sensors and other security capabilities provide
visibility into the adversary behaviors they care most about. And if they cannot provide
visibility, then what should defenders do to change that? This information can be used
to answer questions such as:

- What is my coverage for ATT&CK TTPs given my current tools?
- If I were to add Tool X, how does that coverage change?
- If I'm concerned about a recent threat report, how can I look for that threat in my
  environment?

Background
----------

ATT&CK began bridging offensive actions with defensive countermeasures `in
version 9.0 <https://medium.com/mitre-attack/attack-april-2021-release-39accaf23c81>`__.
This goal was achieved by tagging each (sub-)technique with defensive-focused fields,
such as what data to collect (Data Sources) and how to analyze that data in order to
identify specific behaviors (Detections).

`ATT&CK's Data Sources <http://attack.mitre.org/datasources/>`_ usually fall into one of
the following buckets:

- Granular basic system artifacts (e.g., process, file, registry)
- Granular basic user activities (e.g., logon session)
- Abstract types of system artifacts, with children as sub-types (e.g., scheduled jobs)
- Associated network traffic (e.g., wmi and registry), in such cases, it's important to
  capture the set of protocols that encompasses this traffic, so that users may
  understand where they need to look in their logs/PCAPs/DPI appliances/etc.
- Associated cloud (e.g. Instance, Container, Cloud Storage, Cloud Service)

ATT&CK Data Sources do not fully describe the specific events or sensors that provide
visibility. This leaves the users with significant work to understand how their tools
map to ATT&CK Data Sources and hinders automated reasoning. This project is intended to
build on ATT&CK Data Sources, extending them to connect *conceptual* data sources to
*concrete* sensors, logs, tools, and other security capabilities. This mapping allows
the users of ATT&CK to go from a technique they're concerned about to capabilities they
might have or could acquire to detect it.

Prior research into building on ATT&CK Data Objects has been undertaken by `The Open
Source Security Events Metadata (OSSEM) <https://github.com/OTRF/OSSEM>`__ project and
the Center's `Atomic Data Sources project
<https://github.com/mitre-attack/attack-datasources>`__. OSSEM is a community-led
project created by Roberto and Jose Rodriguez that provides security context telemetry
of behaviors occurring in an environment and metadata describing relationships between
security events and ATT&CK TTPs. Atomic Data Sources developed data source objects and
context to help describe activity within a network and provided a proof-of-concept
approach to mapping ATT&CK Data Sources to sensors.

STIX Representation and Mapping Tools
-------------------------------------

To make the mapping between sensor events and ATT&CK easily accessible to defenders that
use STIX, the mappings are also published in a machine-readable STIX 2 representation. A
set of Python tools is provided to support data manipulation, including the creation of
new mappings and the customization of existing mappings. A command line interface (CLI)
tool is available for validation of mapping file syntax, ensuring conformity to the data
format specification and accurate references of ATT&CK Data Sources. The CLI tool also
supports the production of ATT&CK Navigator layers and Markdown Summary visualizations
from mapping files. Users can refine and extend the mappings for their needs and build a
local copy of the SMAP artifacts using the scripts in this repository.

Get Involved
------------

The mapping between ATT&CK Data Sources and concrete sensors allows cyber defenders to
create a more detailed picture of cyber incidents, including the threat actor, technical
behavior, telemetry collection, and impact. These improvements can be used to develop
better predictions and insights into how we might be attacked in the future by better
understanding of how and why were attacked in the past.

We encourage you to review the mappings, use them, and tell us what you think. Please
see the guidance for contributors if you are interested in `contributing
<https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/blob/main/CONTRIBUTING.md>`_.
You are also welcome to submit issues for any technical questions/concerns or contact
`ctid@mitre-engenuity.org <mailto:ctid@mitre-engenuity.org>`_ directly for more general
inquiries.
