Mapping Methodology
===================
..
   Incorporate Methodology notes from Confluence

The Sensor Mapping to ATT&CK project links event values in sensors and log files to ATT&CK Enterprise Data Sources. The resultant mappings can be used to either take a sensor event value and determine associated ATT&CK techniques and sub-techniques, or to take an ATT&CK technique or sub-techniques and compose a list of associated sensor events. This methodology describes the scope of this project and the process used to map events native to a technology platform to ATT&CK Data Sources, and aims to provide the community a reusable method of using ATT&CK to determine the capabilities of a platform's security offerings.

MITRE ATT&CK® is a globally-accessible knowledge base of adversary
tactics and techniques based on real-world observations. ATT&CK focuses
on how external adversaries compromise and operate within computer
information networks. ATT&CK describes adversary behaviors using the following core
components:

-  **Tactics:** "why" - the adversary's objective or reason for
   performing an action

-  **Techniques:** "how" - the means by which adversaries achieve
   tactical goals

-  **Sub-techniques:** describing more specific means by which
   adversaries achieve tactical goals at a lower level than techniques

Adversary behaviors can be described by mapping them to the appropriate tactics, techniques, and sub-techniques in ATT&CK. To detect these behaviors, ATT&CK has a detection section that maps directly to the collection source (data sources). ATT&CK Data Sources represent information collected by a sensor or logging system that may be used to collect information relevant to identifying the action being performed, sequence of actions, or the results of those actions by an adversary.

..
   Definitions of sensors, native, etc.

Scope
-----

Scoping for this project is focused on mappings for the following security logs, sensors, and capabilities:

- Windows Security Events
- Sysmon
- Auditd
- CloudTrail
- OSQuery
- ZEEK

..
   Expand this section. Consider explaining event scope here as well (from step 1 below).

Mapping Philosophy and Process
------------------------------
..
   Develop graphic for this section.

Mappings are created by analyzing each in-scope event log/sensor in relation to ATT&CK Data Sources. Sensors/log files and ATT&CK are at different levels of abstraction and cannot always perfectly detect the adversary behaviors that they are meant to represent. Some amount of analyst judgement is required and, whenever judgement is involved, there can be differences in opinion. These design decisions document our judgement and rationale.

The methodology consists of the following steps:

- **Identify Platform Event Logs** - Identify the *native* event logs available on the platform.
- **Event ID Review** - For each identified event, understand the security capabilities it provides.
- **Identify Mappable ATT&CK Data Sources** - Identify the ATT&CK Data Sources mappable to event IDs.
- **Create a Mapping** - Creating a mapping based on the information gathered from the previous steps. 

Step 1:  Identify Platform Event Logs
-------------------------------------

Vendor documentation on the security capabilities of each platform (e.g., security reference architectures, security benchmarks, security documentation of various services) is reviewed to identify event IDs offered by the platform for detecting workloads on the platform. Keep the following in mind while selecting event IDs:

- The scope of the events mapped by this project is telemetry that can be collected by a sensor or logging system that may be used to collect information relevant to identifying the action being performed, sequence of actions, or the results of those actions by an adversary. 
- The selected events should be native to the platform, i.e., produced by the operating system themselves. For example, event IDs developed directly in a third-party tool are considered out of scope.
- The event IDs selected to be mapped as part of this project tend to be events that are marketed as native and made available on the platform. The intent is not to provide a mapping for all settings/features of individual platform services that are security related. This is a non-trivial undertaking that may be explored at a later time.

Step 2:  Event ID Review
------------------------

For each identified event ID, consult the available documentation to understand its capabilities. Gather specific facts about the event ID that will later help in mapping the event to the set of ATT&CK Data Sources it is able to detect. 

Step 3: Identify Mappable ATT&CK Data Sources 
---------------------------------------------

After understanding the capabilities of the event ID and gathering the basic facts about its operation, as identified in the previous step, review the ATT&CK matrix and identify the data source the event is able to detect. The following may help with this process: 

- Identify ATT&CK Data Sources in Scope
   - The resource type(s) detected by the event, as identified in the previous step, can help narrow down the ATT&CK Data Sources to consider for the mapping.

Step 4:  Create A Mapping
-------------------------
The previous steps enabled you to gather the information required to create a mapping file for an event. As pulled from the original `ATT&CK's Data Source Methodology <https://github.com/mitre-attack/attack-datasources/blob/main/docs/methodology.md>`_ the below is what we are looking for when reviewing events:
- Identifying Sources of Data:
   - Why were these security events generated in my environment?
   - What operating system supports its generation?
   - Where were they collected? 
- Identifying Data Elements
   - Data Elements help us not only to represent (elements) and describe (attributes) relevant network security concepts, but also to get a better understanding of the interactions (relationships) among them. 
- Identifying Relationships Among Data Elements 
   - By documenting telemetry collected within a network environment we were able to identify the activity that triggered the generation of security telemetry and data elements that were involved in an action
- Identifying Telemetry Source (ETW/Kernal Callbacks/APIs/etc.)
