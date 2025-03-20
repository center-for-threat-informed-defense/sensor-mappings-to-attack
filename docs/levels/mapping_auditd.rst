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

.. MAPPINGS_TABLE Generated at: 2025-03-20T10:08:37.279022Z

Enterprise
----------

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - EVENT
    - ATT&CK MAPPING

  * - | **ADD_GROUP**
      |
      | Triggered when a user-space group is added
    - | **Data Source:** Group
      | **Data Component:** Group Creation

  * - | **ADD_USER**
      |
      | Triggered when a user-space user account is created
    - | **Data Source:** User Account
      | **Data Component:** User Account Creation

  * - | **ANOM_ABEND**
      |
      | Triggered when a processes ends abnormally (with core dump, if enabled)
    - | **Data Source:** Process
      | **Data Component:** Process Termination

  * - | **ANOM_ADD_ACCOUNT**
      |
      | Triggered when a user-space account addition ends abnormally
    - | **Data Source:** User Account
      | **Data Component:** User Account Creation

  * - | **ANOM_DEL_ACCOUNT**
      |
      | Triggered when a user-space account deletion ends abnormally
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **ANOM_LINK**
      |
      | Triggered when suspicious use of file links is detected
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **ANOM_LOGIN_FAILURES**
      |
      | Triggered when the limit of failed login attempts is reached
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ANOM_LOGIN_LOCATION**
      |
      | Triggered when a login atempt is made from forbidden location
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ANOM_LOGIN_SESSIONS**
      |
      | Triggered when a login attempt reaches max amount of sessions
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ANOM_LOGIN_TIME**
      |
      | Triggered when a login attempt is made at a time when prevented
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ANOM_PROMISCUOUS**
      |
      | Triggered when a device enables or disables promiscuous mode
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **AVC**
      |
      | Triggered to record an SELinux permission check
    - | **Data Source:** Service
      | **Data Component:** Service Access

  * - | **CONFIG_CHANGE**
      |
      | audit_enabled record field contains 1 or 2
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | audit_enabled record field contains 0
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | op record field contains add rule
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | op record field contains remove rule
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | audit_failure record field contains value 0
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | audit_failure record field contains value 1
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | audit_failure record field contains value 2
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CONFIG_CHANGE**
      |
      | any other CONFIG_CHANGE cases not specified above
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **CRED_ACQ**
      |
      | Triggered when a user acquires user-space credentials
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CRED_DISP**
      |
      | Triggered when a user disposes of user-space credentials
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **CRED_REFR**
      |
      | Triggered when a user refreshes their user-space credentials
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **CRYPTO_KEY_USER**
      |
      | Triggered to record crypto key identifier used for crypto purposes
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **CRYPTO_SESSION**
      |
      | Triggered to record parameters set during a TLS session establishment
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **DAEMON_ABORT**
      |
      | Triggered when a daemon is stopped due to an error
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **DAEMON_CONFIG**
      |
      | Triggered when a daemon configuration change is detected
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **DAEMON_END**
      |
      | Triggered when a daemon is successfully stopped
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **DAEMON_RESUME**
      |
      | Triggered when the auditd daemon resumes logging
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **DAEMON_ROTATE**
      |
      | Triggered when the auditd daemon rotates the Audit log files
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **DAEMON_START**
      |
      | Triggered when the auditd daemon is started
    - | **Data Source:** Service
      | **Data Component:** Service Creation

  * - | **DEL_GROUP**
      |
      | Triggered when a user-space group is deleted
    - | **Data Source:** Group
      | **Data Component:** Group Deletion

  * - | **DEL_USER**
      |
      | Triggered when a user-space user is deleted
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **FS_RELABEL**
      |
      | Triggered when a file system relabel operation is detected
    - | **Data Source:** Drive
      | **Data Component:** Drive Modification

  * - | **LABEL_LEVEL_CHANGE**
      |
      | Triggered when an object's level label is modified
    - | **Data Source:** File
      | **Data Component:** File Modification

  * - | **LABEL_OVERRIDE**
      |
      | Triggered when administrator overrides object's level label
    - | **Data Source:** File
      | **Data Component:** File Modification

  * - | **LOGIN**
      |
      | Triggered to record relevant login information when user logs into system
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **MAC_CIPSOV4_ADD**
      |
      | Triggered when Commercial Internet Protocol Security Option user adds a new Domain of Interpretation (DOI) via NetLabel
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **MAC_CIPSOV4_DEL**
      |
      | Triggered when a CIPSO user deletes an existing DOI. Adding DOIs is a part of the packet labeling capabilities of the kernel provided by NetLabel.
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **MAC_CONFIG_CHANGE**
      |
      | Triggered when an SELinux Boolean value is changed
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **MAC_MAP_ADD**
      |
      | Triggered when a new Linux Security Module (LSM) domain mapping is added. LSM domain mapping is a part of the packet labeling capabilities of the kernel provided by NetLabel.
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **MAC_MAP_DEL**
      |
      | Triggered when existing LSM domain mapping is deleted
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **MAC_POLICY_LOAD**
      |
      | Triggered when a SELinux Policy file is loaded
    - | **Data Source:** Service
      | **Data Component:** Service Creation

  * - | **MAC_STATUS**
      |
      | Triggered when the SELinux mode is changed (enforcing, permissive, etc)
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **MAC_UNLBL_ALLOW**
      |
      | Triggered when unlabeled traffic is allowed when using packet labeling
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **NETFILTER_CFG**
      |
      | Triggered when Netfilter chain modifications are detected
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **RESP_ACCT_LOCK**
      |
      | Triggered when a user account is locked
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **RESP_ACCT_UNLOCK_TIMED**
      |
      | Triggered when user account is unlocked after configured time
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **ROLE_ASSIGN**
      |
      | Triggered when an administrator user assigns user to SELinux role
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **ROLE_REMOVE**
      |
      | Triggered when an administrator removes a user from an SELinux role
    - | **Data Source:** Service
      | **Data Component:** Service Modification

  * - | **SELINUX_ERR**
      |
      | Triggered when an internal SELinux error is detected
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **SYSTEM_RUNLEVEL**
      |
      | Triggered when the system run level is changed
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **SYSTEM_SHUTDOWN**
      |
      | Triggered when the system is shut down
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **TTY**
      |
      | Triggered when TTY input was sent to an administrative process
    - | **Data Source:** Process
      | **Data Component:** Process Access

  * - | **USER_ACCT**
      |
      | Triggered when a user-space user authorization attempt is detected
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **USER_AUTH**
      |
      | Triggered when a user-space user authentication attempt is detected
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **USER_AVC**
      |
      | Triggered when a user-space AVC message is generated
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting mail file
    - | **Data Source:** File
      | **Data Component:** File Deletion

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value moving home directory
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value user lookup
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting user entries
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting user not found
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting user
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting user logged in
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting home directory
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value unlock password
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change expired password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change age
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change max age
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change min age
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change passwd warning
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change inactive days
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change passwd expiration
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change last change date
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value change all aging information
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value password attribute change
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value password aging data updated
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value display aging info
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value password status display
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value password status displayed for user
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding to group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding group member
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding user to group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding user to shadow group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing primary group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing group member
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing admin name in shadow group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing member in shadow group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting group password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting member
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting user from group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting user from shadow group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value removing group member
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value removing user from shadow group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value deleting group
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding user
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value adding home directory
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value lock password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value delete password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value updating password
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing name
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing uid
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing home directory
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing mail file name
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | op record field contains value changing mail file owner
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CHAUTHTOK**
      |
      | Triggered when a user account password or PIN is modified
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_CMD**
      |
      | Triggered when a user-space shell command is executed
    - | **Data Source:** Process
      | **Data Component:** Process Creation

  * - | **USER_END**
      |
      | Triggered when a user-space session is terminated
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **USER_ERR**
      |
      | Triggered when a user account state error is detected
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **USER_LABELED_EXPORT**
      |
      | Triggered when an object is exported with an SELinux label
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **USER_LOGIN**
      |
      | Triggered when a user logs in
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **USER_LOGOUT**
      |
      | Triggered when a user logs out
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **USER_ROLE_CHANGE**
      |
      | op record field contains add SELinux user record
    - | **Data Source:** User Account
      | **Data Component:** User Account Creation

  * - | **USER_ROLE_CHANGE**
      |
      | op record field contains delete SELinux user record
    - | **Data Source:** User Account
      | **Data Component:** User Account Deletion

  * - | **USER_ROLE_CHANGE**
      |
      | any other USER_ROLE_CHANGE cases not specified above
    - | **Data Source:** User Account
      | **Data Component:** User Account Modification

  * - | **USER_START**
      |
      | Triggered when a user-space session is started
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Creation

  * - | **USER_TTY**
      |
      | Triggered when an explanatory msg about TTY input to admin proc is sent
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **USER_UNLABELED_EXPORT**
      |
      | Triggered when an object is exported without an SELinux label
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **USYS_CONFIG**
      |
      | Triggered when a user-space system configuration change is detected
    - | **Data Source:** Command
      | **Data Component:** Command Execution
.. /MAPPINGS_TABLE
