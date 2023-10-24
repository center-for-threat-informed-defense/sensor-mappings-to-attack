Step 3: Relationship Correlation
================================

Identify the Data Element
-------------------------

Next in reviewing the event ID, **identify the data element**. Once we identify and understand more about sources of data that can be mapped to an ATT&CK data source, we can start identifying data elements within the event fields that could help us eventually represent adversary behavior from a data perspective. 

As we mentioned in Step 2, `Event ID 4688 <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688>`_ also provides attributes that can help us to describe the data elements needed. For instance, regarding the user account data element, we have information of its logon id and the domain it belongs to. 

.. image:: ../_static/MSDN_4688_Ex_Attributes.png
   :width: 600

The use of Data Elements help to understand key attributes that are related to the adversary behavior. For example, if an adversary modifies a Windows Registry value, collection of Windows Registry telemetry is needed. 

Think about the questions below for additional context on how to establish data elements.

- *How is the adversary conducting a behavior?*
- *What are all the data objects that define the context of the data source?*
- *What are some attributes from the event log that contributes to the activity of the adversary behavior?*

.. image:: ../_static/DataElement_Ex.png
   :width: 700

This method can also be used to provide a general idea of what is needed to be collected. 

Note: There is a fundamental rule that should be considered when defining: **there is no one correct way to define data elements**. Please look to your organizational needs to help define what data elements means to you.

Identify Relationships among Data Elements
------------------------------------------

By documenting the event collection, source (creation of a new process), and data elements (user account and process), we can start describing **interactions among elements through relationships**. 

Note: Relationships in ATT&CK have been categorized between *activity* and *information*. Activity relationships are the ones that make references to the action that triggered the generation of the event. Informational relationships are the ones defined based on the metadata provided by the event. Therefore, please be aware of alternative data elements (i.e. a thread can create a process).

.. image:: ../_static/Relationship_Ex.png
   :width: 700

As discussed by `OSSEM <https://github.com/OTRF/OSSEM>`_ at their ATT&CKcon 2018 and 2019 presentation. The activity of the relationship leads to Data Components. Data Components will help us to categorize relationships among data elements based on the security context they describe (i.e. Creation, Execution, Deletion).   