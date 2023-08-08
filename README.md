# Sensor Mappings to ATT&CK

Sensor Mappings to ATT&CK (SMTA) is a Center for Threat-Informed Defense (Center) project that
assists security operations teams and security leaders understand which tools, capabilities, and
events can help detect real-world adversary TTPs in their environments. SMTA builds on [MITRE ATT&CK®](https://attack.mitre.org/)
Data Sources by connecting the conceptual data source representions of information that can be collected 
to concrete logs, sensors, and other security capabilities that provide that type of data. This work complements
the Center's [Security Stack Mappings](https://github.com/center-for-threat-informed-defense/security-stack-mappings) project by allowing defenders to use both resources to understand their overall defensive coverage and make threat-informed decisions.  

<img src="./docs/_static/wmi-example.png" width="900px">

**Table Of Contents:**

- [Getting Started](#getting-started)
- [Getting Involved](#getting-involved)
- [Questions and Feedback](#questions-and-feedback)
- [Notice](#notice)

## Getting Started

<!-- TODO Write one paragraph about how users should get started,
     and update the table of resources below. -->

This scope of this project includes mappings to ATT&CK Data Sources from:
- Sysmon (all events) 
- Windows Event Log (security-relevant events) 
- Auditd 
- CloudTrail 
- OSQuery
- ZEEK

The mapping structure, methodology, and scenarios are fully described in [the project website](https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/).

| Resource                     | Description                                    |
| ---------------------------- | ---------------------------------------------- |
| [Project Website](#)         | Documentation, methodology, and use cases.     |
| [Mappings](#)                | In-scope sensors mapped to ATT&CK.             |
| [ATT&CK Navigator Layers](#) | ATT&CK Navigator layers for the SMTA mappings. |

## Getting Involved

There are several ways that you can get involved with this project and help advance
threat-informed defense.

Please review the mappings, use them, and tell us what you think. We welcome your review
and feedback on the SMTA mappings, our methodology, and other resources.

We are interested developing additional tools and resources to help the community
understand and make threat-informed decisions in their risk management programs. Share
your ideas and we will consider them as we explore additional research projects.

## Questions and Feedback

Please submit [issues](https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/issues) for any technical questions/concerns
or contact [ctid@mitre-engenuity.org](mailto:ctid@mitre-engenuity.org?subject=subject=Question%20about%20sensor-mappings-to-attack) directly for more general inquiries.

We welcome your feedback and contributions to help advance SMTA. Please see the guidance for 
contributors if are you interested in [contributing or simply reporting issues.](/CONTRIBUTING.md)

## Notice

<!-- TODO Add PRS prior to publication. -->

Copyright 2023 MITRE Engenuity. Approved for public release. Document number REPLACE_WITH_PRS_NUMBER

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this
file except in compliance with the License. You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under
the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied. See the License for the specific language governing
permissions and limitations under the License.

This project makes use of MITRE ATT&CK®

[ATT&CK Terms of Use](https://attack.mitre.org/resources/terms-of-use/)
