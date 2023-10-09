Mapping Methodology
===================
The Sensor Mapping to ATT&CK project links event values in sensors and log files to ATT&CK Enterprise Data Sources. The resultant mappings can be used to either take a sensor event value and determine associated ATT&CK Data Sources, or to take an ATT&CK Data Sources and compose a list of associated sensor events. This methodology describes the scope of this project and the process used to take events native to the sensor and map to ATT&CK Data Sources. This aims to provide the community a reusable method of using ATT&CK to determine the capabilities of a platform's security offerings.

Scope
-----

Scoping for this project is focused on mappings for the following security logs, sensors, and capabilities:

- Windows Security Events
- Sysmon
- Auditd
- CloudTrail
- OSQuery
- ZEEK

Mapping Philosophy and Process
------------------------------
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
 

Step 1:  Identify the Sensor's Events
-------------------------------------

Sensors generate logs of real-time data that is indicative of a sequence of actions conducted by the user of a computer system. With those actions having a potential to inform a defender of adversary activity, this is the first location to look for further evidence. Typically, Sensors can be broken out into 2 categories: 

**Host:** data gathered from endpoints in the environment (e.g., Windows, MacOS, Linux)
   
   - Examples: 
      - Windows Event Logs
      - Sysmon
      - OSQuery
      - EDR Products (Carbon Black, Crowdstrike, Microsoft Defender ATP, etc.)
      - Services, Processes, Command-lines, Loaded Modules, DLLs
      - Files, Registry
      - Scheduled Tasks, Cron Jobs, Launch Agents
      - User Account, Hardware Info
      - Memory Data 

**Network:** data gathered from network communications, typically outbound connections

   - Examples: 
      - Firewall Logs
      - Proxy Logs
      - IDS/IPS Logs
      - Netflow Data 
      - Bro/Zeek
      - Packet Capture


These tools have documentation on the security capabilities of each platform (e.g., security reference architectures, security benchmarks, security documentation of various services) and should be reviewed to identify event IDs offered by the platform for detecting workloads on the platform. 

One widely used Windows centric sensor is the Windows Event Logs. The Windows Event Log is an in-depth record of events related to the system, security, and application stored on a Windows operating system. These event logs can be used to track system and some application issues and forecase future problems. Defenders will utilize this tool to help track potential threats and problems potentially attacking your organization. The events store information in a standard format that allows for a clear understanding of the information it is trying to portray (i.e. Log name, Event ID, Source, User, Computer, Event Data/Time, etc.) This project mainly focused on the security event logs for data related to the safety of a computer system. For example, failed and valid logins, file deletions, etc. 

In order for us to find a cohesive list of event ids per sensor, we looked towards some of these locations: 

- `Windows Event Logs from Microsoft <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-auditing-faq>`_
- `Ultimate Windows Security Encyclopedia <https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx>`_
- `Sysmon Event Logs <https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon>`_
- `OSQuery Schema <https://www.osquery.io/schema/5.9.1/>`_
- `Zeek Reference Documentation <https://docs.zeek.org/en/master/script-reference/proto-analyzers.html#>`_
- `CloudTrail Documentation <https://docs.aws.amazon.com/cloudtrail/>`_ 

Keep the following in mind while selecting event IDs:

- The scope of the events mapped by this project is telemetry that can be collected by a sensor or logging system that may be used to collect information relevant to identifying the action being performed, sequence of actions, or the results of those actions by an adversary. 
- The event IDs selected to be mapped as part of this project tend to be events that are marketed as native and made available on the platform. The intent is not to provide a mapping for all settings/features of individual platform services that are security related. This is a non-trivial undertaking that may be explored at a later time.


Step 2: Description Correlation
-------------------------------

What makes sensors useful to defenders is the meaning and context associated with the event. For each identified event ID, consult the available documentation to understand its capabilities. Gather specific facts about the event ID that will later help in mapping the event to the set of ATT&CK Data Sources it is able to detect. 

The most common way to bring context to the event is by applying the description and other types of metadata (Data Elements/Fields). When documented the description, elements, and fields can help us understand what the sensor is truly capturing, and make creating detections more efficient.


