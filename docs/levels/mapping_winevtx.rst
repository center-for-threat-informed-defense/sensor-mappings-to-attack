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

.. MAPPINGS_TABLE Generated at: 2023-10-03T10:40:58.770502Z

.. list-table::
  :widths: 10 30 20 25
  :header-rows: 1

  * - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT

  * - 1100
    - The event logging service has shut down.
    - sensor health
    - host status

  * - 1101
    - Audit events have been dropped by the transport.
    - sensor health
    - host status

  * - 1102
    - The audit log was cleared.
    - sensor health
    - host status

  * - 1104
    - The security Log is now full.
    - sensor health
    - host status

  * - 2002
    - A Windows Defender Firewall setting has changed.
    - firewall
    - firewall metadata

  * - 2003
    - A Windows Defender Firewall setting in the Private profile has changed.
    - firewall
    - firewall metadata

  * - 2004
    - A rule has been added to the Windows Defender Firewall exception list
    - firewall
    - firewall rule modification

  * - 2005
    - A rule has been modified in the Windows Defender Firewall exception list.
    - firewall
    - firewall rule modification

  * - 2006
    - A rule has been deleted in the Windows Defender Firewall exception list
    - firewall
    - firewall rule modification

  * - 2009
    - The Windows Firewall service failed to load Group Policy.
    - firewall
    - firewall metadata

  * - 2033
    - All rules have been deleted from the Windows Firewall configuration on this computer.
    - firewall
    - firewall rule modification

  * - 4103
    - Module logging.
    - command
    - command execution

  * - 4103
    - Module logging.
    - script
    - script execution

  * - 4104
    - Script Block Logging.
    - script
    - script execution

  * - 4610
    - An authentication package has been loaded by the Local Security Authority.
    - logon session
    - logon session metadata

  * - 4611
    - A trusted logon process has been registered with the Local Security Authority.
    - logon session
    - logon session metadata

  * - 4614
    - A notification package has been loaded by the Security Account Manager.
    - logon session
    - logon session metadata

  * - 4616
    - The system time was changed.
    - sensor health
    - host status

  * - 4622
    - A security package has been loaded by the Local Security Authority.
    - logon session
    - logon session metadata

  * - 4624
    - An account was successfully logged on
    - logon session
    - logon session creation

  * - 4625
    - An account failed to log on
    - user account
    - user account authentication

  * - 4627
    - Group membership information.
    - Group
    - Group Metdata

  * - 4634
    - An account was logged off
    - logon session
    - logon session metadata

  * - 4647
    - User initiated logoff.
    - logon session
    - logon session metadata

  * - 4648
    - A logon was attempted using explicit credentials.
    - user account
    - user account authentication

  * - 4656
    - A handle to an object was requested.
    - File
    - file access

  * - 4656
    - A handle to an object was requested.
    - named pipe
    - named pipe metadata

  * - 4656
    - A handle to an object was requested
    - Process
    - process access

  * - 4656
    - A handle to an object was requested.
    - service
    - service access

  * - 4656
    - A handle to an object was requested
    - windows registry
    - Windows Registry Key Access

  * - 4657
    - A registry value was modified.
    - windows registry
    - windows registry key creation

  * - 4657
    - A registry value was modified.
    - windows registry
    - windows registry key deletion

  * - 4657
    - A registry value was modified.
    - windows registry
    - windows registry key modification

  * - 4660
    - An object was deleted.
    - File
    - file deletion

  * - 4660
    - An object was deleted.
    - windows registry
    - windows registry key deletion

  * - 4661
    - A handle to an object was requested.
    - active directory
    - active directory object access

  * - 4661
    - A handle to an object was requested.
    - File
    - file access

  * - 4662
    - An operation was performed on an object.
    - active directory
    - active directory object access

  * - 4663
    - An attempt was made to access an object
    - File
    - file access

  * - 4663
    - An attempt was made to access an object.
    - File
    - file creation

  * - 4663
    - An attempt was made to access an object.
    - File
    - file deletion

  * - 4663
    - An attempt was made to access an object
    - Process
    - process access

  * - 4663
    - An attempt was made to access an object
    - windows registry
    - windows registry key access

  * - 4663
    - An attempt was made to access an object
    - windows registry
    - windows registry key modification

  * - 4664
    - An attempt was made to create a hard link.
    - File
    - file modification

  * - 4670
    - Permissions on an object were changed.
    - File
    - file modification

  * - 4670
    - Permissions on an object were changed.
    - windows registry
    - windows registry key modification

  * - 4672
    - Special privileges assigned to new logon.
    - logon session
    - logon session modification

  * - 4673
    - A privileged service was called.
    - logon session
    - logon session metadata

  * - 4674
    - An operation was attempted on a privileged object
    - User Account
    - User Account Metadata

  * - 4674
    - An operation was attempted on a privileged object.
    - logon session
    - logon session metadata

  * - 4688
    - Program execution. When you start a program you are creating a process that stays open until the program ends
    - Process
    - process creation

  * - 4689
    - A process has exited.
    - Process
    - process termination

  * - 4690
    - An attempt was made to duplicate a handle to an object.
    - File
    - file access

  * - 4696
    - A primary token was assigned to process. The assigning process fields identifies the process that started the child (new) process
    - Process
    - process creation

  * - 4697
    - A service was installed in the system.
    - service
    - service creation

  * - 4698
    - A scheduled task was created.
    - scheduled job
    - scheduled job creation

  * - 4699
    - A scheduled task was deleted.
    - scheduled job
    - scheduled job deletion

  * - 4700
    - A scheduled task was enabled.
    - scheduled job
    - scheduled job modification

  * - 4701
    - A scheduled task was disabled.
    - scheduled job
    - scheduled job modification

  * - 4702
    - A scheduled task was updated.
    - scheduled job
    - scheduled job modification

  * - 4703
    - A user right was adjusted.
    - user account
    - user account modification

  * - 4717
    - System security access was granted to an account.
    - user account
    - user account modification

  * - 4718
    - System security access was removed from an account.
    - user account
    - user account modification

  * - 4719
    - System audit policy was changed.
    - active directory
    - active directory object modification

  * - 4720
    - A user account was created
    - user account
    - user account creation

  * - 4722
    - A user account was enabled.
    - user account
    - user account modification

  * - 4723
    - An attempt was made to change an account's password.
    - user account
    - user account modification

  * - 4724
    - An attempt was made to reset an account's password
    - user account
    - user account modification

  * - 4725
    - A user account was disabled.
    - user account
    - user account modification

  * - 4726
    - A user account was deleted
    - user account
    - user account deletion

  * - 4727
    - A security-enabled global group was created.
    - group
    - group creation

  * - 4728
    - A member was added to a security-enabled global group.
    - group
    - group modification

  * - 4729
    - A member was removed from a security-enabled global group.
    - group
    - group modification

  * - 4730
    - A security-enabled global group was deleted.
    - group
    - group deletion

  * - 4731
    - A security-enabled local group was created.
    - group
    - group creation

  * - 4732
    - A member was added to a security-enabled local group.
    - group
    - group modification

  * - 4733
    - A member was removed from a security-enabled local group.
    - group
    - group modification

  * - 4734
    - A security-enabled local group was deleted.
    - group
    - group deletion

  * - 4735
    - A security-enabled local group was changed.
    - group
    - group modification

  * - 4737
    - A security-enabled global group was changed.
    - active directory
    - active directory object modification

  * - 4738
    - A user account was changed.
    - user account
    - user account modification

  * - 4740
    - A user account was locked out.
    - user account
    - user account modification

  * - 4741
    - A computer account was created.
    - user account
    - user account creation

  * - 4742
    - A computer account was changed.
    - user account
    - user account modification

  * - 4743
    - A computer account was deleted.
    - user account
    - user account deletion

  * - 4754
    - A security-enabled universal group was created.
    - group
    - group creation

  * - 4755
    - A security-enabled universal group was changed.
    - group
    - group modification

  * - 4756
    - A member was added to a security-enabled universal group.
    - group
    - group modification

  * - 4757
    - A member was removed from a security-enabled universal group.
    - group
    - group modification

  * - 4758
    - A security-enabled universal group was deleted.
    - group
    - group deletion

  * - 4764
    - A groups type was changed.
    - group
    - group modification

  * - 4767
    - A user account was unlocked.
    - user account
    - user account modification

  * - 4768
    - A Kerberos authentication ticket (TGT) was requested.
    - active directory
    - active directory credential request

  * - 4769
    - A Kerberos service ticket was requested.
    - active directory
    - active directory credential request

  * - 4770
    - A Kerberos service ticket was renewed
    - active directory
    - active directory object modification

  * - 4771
    - Kerberos pre-authentication failed
    - active directory
    - active directory credential request

  * - 4773
    - A Kerberos service ticket request failed
    - active directory
    - active directory object access

  * - 4776
    - The computer attempted to validate the credentials for an account
    - user account
    - user account authentication

  * - 4778
    - A session was reconnected to a Window Station.
    - logon session
    - logon session creation

  * - 4779
    - A session was disconnected from a Window Station
    - logon session
    - logon session terminated

  * - 4781
    - The name of an account was changed.
    - user account
    - user account modification

  * - 4798
    - A user's local group membership was enumerated.
    - group
    - group enumeration

  * - 4799
    - A security-enabled local group membership was enumerated.
    - group
    - group enumeration

  * - 4932
    - Synchronization of a replica of an Active Directory naming context has begun.
    - active directory
    - active directory object access

  * - 4946
    - A change has been made to Windows Firewall exception list. A rule was added.
    - firewall
    - firewall rule modification

  * - 4947
    - A change has been made to Windows Firewall exception list. A rule was modified.
    - firewall
    - firewall rule modification

  * - 4948
    - A change has been made to Windows Firewall exception list. A rule was deleted.
    - firewall
    - firewall rule modification

  * - 4950
    - A windows firewall setting has changed
    - firewall
    - firewall metadata

  * - 4954
    - Windows firewall group policy settings has changed
    - firewall
    - firewall metadata

  * - 4964
    - Special groups have been assigned to a new logon.
    - logon session
    - logon session creation

  * - 5024
    - The Windows Firewall Service has started successfully.
    - firewall
    - firewall enabled

  * - 5025
    - The Windows Firewall Service has been stopped.
    - firewall
    - firewall disable

  * - 5031
    - The Windows Firewall Service blocked an application from accepting incoming connections on the network.
    - network traffic
    - network connection creation

  * - 5034
    - The Windows Firewall Driver was stopped.
    - firewall
    - firewall disable

  * - 5136
    - A directory service object was modified.
    - active directory
    - active directory object modification

  * - 5137
    - A directory service object was created.
    - active directory
    - active directory object creation

  * - 5138
    - A directory service object was undeleted
    - active directory
    - active directory object creation

  * - 5139
    - A directory service object was moved.
    - active directory
    - active directory object modification

  * - 5140
    - A network share object was accessed.
    - network share
    - network share access

  * - 5141
    - A directory service object was deleted.
    - active directory
    - active directory object deletion

  * - 5142
    - A network share object was added.
    - network share
    - network share creation

  * - 5143
    - A network share object was modified.
    - network share
    - network share modification

  * - 5144
    - A network share object was deleted.
    - network share
    - network share deletion

  * - 5145
    - A network share object was checked to see whether client can be granted desired access.
    - named pipe
    - named pipe metadata

  * - 5145
    - A network share object was checked to see whether client can be granted desired access.
    - network share
    - network share access

  * - 5154
    - The Windows Filtering Platform has permitted an application or service to listen on a port for incoming connections.
    - network traffic
    - network connection creation

  * - 5154
    - The Windows Filtering Platform has permitted an application or service to listen on a port for incoming connections.
    - network traffic
    - network connection creation

  * - 5155
    - The Windows Filtering Platform has blocked an application or service from listening on a port for incoming connections.
    - network traffic
    - network connection creation

  * - 5155
    - The Windows Filtering Platform has blocked an application or service from listening on a port for incoming connections.
    - network traffic
    - network connection creation

  * - 5156
    - The Windows Filtering Platform has permitted a connection.
    - network traffic
    - network connection creation

  * - 5157
    - The Windows Filtering Platform has blocked a connection.
    - network traffic
    - network connection creation

  * - 5157
    - The Windows Filtering Platform has blocked a connection.
    - network traffic
    - network connection creation

  * - 5158
    - The Windows Filtering Platform has permitted a bind to a local port.
    - network traffic
    - network connection creation

  * - 5159
    - The Windows Filtering Platform has blocked a bind to a local port.
    - network traffic
    - network connection creation

  * - 5159
    - The Windows Filtering Platform has blocked a bind to a local port.
    - network traffic
    - network connection creation

  * - 5857
    - WMIProv provider started.
    - wmi
    - wmi creation

  * - 5858
    - WMI Query Error.
    - wmi
    - wmi creation

  * - 5859
    - WMI Event.
    - wmi
    - wmi creation

  * - 5860
    - WMI temporary event created.
    - wmi
    - wmi creation

  * - 5861
    - WMI permanent event created.
    - wmi
    - wmi creation

  * - 6005
    - The Event log service was started.
    - sensor health
    - host status

  * - 6005
    - The Event log service was started.
    - service
    - service metadata

  * - 6006
    - The Event log service was stopped.
    - sensor health
    - host status

  * - 6006
    - The Event log service was stopped.
    - service
    - service metadata

  * - 6416
    - A new external device was recognized by the system.
    - drive
    - drive creation

  * - 6419
    - A request was made to disable a device.
    - drive
    - drive modification

  * - 6420
    - A device was disabled.
    - drive
    - drive modification

  * - 6421
    - A request was made to enable a device.
    - drive
    - drive modification

  * - 6422
    - A device was enabled.
    - drive
    - drive modification

  * - 6423
    - The installation of this device is forbidden by system policy.
    - drive
    - drive creation

  * - 6424
    - The installation of this device was allowed, after having previously been forbidden by policy.
    - drive
    - drive creation
.. /MAPPINGS_TABLE
