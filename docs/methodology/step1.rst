Step 1:  Identify the Sensor's Events
=====================================

Sensors generate logs of real-time data that is indicative of a sequence of actions conducted by the user of 
a computer system. With those actions having a potential to inform a defender of adversary activity, this is 
the first location to look for further evidence. Typically, sensors can be broken out into two categories: 

**Host:** data gathered from endpoints in the environment (e.g., Windows, MacOS, Linux)
   
   - Examples: 
      - Windows Event Log
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

One widely used Windows-centric sensor is Windows Event Log. The Windows Event Log is an in-depth record of events 
related to the system, security, and applications stored on a Windows operating system. These event logs can be 
used to track certain system and application issues and potentially forecast future problems. Defenders will utilize 
this tool to help track potential threats and problems potentially occurring within an organization's environment. 
The events store information in a standard format that allows for a clear understanding of the information collected 
(i.e., Log name, Event ID, Source, User, Computer, Event Data/Time, etc.) 

These sensors or tools have user documentation for the security capabilities of each platform (e.g., security 
reference architectures, security benchmarks, security documentation of various services) and should be reviewed 
to understand event types offered by the platform for detecting workloads on the platform. This project focused on 
security event logs for data related to the safety of a computer system, such as failed and valid logins and file 
deletions. This user documentation was reviewed to develop the Events and Event IDs to be mapped for each sensor, 
including: 

- `Windows Event Logs from Microsoft <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/advanced-security-auditing-faq>`_
- `Ultimate Windows Security Encyclopedia <https://www.ultimatewindowssecurity.com/securitylog/encyclopedia/default.aspx>`_
- `Sysmon Event Logs <https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon>`_
- `OSQuery Schema <https://www.osquery.io/schema/5.9.1/>`_
- `Zeek Reference Documentation <https://docs.zeek.org/en/master/script-reference/proto-analyzers.html#>`_
- `CloudTrail Documentation <https://docs.aws.amazon.com/cloudtrail/>`_ 
- `Auditd Linux man page <https://www.man7.org/linux/man-pages/man8/auditd.8.html>`_

When selecting events to map, the following considerations were used:

- The scope of the events consists of telemetry that can be collected by a sensor or logging system which may collect information relevant to identifying the action being performed by an adversary, sequence of actions, or the results of those actions.
- The events are considered as native to the sensor and made available on the platform. The intent is not to provide a mapping for all settings/features of individual platform services. This is a non-trivial undertaking that may be explored at a later time.