Identify the Source of Data 
***************************

Start with **identifying the source of data**. In a Windows environment, we can collect information pertaining to "Processes" from built-in event providers such as Microsoft-Windows-Security-Auditing and open third-party tools, including Sysmon. 

Let's take a look at Windows `Event ID 4688 <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688>`_. Because this is a Microsoft tool, we can go straight to their website to get addition context on what this event does. By the event description, 4688 is generated every time a new process starts. We can also see within the information provided by this event the user account that requested the creation of the process, and information of a process that executed a new process. This event also provides metadata that can help us to describe the data elements needed in Step 3 later on in the methodology process. For instance, regarding the user account data element, we have information of its logon id and the domain it belongs to. 

.. image:: _static/WELEX2.png
   :width: 600


.. image:: _static/WSE.png
   :width: 600

Think about the questions below for additional context on potential source of the data. 

- *why were these security events generated in my environment? (Activity)*
- *what operating system supports its generation? (Platform)*

Example: Let's use security event 4688: A new process has been created provided by Microsoft Windows security auditing as a basic example to understand this step of the methodology. 

- The action that triggered the generation of this event was the creation of a new process (Activity). 
- This security event can be collected by using the built-in event logging application for devices that work with the Windows operating system (Platform). Within a Windows environment, it is typically known to have a "process" as a source of data that. 


Lets look at Sysmon EID 1, Sysmon EID 8, WinEvtx 4688, and WinEvtx 4696. The image below shows that the definition all have some correlation with either starting or executing a process. 

.. image:: _static/DEF3.png
   :width: 700

This step also takes into account the overall event where a process can be represented as the main data element around an adversary action. This could include actions such as a process connected to an IP address, modifying a registry, or creating a file.

Step 3: Relationship Correlation
--------------------------------

Identify the Data Element
*************************

Next in reviewing the event ID, **identify the data element**. Once we identify and understand more about sources of data that can be mapped to an ATT&CK data source, we can start identifying data elements within the event fields that could help us eventually represent adversary behavior from a data perspective. 

The use of Data Elements help to name ATT&CK Data Sources related to the adversary behavior. For example, if an adversary modifies a Windows Registry value, collection of Windows Registry telemetry is needed. **How the adversary modified the registry, such as the process or user that performed the action, is how we pinpoint the data elements.** Below continuing on with our process example. As we think about how an adversary can create a process we are left with process, user, command, and thread. 

.. image:: _static/DE3.png
   :width: 700

Identifying the main data object to collect data from and/or all the data objects that define the context of the source of data is a method that can also be applied. This method can also be used to provide a general idea of what is needed to be collected. For example, data elements that provide metadata about network traffic can be grouped together and be associated with Netflow.

.. image:: _static/DE2.png
   :width: 600

The image below displays how we can extend the concept of an event log and capture the data elements featured within it. 

.. image:: _static/DE5.png
   :width: 600


There is a fundamental rule that should be considered when defining: **there is no one correct way to define data elements**. Please look to your organizational needs to help define what data elements means to you.

Identify Relationships among Data Elements
******************************************

By documenting the event collection, source (creation of a new process), and data elements (user account and process), we can start describing **interactions among elements through relationships**. Relationships in ATT&CK have been categorized between *activity* and *information*. Activity relationships are the ones that make references to the action that triggered the generation of the event. Informational relationships are the ones defined based on the metadata provided by the event. 

.. image:: _static/RDE1.png
   :width: 600

As the groupings grow, the similarities appear where different platforms or sensors tend to link to the same ATT&CK Data Source. 

.. image:: _static/RDE4.png
   :width: 600

As discussed by `OSSEM <https://github.com/OTRF/OSSEM>`_ at their ATT&CKcon 2018 and 2019 presentation. The activity of the relationship leads to Data Components. Data Components will help us to categorize relationships among data elements based on the security context they describe (i.e. Creation, Execution, Deletion). 

.. image:: _static/RDE5.png
   :width: 700   
