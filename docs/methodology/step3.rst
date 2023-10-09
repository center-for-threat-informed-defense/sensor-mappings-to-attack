Step 3: Relationship Correlation
================================

Identify the Data Element
-------------------------

Next in reviewing the event ID, **identify the data element**. Once we identify and understand more about sources of data that can be mapped to an ATT&CK data source, we can start identifying data elements within the event fields that could help us eventually represent adversary behavior from a data perspective. 

As we mentioned in Step 2, `Event ID 4688 <https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4688>`_ also provides attributes that can help us to describe the data elements needed. For instance, regarding the user account data element, we have information of its logon id and the domain it belongs to. 

.. image:: ../_static/WELEX4.png
   :width: 600

The use of Data Elements help to understand key attributes that are related to the adversary behavior. For example, if an adversary modifies a Windows Registry value, collection of Windows Registry telemetry is needed. **How the adversary modified the registry, such as the process or user that performed the action**, is how we pinpoint the data elements. Below continuing on with our process example. As we think about how an adversary can create a process we are left with process, user, command, and thread. 

.. image:: ../_static/DE3.png
   :width: 700

Additional questions to ask yourself is: 

- What are the main data objects to collect data from?
- What are all the data objects that define the context of the data source?
- What are some attributes from the event log that contributes to the activity of the adversary behavior?

This method can also be used to provide a general idea of what is needed to be collected. For example, data elements that provide metadata about network traffic can be grouped together and be associated with Netflow.

.. image:: ../_static/DE2.png
   :width: 600

The image below displays how we can extend the concept of an event log and capture the data elements featured within it. 

.. image:: ../_static/DE5.png
   :width: 600


There is a fundamental rule that should be considered when defining: **there is no one correct way to define data elements**. Please look to your organizational needs to help define what data elements means to you.

Identify Relationships among Data Elements
------------------------------------------

By documenting the event collection, source (creation of a new process), and data elements (user account and process), we can start describing **interactions among elements through relationships**. Relationships in ATT&CK have been categorized between *activity* and *information*. Activity relationships are the ones that make references to the action that triggered the generation of the event. Informational relationships are the ones defined based on the metadata provided by the event. 

.. image:: ../_static/RDE1.png
   :width: 600

As the groupings grow, the similarities appear where different platforms or sensors tend to link to the same ATT&CK Data Source. 

.. image:: ../_static/RDE4.png
   :width: 600

As discussed by `OSSEM <https://github.com/OTRF/OSSEM>`_ at their ATT&CKcon 2018 and 2019 presentation. The activity of the relationship leads to Data Components. Data Components will help us to categorize relationships among data elements based on the security context they describe (i.e. Creation, Execution, Deletion). 

.. image:: ../_static/RDE5.png
   :width: 700   