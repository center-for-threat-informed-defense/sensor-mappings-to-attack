# Mapping Methodology

This document describes the methodology used to map event IDs native to a technology platform to ATT&CK Data Sources; and aims to provide the community a reusable method of using ATT&CK to determine the capabilities of a platform's security offerings.

ATT&CK is a globally-accessible knowledge base of adversary tactics and techniques based on real-world observations. The ATT&CK knowledge base represents adversary goals as tactics and the specific behaviors employed by adversaries to achieve those goals (how) as techniques and sub-techniques. The methodology described below, utilizes the information in the ATT&CK knowledge base and its underlying data model to understand, assess and record the real-world threats that security controls native to a technology platform are able to mitigate.

The methodology consists of the following steps:
1. **Identify Platform Event Logs** - Identify the *native* event logs available on the platform.
1. **Event ID Review** - For each identified event, understand the security capabilities it provides.
1. **Identify Mappable ATT&CK Data Sources** - Identify the ATT&CK Data Sources mappable to event IDs.
1. **Create a Mapping** - Creating a mapping based on the information gathered from the previous steps. 

## Step 1:  Identify Platform Event Logs
Cyber security has emerged as an essential component of technology platforms, and consequently vendors tend to offer a variety of documentation on the security capabilities of their platform. Peruse the platform documentation (e.g. security reference architectures, security benchmarks, security documentation of various services, etc.) to identify event IDs offered by a platform for detecting workloads on the platform. Keep the following in mind while selecting event IDs:
- The scope of the events mapped by this project is telemetry that can be collected by a sensor or logging system that may be used to collect information relevant to identifying the action being performed, sequence of actions, or the results of those actions by an adversary. 
- The selected events should be native to the platform, i.e. produced by the operating system themselves. For example, event IDs developed directly in a third-party tool are considered out of scope.
- The event IDs selected to be mapped as part of this project tend to be events that are marketed as native and made available on the platform. The intent is not to provide a mapping for all settings/features of individual platform services that are security related. This is a non-trivial undertaking that may be explored at a later time.

## Step 2:  Event ID Review
For each identified event ID, consult the available documentation to understand its capabilities. Gather the following facts about the event ID that will later help in mapping the event to the set of ATT&CK Data Sources it is able to detect. 

## Step 3: Identify Mappable ATT&CK Data Sources 
After understanding the capabilities of the event ID and gathering the basic facts about its operation, as identified in the previous step, review the ATT&CK matrix and idenitfy the data source the event is able to detect. The following may help with this process: 

#### Identify ATT&CK Data Sources in Scope
- The resource type(s) detected by the event, as identified in the previous step, can help narrow down the ATT&CK 

## Step 4:  Create A Mapping
The previous steps enabled you to gather the information required to create a mapping file for an event. As pulled from the original [ATT&CK's Data Source Methodology](https://github.com/mitre-attack/attack-datasources/blob/main/docs/methodology.md) the below is what we are looking for when reviewing events:
- Identifying Sources of Data:
  - Why were these security events generated in my environment?
  - What operating system supports its generation?
  - Where were they collected? 
- Identifying Data Elements
  - Data Elements help us not only to represent (elements) and describe (attributes) relevant network security concepts, but also to get a better understanding of the interactions (relationships) among them. 
- Identifying Relationships Among Data Elements 
  - By documenting telemetry collected within a network environment we were able to identify the activity that triggered the generation of security telemetry and data elements that were involved in an action
- Identifying Telemetry Source (ETW/Kernal Callbacks/APIs/etc.)
