WinEvtx
=======

Browse the WinEvtx mappings on this page, download the mappings (in CSV/STIX format), or
visualize the sensor coverage in ATT&CK Navigator.

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="../../csv/WinEvtx-sensors-mappings-enterprise.csv">
        <i class="fa fa-table"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="../../stix/WinEvtx-mappings-enterprise.json">
        <i class="fa fa-file-excel-o"></i> Download STIX</a>

        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/WinEvtx-heatmap.json">
        <i class="fa fa-map-signs"></i> Open in ATT&CK Navigator</a>
    </p>

.. MAPPINGS_TABLE Generated at: 2025-03-20T10:08:37.278215Z

Enterprise
----------

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - EVENT
    - ATT&CK MAPPING

  * - | **1100**
      |
      | The event logging service has shut down.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **1101**
      |
      | Audit events have been dropped by the transport.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **1102**
      |
      | The audit log was cleared.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **1104**
      |
      | The security Log is now full.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **2002**
      |
      | A Windows Defender Firewall setting has changed.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Metadata

  * - | **2003**
      |
      | A Windows Defender Firewall setting in the Private profile has changed.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Metadata

  * - | **2004**
      |
      | A rule has been added to the Windows Defender Firewall exception list
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **2005**
      |
      | A rule has been modified in the Windows Defender Firewall exception list.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **2006**
      |
      | A rule has been deleted in the Windows Defender Firewall exception list
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **2009**
      |
      | The Windows Firewall service failed to load Group Policy.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Metadata

  * - | **2033**
      |
      | All rules have been deleted from the Windows Firewall configuration on this computer.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **4103**
      |
      | Module logging.
    - | **Data Source:** Command
      | **Data Component:** Command Execution

  * - | **4103**
      |
      | Module logging.
    - | **Data Source:** Script
      | **Data Component:** Script Execution

  * - | **4104**
      |
      | Script Block Logging.
    - | **Data Source:** Script
      | **Data Component:** Script Execution

  * - | **4610**
      |
      | An authentication package has been loaded by the Local Security Authority.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4611**
      |
      | A trusted logon process has been registered with the Local Security Authority.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4614**
      |
      | A notification package has been loaded by the Security Account Manager.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4616**
      |
      | The system time was changed.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **4622**
      |
      | A security package has been loaded by the Local Security Authority.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4624**
      |
      | An account was successfully logged on
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **4625**
      |
      | An account failed to log on
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **4634**
      |
      | An account was logged off
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4647**
      |
      | User initiated logoff.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4648**
      |
      | A logon was attempted using explicit credentials.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **4656**
      |
      | A handle to an object was requested.
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **4656**
      |
      | A handle to an object was requested.
    - | **Data Source:** Named Pipe
      | **Data Component:** Named Pipe Metadata

  * - | **4656**
      |
      | A handle to an object was requested
    - | **Data Source:** Process
      | **Data Component:** Process Access

  * - | **4656**
      |
      | A handle to an object was requested.
    - | **Data Source:** Service
      | **Data Component:** Service Access

  * - | **4657**
      |
      | A registry value was modified.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Creation

  * - | **4657**
      |
      | A registry value was modified.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Deletion

  * - | **4657**
      |
      | A registry value was modified.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Modification

  * - | **4660**
      |
      | An object was deleted.
    - | **Data Source:** File
      | **Data Component:** File Deletion

  * - | **4660**
      |
      | An object was deleted.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Deletion

  * - | **4661**
      |
      | A handle to an object was requested.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Access

  * - | **4661**
      |
      | A handle to an object was requested.
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **4662**
      |
      | An operation was performed on an object.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Access

  * - | **4663**
      |
      | An attempt was made to access an object
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **4663**
      |
      | An attempt was made to access an object.
    - | **Data Source:** File
      | **Data Component:** File Creation

  * - | **4663**
      |
      | An attempt was made to access an object.
    - | **Data Source:** File
      | **Data Component:** File Deletion

  * - | **4663**
      |
      | An attempt was made to access an object
    - | **Data Source:** Process
      | **Data Component:** Process Access

  * - | **4663**
      |
      | An attempt was made to access an object
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Access

  * - | **4664**
      |
      | An attempt was made to create a hard link.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **4670**
      |
      | Permissions on an object were changed.
    - | **Data Source:** File
      | **Data Component:** File Modification

  * - | **4670**
      |
      | Permissions on an object were changed.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Modification

  * - | **4672**
      |
      | Special privileges assigned to new logon.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Modification

  * - | **4673**
      |
      | A privileged service was called.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4674**
      |
      | An operation was attempted on a privileged object.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **4674**
      |
      | An operation was attempted on a privileged object
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **4688**
      |
      | Program execution. When you start a program you are creating a process that stays open until the program ends
    - | **Data Source:** Process
      | **Data Component:** Process Creation

  * - | **4689**
      |
      | A process has exited.
    - | **Data Source:** Process
      | **Data Component:** Process Termination

  * - | **4690**
      |
      | An attempt was made to duplicate a handle to an object.
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **4696**
      |
      | A primary token was assigned to process. The assigning process fields identifies the process that started the child (new) process
    - | **Data Source:** Process
      | **Data Component:** Process Creation

  * - | **4697**
      |
      | A service was installed in the system.
    - | **Data Source:** Service
      | **Data Component:** Service Creation

  * - | **4698**
      |
      | A scheduled task was created.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Creation

  * - | **4699**
      |
      | A scheduled task was deleted.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Deletion

  * - | **4700**
      |
      | A scheduled task was enabled.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Modification

  * - | **4701**
      |
      | A scheduled task was disabled.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Modification

  * - | **4702**
      |
      | A scheduled task was updated.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Modification

  * - | **4703**
      |
      | A user right was adjusted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4717**
      |
      | System security access was granted to an account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4718**
      |
      | System security access was removed from an account.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4719**
      |
      | System audit policy was changed.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **4720**
      |
      | A user account was created
    - | **Data Source:** User Account
      | **Data Component:** User Account Creation

  * - | **4722**
      |
      | A user account was enabled.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4723**
      |
      | An attempt was made to change an account's password.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4724**
      |
      | An attempt was made to reset an account's password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4725**
      |
      | A user account was disabled.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4726**
      |
      | A user account was deleted
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **4727**
      |
      | A security-enabled global group was created.
    - | **Data Source:** Group
      | **Data Component:** Group Creation

  * - | **4729**
      |
      | A member was removed from a security-enabled global group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4730**
      |
      | A security-enabled global group was deleted.
    - | **Data Source:** Group
      | **Data Component:** Group Deletion

  * - | **4731**
      |
      | A security-enabled local group was created.
    - | **Data Source:** Group
      | **Data Component:** Group Creation

  * - | **4732**
      |
      | A member was added to a security-enabled local group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4733**
      |
      | A member was removed from a security-enabled local group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4734**
      |
      | A security-enabled local group was deleted.
    - | **Data Source:** Group
      | **Data Component:** Group Deletion

  * - | **4735**
      |
      | A security-enabled local group was changed.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4737**
      |
      | A security-enabled global group was changed.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **4738**
      |
      | A user account was changed.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4740**
      |
      | A user account was locked out.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4741**
      |
      | A computer account was created.
    - | **Data Source:** User Account
      | **Data Component:** User Account Creation

  * - | **4742**
      |
      | A computer account was changed.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4743**
      |
      | A computer account was deleted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **4754**
      |
      | A security-enabled universal group was created.
    - | **Data Source:** Group
      | **Data Component:** Group Creation

  * - | **4755**
      |
      | A security-enabled universal group was changed.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4756**
      |
      | A member was added to a security-enabled universal group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4757**
      |
      | A member was removed from a security-enabled universal group.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4758**
      |
      | A security-enabled universal group was deleted.
    - | **Data Source:** Group
      | **Data Component:** Group Deletion

  * - | **4764**
      |
      | A groups type was changed.
    - | **Data Source:** Group
      | **Data Component:** Group Modification

  * - | **4767**
      |
      | A user account was unlocked.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4768**
      |
      | A Kerberos authentication ticket (TGT) was requested.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Credential Request

  * - | **4769**
      |
      | A Kerberos service ticket was requested.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Credential Request

  * - | **4770**
      |
      | A Kerberos service ticket was renewed
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **4771**
      |
      | Kerberos pre-authentication failed
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Credential Request

  * - | **4773**
      |
      | A Kerberos service ticket request failed
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Access

  * - | **4776**
      |
      | The computer attempted to validate the credentials for an account
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **4778**
      |
      | A session was reconnected to a Window Station.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **4779**
      |
      | A session was disconnected from a Window Station
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Terminated

  * - | **4781**
      |
      | The name of an account was changed.
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **4798**
      |
      | A user's local group membership was enumerated.
    - | **Data Source:** Group
      | **Data Component:** Group Enumeration

  * - | **4799**
      |
      | A security-enabled local group membership was enumerated.
    - | **Data Source:** Group
      | **Data Component:** Group Enumeration

  * - | **4932**
      |
      | Synchronization of a replica of an Active Directory naming context has begun.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Access

  * - | **4946**
      |
      | A change has been made to Windows Firewall exception list. A rule was added.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **4947**
      |
      | A change has been made to Windows Firewall exception list. A rule was modified.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **4948**
      |
      | A change has been made to Windows Firewall exception list. A rule was deleted.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **4950**
      |
      | A windows firewall setting has changed
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Metadata

  * - | **4954**
      |
      | Windows firewall group policy settings has changed
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Metadata

  * - | **4964**
      |
      | Special groups have been assigned to a new logon.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **5024**
      |
      | The Windows Firewall Service has started successfully.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Enabled

  * - | **5025**
      |
      | The Windows Firewall Service has been stopped.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Disable

  * - | **5031**
      |
      | The Windows Firewall Service blocked an application from accepting incoming connections on the network.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5034**
      |
      | The Windows Firewall Driver was stopped.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Disable

  * - | **5136**
      |
      | A directory service object was modified.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **5137**
      |
      | A directory service object was created.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Creation

  * - | **5138**
      |
      | A directory service object was undeleted
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Creation

  * - | **5139**
      |
      | A directory service object was moved.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Modification

  * - | **5140**
      |
      | A network share object was accessed.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Access

  * - | **5141**
      |
      | A directory service object was deleted.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Deletion

  * - | **5142**
      |
      | A network share object was added.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Creation

  * - | **5143**
      |
      | A network share object was modified.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Modification

  * - | **5144**
      |
      | A network share object was deleted.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Deletion

  * - | **5145**
      |
      | A network share object was checked to see whether client can be granted desired access.
    - | **Data Source:** Named Pipe
      | **Data Component:** Named Pipe Metadata

  * - | **5145**
      |
      | A network share object was checked to see whether client can be granted desired access.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Access

  * - | **5154**
      |
      | The Windows Filtering Platform has permitted an application or service to listen on a port for incoming connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5155**
      |
      | The Windows Filtering Platform has blocked an application or service from listening on a port for incoming connections.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5156**
      |
      | The Windows Filtering Platform has permitted a connection.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5157**
      |
      | The Windows Filtering Platform has blocked a connection.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5158**
      |
      | The Windows Filtering Platform has permitted a bind to a local port.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5159**
      |
      | The Windows Filtering Platform has blocked a bind to a local port.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **5857**
      |
      | WMIProv provider started.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **5858**
      |
      | WMI Query Error.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **5859**
      |
      | WMI Event.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **5860**
      |
      | WMI temporary event created.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **5861**
      |
      | WMI permanent event created.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **6005**
      |
      | The Event log service was started.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **6005**
      |
      | The Event log service was started.
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **6006**
      |
      | The Event log service was stopped.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **6006**
      |
      | The Event log service was stopped.
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **6416**
      |
      | A new external device was recognized by the system.
    - | **Data Source:** Drive
      | **Data Component:** Drive Creation

  * - | **6419**
      |
      | A request was made to disable a device.
    - | **Data Source:** Drive
      | **Data Component:** Drive Modification

  * - | **6420**
      |
      | A device was disabled.
    - | **Data Source:** Drive
      | **Data Component:** Drive Modification

  * - | **6421**
      |
      | A request was made to enable a device.
    - | **Data Source:** Drive
      | **Data Component:** Drive Modification

  * - | **6422**
      |
      | A device was enabled.
    - | **Data Source:** Drive
      | **Data Component:** Drive Modification

  * - | **6423**
      |
      | The installation of this device is forbidden by system policy.
    - | **Data Source:** Drive
      | **Data Component:** Drive Creation

  * - | **6424**
      |
      | The installation of this device was allowed, after having previously been forbidden by policy.
    - | **Data Source:** Drive
      | **Data Component:** Drive Creation
.. /MAPPINGS_TABLE
