Future Work 
===========

Sensor Mappings to ATT&CK project is planning to look at other areas of research: 

- Event ID mappings to ATT&CK Techniques 
- Event ID mappings to Vendor Sensors
- Additional Sensors within the Windows, Linux, MacOS, Network, and Cloud platform

Note: Pay attention to the differences between similar data sources and events. Two events with the same field names can represent different data. For example, process data collected from Sysmon 1, Windows Event 4688, and/or Windows Event 4696 could provide visibility into behaviors associated with T1134: Access Token Manipulation. But when looking for T1543: Create or Modify System Process, data should not be collected from Windows Event 4696 to prove adversary activity as this technique does not involve the use of system tokens. The following visuals are provided to help illustrate this example:

.. image:: _static/T1543EX.png
   :width: 600

.. image:: _static/T1134EX.png
   :width: 600

If you have any thoughts to future areas of research, please submit a `GitHub Issue <https://github.com/center-for-threat-informed-defense/sensor-mappings-to-attack/issues>`_