Step 2: Definition Correlation
===============================

What makes sensors useful to defenders is the meaning and context associated with the event. For each identified event ID, consult the available documentation to understand its capabilities. Gather specific facts about the event ID that will later help in mapping the event to the set of ATT&CK Data Sources it is able to detect. 

The most common way to bring context to the event is by applying the description and other types of metadata (Data Elements/Fields). When documented the description, elements, and fields can help us understand what the sensor is truly capturing, and make creating detections more efficient.

Identify the Source of Data 
---------------------------

Start with **identifying the source of data**. In a Windows environment, we can collect information pertaining to "Processes" from built-in event providers such as Microsoft-Windows-Security-Auditing and open third-party tools, including Sysmon. 

Think about the questions below for additional context on potential source of the data. 

- *why were these security events generated in my environment? (Activity)*
- *what operating system supports its generation? (Platform)*

Let's take a look at Windows `Event ID 4688 <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688>`_. Because this is a Microsoft tool, we can go straight to their website to get addition context on what this event does. By the event description, 4688 is generated every time a new process starts. We can also see within the information provided by this event the user account that requested the creation of the process, and information of a process that executed a new process. This event also provides metadata that can help us to describe the data elements needed in Step 3 later on in the methodology process.

.. image:: ../_static/MSDN_4688_Ex.png
   :width: 600

- The action that triggered the generation of this event was the creation of a new process (Activity). 
- This security event can be collected by using the built-in event logging application for devices that work with the Windows operating system (Platform). Within a Windows environment, it is typically known to have a "process" as a source of data that. 

Correlate to ATT&CK Data Component Defintion
--------------------------------------------
In correlation to ATT&CK, when you go to the `Data Source <https://attack.mitre.org/datasources/>`_ pages you can see definitions for a given one. 

.. image:: ../_static/ATTACK_Ex_PC.png
   :width: 600

ATT&CK's definition of process creation is : **..the initial construction of an executable..** through keyword analysis, this turns out to be the same as **..a process is created..** Therefore we can comfortably link event ID 4688 with ATT&CK Data Component. 

Lets look at Sysmon EID 1, Sysmon EID 8, WinEvtx 4688, and WinEvtx 4696. The image below shows that the definition all have some correlation with either starting or executing a process. 

.. image:: ../_static/DefinitionCorrelation_Ex.png
   :width: 700