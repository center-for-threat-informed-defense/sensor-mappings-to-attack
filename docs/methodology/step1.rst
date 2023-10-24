Step 1:  Identify the Sensor's Events
=====================================

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
