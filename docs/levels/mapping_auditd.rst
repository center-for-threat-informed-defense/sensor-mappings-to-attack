Auditd
======

Browse the Auditd mappings on this page, download the mappings (in CSV/STIX format), or
visualize the sensor coverage in ATT&CK Navigator.

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="../../csv/Auditd-sensors-mappings-enterprise.csv">
        <i class="fa fa-table"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="../../stix/Auditd-mappings-enterprise.json">
        <i class="fa fa-file-excel-o"></i> Download STIX</a>

        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/Auditd-heatmap.json">
        <i class="fa fa-map-signs"></i> Open in ATT&CK Navigator</a>
    </p>

.. MAPPINGS_TABLE Generated at: 2023-10-03T10:40:58.770502Z

.. list-table::
  :widths: 35 30 20 25
  :header-rows: 1

  * - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT

  * - ADD_GROUP
    - Triggered when a user-space group is added
    - Group
    - Group Creation

  * - ADD_USER
    - Triggered when a user-space user account is created
    - User Account
    - User Account Creation

  * - ANOM_ABEND
    - Triggered when a processes ends abnormally (with core dump, if enabled)
    - Process
    - Process Termination

  * - ANOM_ADD_ACCOUNT
    - Triggered when a user-space account addition ends abnormally
    - User Account
    - User Account Creation

  * - ANOM_DEL_ACCOUNT
    - Triggered when a user-space account deletion ends abnormally
    - User Account
    - User Account Deletion

  * - ANOM_LINK
    - Triggered when suspicious use of file links is detected
    - File
    - File Access

  * - ANOM_LOGIN_FAILURES
    - Triggered when the limit of failed login attempts is reached
    - User Account
    - User Account Authentication

  * - ANOM_LOGIN_LOCATION
    - Triggered when a login atempt is made from forbidden location
    - User Account
    - User Account Authentication

  * - ANOM_LOGIN_SESSIONS
    - Triggered when a login attempt reaches max amount of sessions
    - User Account
    - User Account Authentication

  * - ANOM_LOGIN_TIME
    - Triggered when a login attempt is made at a time when prevented
    - User Account
    - User Account Authentication

  * - ANOM_PROMISCUOUS
    - Triggered when a device enables or disables promiscuous mode
    - Service
    - Service Modification

  * - AVC
    - Triggered to record an SELinux permission check
    - Service
    - Service Access

  * - CONFIG_CHANGE
    - audit_enabled record field contains 1 or 2
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - audit_enabled record field contains 0
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - op record field contains add rule
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - op record field contains remove rule
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - audit_failure record field contains value 0
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - audit_failure record field contains value 1
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - audit_failure record field contains value 2
    - Service
    - Service Modification

  * - CONFIG_CHANGE
    - any other CONFIG_CHANGE cases not specified above
    - Service
    - Service Modification

  * - CRED_ACQ
    - Triggered when a user acquires user-space credentials
    - User Account
    - User Account Metadata

  * - CRED_DISP
    - Triggered when a user disposes of user-space credentials
    - User Account
    - User Account Metadata

  * - CRED_REFR
    - Triggered when a user refreshes their user-space credentials
    - User Account
    - User Account Access

  * - CRYPTO_KEY_USER
    - Triggered to record crypto key identifier used for crypto purposes
    - Logon Session
    - Logon Session Metadata

  * - CRYPTO_SESSION
    - Triggered to record parameters set during a TLS session establishment
    - Logon Session
    - Logon Session Creation

  * - DAEMON_ABORT
    - Triggered when a daemon is stopped due to an error
    - Service
    - Service Metadata

  * - DAEMON_CONFIG
    - Triggered when a daemon configuration change is detected
    - Service
    - Service Modification

  * - DAEMON_END
    - Triggered when a daemon is successfully stopped
    - Service
    - Service Metadata

  * - DAEMON_RESUME
    - Triggered when the auditd daemon resumes logging
    - Service
    - Service Metadata

  * - DAEMON_ROTATE
    - Triggered when the auditd daemon rotates the Audit log files
    - Service
    - Service Metadata

  * - DAEMON_START
    - Triggered when the auditd daemon is started
    - Service
    - Service Creation

  * - DEL_GROUP
    - Triggered when a user-space group is deleted
    - Group
    - Group Deletion

  * - DEL_USER
    - Triggered when a user-space user is deleted
    - User Account
    - User Account Deletion

  * - FS_RELABEL
    - Triggered when a file system relabel operation is detected
    - Drive
    - Drive Modification

  * - LABEL_LEVEL_CHANGE
    - Triggered when an object's level label is modified
    - File
    - File Modification

  * - LABEL_OVERRIDE
    - Triggered when administrator overrides object's level label
    - File
    - File Modification

  * - LOGIN
    - Triggered to record relevant login information when user logs into system
    - Logon Session
    - Logon Session Metadata

  * - MAC_CIPSOV4_ADD
    - Triggered when Commercial Internet Protocol Security Option user adds a new Domain of Interpretation (DOI) via NetLabel
    - Service
    - Service Modification

  * - MAC_CIPSOV4_DEL
    - Triggered when a CIPSO user deletes an existing DOI. Adding DOIs is a part of the packet labeling capabilities of the kernel provided by NetLabel
    - Service
    - Service Modification

  * - MAC_CONFIG_CHANGE
    - Triggered when an SELinux Boolean value is changed
    - Service
    - Service Modification

  * - MAC_MAP_ADD
    - Triggered when a new Linux Security Module (LSM) domain mapping is added. LSM domain mapping is a part of the packet labeling capabilities of the kernel provided by NetLabel.
    - Service
    - Service Modification

  * - MAC_MAP_DEL
    - Triggered when existing LSM domain mapping is deleted
    - Service
    - Service Modification

  * - MAC_POLICY_LOAD
    - Triggered when a SELinux Policy file is loaded
    - Service
    - Service Creation

  * - MAC_STATUS
    - Triggered when the SELinux mode is changed (enforcing, permissive, etc)
    - Service
    - Service Modification

  * - MAC_UNLBL_ALLOW
    - Triggered when unlabeled traffic is allowed when using packet labeling
    - Network Traffic
    - Network Traffic Content

  * - NETFILTER_CFG
    - Triggered when Netfilter chain modifications are detected
    - Firewall
    - Firewall Rule Modification

  * - RESP_ACCT_LOCK
    - Triggered when a user account is locked
    - User Account
    - User Account Authentication

  * - RESP_ACCT_UNLOCK_TIMED
    - Triggered when user account is unlocked after configured time
    - User Account
    - User Account Authentication

  * - ROLE_ASSIGN
    - Triggered when an administrator user assigns user to SELinux role
    - Service
    - Service Modification

  * - ROLE_REMOVE
    - Triggered when an administrator removes a user from an SELinux role
    - Service
    - Service Modification

  * - SELINUX_ERR
    - Triggered when an internal SELinux error is detected
    - Service
    - Service Metadata

  * - SYSTEM_RUNLEVEL
    - Triggered when the system run level is changed
    - Sensor Health
    - Host Status

  * - SYSTEM_SHUTDOWN
    - Triggered when the system is shut down
    - Sensor Health
    - Host Status

  * - TTY
    - Triggered when TTY input was sent to an administrative process
    - Process
    - Process Access

  * - USER_ACCT
    - Triggered when a user-space user authorization attempt is detected
    - User Account
    - User Account Authentication

  * - USER_AUTH
    - Triggered when a user-space user authentication attempt is detected
    - User Account
    - User Account Authentication

  * - USER_AVC
    - Triggered when a user-space AVC message is generated
    - File
    - File Access

  * - USER_CHAUTHTOK
    - op record field contains value change password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change expired password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change age
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change max age
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change min age
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change passwd warning
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change inactive days
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change passwd expiration
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change last change date
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value change all aging information
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value password attribute change
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value password aging data updated
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value display aging info
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value password status display
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value password status displayed for user
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value adding to group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value adding group member
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value adding user to group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value adding user to shadow group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing primary group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing group member
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing admin name in shadow group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing member in shadow group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value deleting group password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value deleting member
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value deleting user from group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value deleting user from shadow group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value removing group member
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value removing user from shadow group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value user lookup
    - User Account
    - User Account Accessed

  * - USER_CHAUTHTOK
    - op record field contains value adding group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value deleting group
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value adding user
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value adding home directory
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value deleting user entries
    - User Account
    - User Account Deletion

  * - USER_CHAUTHTOK
    - op record field contains value deleting user not found
    - User Account
    - User Account Deletion

  * - USER_CHAUTHTOK
    - op record field contains value deleting user
    - User Account
    - User Account Deletion

  * - USER_CHAUTHTOK
    - op record field contains value deleting user logged in
    - User Account
    - User Account Deletion

  * - USER_CHAUTHTOK
    - op record field contains value deleting mail file
    - File
    - File Deletion

  * - USER_CHAUTHTOK
    - op record field contains value deleting home directory
    - User Account
    - User Account Deletion

  * - USER_CHAUTHTOK
    - op record field contains value lock password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value delete password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value updating password
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value unlock password
    - User Account
    - User Account Metadata

  * - USER_CHAUTHTOK
    - op record field contains value changing name
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing uid
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing home directory
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value moving home directory
    - User Account
    - User Account Access

  * - USER_CHAUTHTOK
    - op record field contains value changing mail file name
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - op record field contains value changing mail file owner
    - User Account
    - User Account Modification

  * - USER_CHAUTHTOK
    - Triggered when a user account password or PIN is modified
    - User Account
    - User Account Modification

  * - USER_CMD
    - Triggered when a user-space shell command is executed
    - Process
    - Process Creation

  * - USER_END
    - Triggered when a user-space session is terminated
    - Logon Session
    - Logon Session Metadata

  * - USER_ERR
    - Triggered when a user account state error is detected
    - User Account
    - User Account Metadata

  * - USER_LABELED_EXPORT
    - Triggered when an object is exported with an SELinux label
    - File
    - File Metadata

  * - USER_LOGIN
    - Triggered when a user logs in
    - Logon Session
    - Logon Session Creation

  * - USER_LOGOUT
    - Triggered when a user logs out
    - Logon Session
    - Logon Session Metadata

  * - USER_ROLE_CHANGE
    - op record field is not present
    - User Account
    - User Account Modification

  * - USER_ROLE_CHANGE
    - op record field contains add SELinux user record
    - User Account
    - User Account Creation

  * - USER_ROLE_CHANGE
    - op record field contains delete SELinux user record
    - User Account
    - User Account Deletion

  * - USER_ROLE_CHANGE
    - any other USER_ROLE_CHANGE cases not specified above
    - User Account
    - User Account Modification

  * - USER_START
    - Triggered when a user-space session is started
    - Logon Session
    - Logon Session Creation

  * - USER_TTY
    - Triggered when an explanatory msg about TTY input to admin proc is sent
    - Service
    - Service Metadata

  * - USER_UNLABELED_EXPORT
    - Triggered when an object is exported without an SELinux label
    - File
    - File Metadata

  * - USYS_CONFIG
    - Triggered when a user-space system configuration change is detected
    - Command
    - Command Execution
.. /MAPPINGS_TABLE
