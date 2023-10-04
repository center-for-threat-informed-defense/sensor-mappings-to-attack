Mappings
========
.. MAPPINGS_TABLE Generated at: 2023-10-03T10:40:58.770502Z

.. excel-table::
   :file: /_static/SENSORMAPPING.xlsx
   :sheet: Sheet
   :selection: A1:H5


Windows Event Logs
------------------

.. list-table::
  :widths: 20 15 25 20 25 20 20 20
  :header-rows: 1

  * - SENSOR
    - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT
    - DATA ELEMENT SOURCE 
    - ACTIVITY
    - DATA ELEMENT TARGET

  * - WinEvtx
    - 4768
    - Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request
    - user
    - requested
    - ad credentials

Sysmon
------

.. list-table::
  :widths: 20 15 25 20 25 20 20 20
  :header-rows: 1

  * - SENSOR
    - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT
    - DATA ELEMENT SOURCE 
    - ACTIVITY
    - DATA ELEMENT TARGET

  * - WinEvtx
    - 4768
    - Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request
    - user
    - requested
    - ad credentials

Auditd
------

.. list-table::
  :widths: 15 25 20 25 20 20 20
  :header-rows: 1

  * - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT
    - DATA ELEMENT SOURCE 
    - ACTIVITY
    - DATA ELEMENT TARGET

  * - WinEvtx
    - 4768
    - Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request
    - user
    - requested
    - ad credentials

  * - ADD_GROUP	
    - Triggered when a user-space group is added	
    - Group	
    - Group Creation	
    - process/user	
    - created	
    - group

  * - ADD_USER	
    - Triggered when a user-space user account is created	
    - User Account
    - User Account Creation	
    - process/user	
    - created
    - user account


ZEEK
----

.. list-table::
  :widths: 20 15 25 20 25 20 20 20
  :header-rows: 1

  * - SENSOR
    - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT
    - DATA ELEMENT SOURCE 
    - ACTIVITY
    - DATA ELEMENT TARGET

  * - WinEvtx
    - 4768
    - Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request
    - user
    - requested
    - ad credentials

CloudTrail
----------

.. list-table::
  :widths: 20 15 25 20 25 20 20 20
  :header-rows: 1

  * - SENSOR
    - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT
    - DATA ELEMENT SOURCE 
    - ACTIVITY
    - DATA ELEMENT TARGET

  * - WinEvtx
    - 4768
    - Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request
    - user
    - requested
    - ad credentials

OSQuery
-------

.. list-table::
  :widths: 20 15 25 20 25 20 20 20
  :header-rows: 1

  * - SENSOR
    - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT
    - DATA ELEMENT SOURCE 
    - ACTIVITY
    - DATA ELEMENT TARGET

  * - WinEvtx
    - 4768
    - Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request
    - user
    - requested
    - ad credentials
.. /MAPPINGS_TABLE