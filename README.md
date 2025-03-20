[![MITRE ATT&CK® 13.1](https://img.shields.io/badge/MITRE%20ATT%26CK®-v13-red)](https://attack.mitre.org/versions/v13/)

# Sensor Mappings to ATT&CK

Sensor Mappings to ATT&CK (SMAP) is a Center for Threat-Informed Defense (Center) project that
assists security operations teams and security leaders understand which tools, capabilities, and
events can help detect real-world adversary TTPs in their environments. SMAP builds on [MITRE ATT&CK®](https://attack.mitre.org/)
Data Sources by connecting the conceptual data source representions of information that can be collected
to concrete logs, sensors, and other security capabilities that provide that type of data. This work complements
the Center's [Security Stack Mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) project by allowing defenders to use both resources to understand their overall defensive coverage and make threat-informed decisions.


**Table Of Contents:**

- [Getting Started](#getting-started)
- [Getting Involved](#getting-involved)
- [Questions and Feedback](#questions-and-feedback)
- [How Do I Contribute?](#how-do-i-contribute)
- [Notice](#notice)

## Getting Started

To get started, read the project website. It provides an overview of the goals and
methodologies, defines all the key terms, and contains detailed examples.

| Resource                                                                                                                                                                               | Description                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| [Project Website](https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/)                                                                                     | Documentation, methodology, use cases, examples. |
| [Mappings Spreadsheet](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/blob/main/mappings/input/enterprise/xlsx/Sensor%20ID%20to%20Data%20Source.xlsx) | Complete list of Sensor Mappings.                |
| [Navigator Layers](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/tree/main/mappings/layers/enterprise)                                               | ATT&CK Navigator views of the Sensor Mappings.   |
| [STIX Bundles](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/tree/main/mappings/stix/enterprise)                                                     | Machine-readable list of Sensor Mappings.        |

The initial SMAP work was developed using ATT&CKv13.1. The mappings include some data 
components that are not represented in ATT&CKv13.1 and may not be represented in more 
recent versions of ATT&CK. The reason for this is that ATT&CK does not include data 
components that do not currently have a relationship to a (sub-)technique. These 
mapped data components are being tracked by the ATT&CK team and will be considered for 
incorporation in future versions of ATT&CK as the overall ATT&CK catalog evolves.

## Getting Involved

There are several ways that you can get involved with this project and help advance
threat-informed defense.

Please review the mappings, use them, and tell us what you think. We welcome your review
and feedback on the SMAP mappings, our methodology, and other resources.

We are interested developing additional tools and resources to help the community
understand and make threat-informed decisions in their risk management programs. Share
your ideas and we will consider them as we explore additional research projects.

## Questions and Feedback

Please submit
[issues](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/issues)
for any technical questions/concerns or contact
[ctid@mitre.org](mailto:ctid@mitre.org?subject=subject=Question%20about%20sensor-mappings-to-attack)
directly for more general inquiries.

## How Do I Contribute?

We welcome your feedback and contributions to help advance the Summiting project! Please
see the [guidance for contributors](/CONTRIBUTING.md).

## Notice

Copyright 2023 MITRE. Approved for public release. Document number CT0089.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied. See the License for the specific language governing
permissions and limitations under the License.

This project makes use of MITRE ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)
