OSQuery
=======

Browse the OSQuery mappings on this page, download the mappings (in CSV/STIX format), or
visualize the sensor coverage in ATT&CK Navigator.

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="../../csv/OSQuery-sensors-mappings-enterprise.csv">
        <i class="fa fa-table"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="../../stix/OSQuery-mappings-enterprise.json">
        <i class="fa fa-file-excel-o"></i> Download STIX</a>

        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/OSQuery-heatmap.json">
        <i class="fa fa-map-signs"></i> Open in ATT&CK Navigator</a>
    </p>

.. MAPPINGS_TABLE Generated at: 2025-03-20T10:08:37.278765Z

Enterprise
----------

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - EVENT
    - ATT&CK MAPPING

  * - | **account_policy_data**
      |
      | Additional OS X user account data from the AccountPolicy section of OpenDirectory.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **acpi_tables**
      |
      | Firmware ACPI functional table common metadata and content.
    - | **Data Source:** Firmware
      | **Data Component:** Firmware Metadata

  * - | **ad_config**
      |
      | OS X Active Directory configuration.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Metadata

  * - | **alf**
      |
      | OS X application layer firewall (ALF) service details.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Metadata

  * - | **alf_exceptions**
      |
      | OS X application layer firewall (ALF) service exceptions
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Rule Modification

  * - | **alf_explicit_auths**
      |
      | ALF services explicitly allowed to perform networking.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Enumeration

  * - | **app_schemes**
      |
      | OS X application schemes and handlers (e.g., http, file, mailto).
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **apparmor_events**
      |
      | Track AppArmor (security auditing) events.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **apparmor_profiles**
      |
      | Track active AppArmor profiles.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **appcompat_shims**
      |
      | Application Compatibility shims are a way to persist malware. This table presents the AppCompat Shim information from the registry in a nice format. See http://files.brucon.org/2015/Tomczak_and_Ballenthin_Shims_for_the_Win.pdf for more details.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Access

  * - | **apps**
      |
      | OS X applications installed in known search paths (e.g., /Applications)
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **apt_sources**
      |
      | Current list of APT repositories or software channels.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **arp_cache**
      |
      | Address resolution cache, both static and dynamic (from ARP, NDP)
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **asl**
      |
      | Queries the Apple System Log data structure for system events
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **augeas**
      |
      | Configuration files parsed by augeas
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **authenticode**
      |
      | File (executable, bundle, installer, disk) code signing status.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **authorization_mechanisms**
      |
      | OS X Authorization mechanisms database.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Module Load

  * - | **authorizations**
      |
      | OS X Authorization rights database.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **authorized_keys**
      |
      | A line-delimited authorized_keys table
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **autoexec**
      |
      | Aggregate of executables that will automatically execute on the target machine. This is an amalgamation of other tables like services, scheduled_tasks, startup_items and more.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Access

  * - | **background_activities_moderator**
      |
      | Background Activities Moderator (BAM) tracks application execution.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **battery**
      |
      | Provides information about the internal battery of a Macbook.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **bitlocker_info**
      |
      | Retrieve bitlocker status of the machine.
    - | **Data Source:** Driver
      | **Data Component:** Driver Metadata

  * - | **block_devices**
      |
      | Block (buffered access) device file nodes: disks, ramdisks, and DMG containers.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **browser_plugins**
      |
      | All C/NPAPI browser plugin details for all users.
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **certificates**
      |
      | Certificate Authorities installed in Keychains/ca-bundles.
    - | **Data Source:** Certificate
      | **Data Component:** Certificate Registration

  * - | **chassis_info**
      |
      | Display information pertaining to the chassis and its security status.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **chrome_extension_content_scripts**
      |
      | Content scripts associated with Chrome extensions
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **chrome_extensions**
      |
      | Chrome browser extensions
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **connectivity**
      |
      | Booleans about Windows network connectivity.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **cpu_info**
      |
      | Info about the CPU running on the machine.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **cpu_time**
      |
      | Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **cpuid**
      |
      | Useful CPU features from the cpuid ASM call.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **crashes**
      |
      | Application, System, and Mobile App crash logs.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **crontab**
      |
      | Line parsed values from system and user cron/tab.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Metadata

  * - | **cups_destinations**
      |
      | Returns all configured printers.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **cups_jobs**
      |
      | Returns all completed print jobs from cups.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **deb_packages**
      |
      | The installed DEB package database.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **default_environment**
      |
      | Default environment variables and values.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **device_file**
      |
      | Similar to the file table, but use TSK and allow block address access
    - | **Data Source:** Drive
      | **Data Component:** Drive Access

  * - | **device_firmware**
      |
      | A best-effort list of discovered firmware versions.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **device_hash**
      |
      | Similar to the hash table, but use TSK and allow block address access
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **device_partitions**
      |
      | Use TSK to enumerate details about partitions on a disk device.
    - | **Data Source:** Drive
      | **Data Component:** Drive Access

  * - | **disk_encryption**
      |
      | Disk encryption status and information.
    - | **Data Source:** Drive
      | **Data Component:** Drive Access

  * - | **disk_events**
      |
      | Track DMG disk image events (appearance/disappearance) when opened
    - | **Data Source:** Drive
      | **Data Component:** Drive Access

  * - | **disk_info**
      |
      | Retrieve basic information about the physical disks of a system.
    - | **Data Source:** Drive
      | **Data Component:** Drive Access

  * - | **dns_cache**
      |
      | Enumerate the DNS cache using the undocumented DnsGetCacheDataTable function in dnsapi.dll.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **dns_resolvers**
      |
      | Resolvers used by this host.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **drivers**
      |
      | Details for in-use Windows device drivers. This does not display installed but unused drivers.
    - | **Data Source:** Driver
      | **Data Component:** Driver Metadata

  * - | **elf_dynamic**
      |
      | ELF dynamic section information.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **elf_info**
      |
      | ELF file information.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **elf_sections**
      |
      | ELF section information.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **elf_segments**
      |
      | ELF segments information.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **elf_symbols**
      |
      | ELF symbol list.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **etc_hosts**
      |
      | Line-parsed /etc/hosts.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **etc_protocols**
      |
      | Line-parsed /etc/protocols.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **etc_services**
      |
      | Line-parsed /etc/services.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **event_taps**
      |
      | Returns information about installed event taps.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **extended_attributes**
      |
      | Returns the extended attributes for files (similar to Windows ADS).
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **fan_speed_sensors**
      |
      | Fan speeds.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **fbsd_kmods**
      |
      | Loaded FreeBSD kernel modules.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Module Load

  * - | **file**
      |
      | Interactive filesystem attributes and metadata.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **file_events**
      |
      | Track time/action changes to files specified in configuration data.
    - | **Data Source:** File
      | **Data Component:** File Creation

  * - | **file_events**
      |
      | Track time/action changes to files specified in configuration data.
    - | **Data Source:** File
      | **Data Component:** File Deletion

  * - | **file_events**
      |
      | Track time/action changes to files specified in configuration data.
    - | **Data Source:** File
      | **Data Component:** File Modification

  * - | **firefox_addons**
      |
      | Firefox browser extensions, webapps, and addons.
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **gatekeeper**
      |
      | OS X Gatekeeper Details.
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **gatekeeper_apps**
      |
      | Gatekeeper apps a user has allowed to run.
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **groups**
      |
      | Local system groups.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **hardware_events**
      |
      | Hardware (PCI/USB/HID) events from UDEV or IOKit.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **hash**
      |
      | Filesystem hash data.
    - | **Data Source:** Driver
      | **Data Component:** Drive Metadata

  * - | **homebrew_packages**
      |
      | The installed homebrew package database.
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **hvci_status**
      |
      | Retrieve HVCI info of the machine.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **ibridge_info**
      |
      | Information about the Apple iBridge hardware controller.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **ie_extensions**
      |
      | Internet Explorer browser extensions.
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **intel_me_info**
      |
      | Intel ME/CSE Info.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **interface_details**
      |
      | Detailed information and stats of network interfaces.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **interface_ipv6**
      |
      | IPv6 configuration and stats of network interfaces.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **interfaces**
      |
      | Network interfaces and relevant metadata.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **iokit_devicetree**
      |
      | The IOKit registry matching the DeviceTree plane.
    - | **Data Source:** Driver
      | **Data Component:** Driver Metadata

  * - | **iokit_registry**
      |
      | The full IOKit registry without selecting a plane.
    - | **Data Source:** Driver
      | **Data Component:** Driver Metadata

  * - | **iptables**
      |
      | Linux IP packet filtering and NAT tool.
    - | **Data Source:** Firewall
      | **Data Component:** Firewall Enumeration

  * - | **kernel_extensions**
      |
      | OS X's kernel extensions, both loaded and within the load search path.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **kernel_info**
      |
      | Basic active kernel information.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **kernel_modules**
      |
      | Linux kernel modules both loaded and within the load search path.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Module Load

  * - | **kernel_panics**
      |
      | System kernel panic logs.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **keychain_acls**
      |
      | Applications that have ACL entries in the keychain.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **keychain_items**
      |
      | Generic details about keychain items.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **known_hosts**
      |
      | A line-delimited known_hosts table.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **kva_speculative_info**
      |
      | Display kernel virtual address and speculative execution information for the system.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **last**
      |
      | System logins and logouts.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **launchd**
      |
      | LaunchAgents and LaunchDaemons from default search paths.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Metadata

  * - | **launchd_overrides**
      |
      | Override keys, per user, for LaunchDaemons and Agents.
    - | **Data Source:** Scheduled Job
      | **Data Component:** Scheduled Job Metadata

  * - | **listening_ports**
      |
      | Processes with listening (bound) network sockets/ports.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **lldp_neighbors**
      |
      | LLDP neighbors of interfaces.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **logged_in_users**
      |
      | Users with an active shell on the system.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **logical_drives**
      |
      | Details for logical drives on the system. A logical drive generally represents a single partition.
    - | **Data Source:** Drive
      | **Data Component:** Drive Access

  * - | **logon_sessions**
      |
      | Windows Logon Session.
    - | **Data Source:** Logon Session
      | **Data Component:** Logon Session Metadata

  * - | **magic**
      |
      | Magic number recognition library table.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **managed_policies**
      |
      | The managed configuration policies from AD, MDM, MCX, etc.
    - | **Data Source:** Active Directory
      | **Data Component:** Active Directory Object Access

  * - | **mdfind**
      |
      | Run searches against the spotlight database.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **mdls**
      |
      | Query file metadata in the Spotlight database.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **memory_array_mapped_addresses**
      |
      | Data associated for address mapping of physical memory arrays.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **memory_arrays**
      |
      | Data associated with collection of memory devices that operate to form a memory address.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **memory_device_mapped_addresses**
      |
      | Data associated for address mapping of physical memory devices.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **memory_devices**
      |
      | Physical memory device (type 17) information retrieved from SMBIOS.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **memory_error_info**
      |
      | Data associated with errors of a physical memory array.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **memory_info**
      |
      | Main memory information in bytes.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **memory_map**
      |
      | OS memory region map.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **mounts**
      |
      | System mounted devices and filesystems (not process specific).
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Access

  * - | **nfs_shares**
      |
      | NFS shares exported by the host.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Access

  * - | **npm_packages**
      |
      | Lists all npm packages in a directory or globally installed in a system.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **ntdomains**
      |
      | Display basic NT domain information of a Windows machine.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **ntfs_acl_permissions**
      |
      | Retrieve NTFS ACL permission information for files and directories.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **ntfs_journal_events**
      |
      | Track time/action changes to files specified in configuration data.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **oem_strings**
      |
      | OEM defined strings retrieved from SMBIOS.
    - | **Data Source:** Firmware
      | **Data Component:** Firmware Metadata

  * - | **office_mru**
      |
      | View recently opened Office documents.
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **opera_extensions**
      |
      | Opera browser extensions.
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **os_version**
      |
      | A single row containing the operating system name and version.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **package_bom**
      |
      | OS X package bill of materials (BOM) file list.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **package_receipts**
      |
      | OS X package receipt details.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **patches**
      |
      | Lists all the patches applied. Note: This does not include patches applied via MSI or downloaded from Windows Update (e.g. Service Packs).
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **pci_devices**
      |
      | PCI devices active on the host system.
    - | **Data Source:** Firmware
      | **Data Component:** Firmware Metadata

  * - | **pipes**
      |
      | Named and Anonymous pipes.
    - | **Data Source:** Named Pipe
      | **Data Component:** Named Pipe Enumeration

  * - | **platform_info**
      |
      | Information about EFI/UEFI/ROM and platform/boot.
    - | **Data Source:** Firmware
      | **Data Component:** Firmware Metadata

  * - | **plist**
      |
      | Read and parse a plist file.
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **portage_keywords**
      |
      | A summary about portage configurations like keywords, mask and unmask.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **portage_packages**
      |
      | List of currently installed packages.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **portage_use**
      |
      | List of enabled portage USE values for specific package.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **powershell_events**
      |
      | Powershell script blocks reconstructed to their full script content, this table requires script block logging to be enabled.
    - | **Data Source:** Script
      | **Data Component:** Script Execution

  * - | **preferences**
      |
      | OS X defaults and managed preferences.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **process_envs**
      |
      | A key/value table of environment variables for each process.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **process_events**
      |
      | Track time/action process executions.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **process_file_events**
      |
      | A File Integrity Monitor implementation using the audit service.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **process_memory_map**
      |
      | Process memory mapped files and pseudo device/regions.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **process_namespaces**
      |
      | Linux namespaces for processes running on the host system.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **process_open_files**
      |
      | File descriptors for each process.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **process_open_pipes**
      |
      | Pipes and partner processes for each process.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **process_open_sockets**
      |
      | Processes which have open network sockets on the system.
    - | **Data Source:** Process
      | **Data Component:** Process Metadata

  * - | **processes**
      |
      | All running processes on the host system.
    - | **Data Source:** Process
      | **Data Component:** Process Enumeration

  * - | **programs**
      |
      | Represents products as they are installed by Windows Installer. A product generally correlates to one installation package on Windows. Some fields may be blank as Windows installation details are left to the discretion of the product author.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **python_packages**
      |
      | Python packages installed in a system.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **quicklook_cache**
      |
      | Files and thumbnails within OS X's Quicklook Cache.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **registry**
      |
      | All of the Windows registry hives.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Access

  * - | **routes**
      |
      | The active route table for the host system.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **rpm_package_files**
      |
      | RPM packages that are currently installed on the host system.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **rpm_packages**
      |
      | RPM packages that are currently installed on the host system.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **running_apps**
      |
      | macOS applications currently running on the host system.
    - | **Data Source:** Process
      | **Data Component:** Process Creation

  * - | **safari_extensions**
      |
      | Safari browser extension details for all users.
    - | **Data Source:** Application Log
      | **Data Component:** Application Log Content

  * - | **sandboxes**
      |
      | OS X application sandboxes container details.
    - | **Data Source:** Image
      | **Data Component:** Image Metadata

  * - | **scheduled_tasks**
      |
      | Lists all of the tasks in the Windows task scheduler.
    - | **Data Source:** Scheduled Task
      | **Data Component:** Scheduled Task Enumeration

  * - | **screenlock**
      |
      | macOS screenlock status for the current logged in user context.
    - | **Data Source:** User Interface
      | **Data Component:** System Settings

  * - | **selinux_events**
      |
      | Track SELinux events.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **selinux_settings**
      |
      | Track active SELinux settings.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **services**
      |
      | Lists all installed Windows services and their relevant data.
    - | **Data Source:** Service
      | **Data Component:** Service Enumeration

  * - | **shadow**
      |
      | Local system users encrypted passwords and related information. Please note, that you usually need superuser rights to access `/etc/shadow`.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **shared_folders**
      |
      | Folders available to others via SMB or AFP.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Access

  * - | **shared_memory**
      |
      | OS shared memory regions.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **shared_resources**
      |
      | Displays shared resources on a computer system running Windows. This may be a disk drive, printer, interprocess communication, or other sharable device.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **sharing_preferences**
      |
      | OS X Sharing preferences.
    - | **Data Source:** Network Share
      | **Data Component:** Network Share Access

  * - | **shell_history**
      |
      | A line-delimited (command) table of per-user .*_history data.
    - | **Data Source:** Command
      | **Data Component:** Command Metadata

  * - | **shimcache**
      |
      | Application Compatibility Cache, contains artifacts of execution.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **signature**
      |
      | File (executable, bundle, installer, disk) code signing status.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **sip_config**
      |
      | Apple's System Integrity Protection (rootless) status.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **smbios_tables**
      |
      | BIOS (DMI) structure common details and content.
    - | **Data Source:** Firmware
      | **Data Component:** Firmware Metadata

  * - | **socket_events**
      |
      | Track network socket opens and closes.
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Traffic Content

  * - | **ssh_configs**
      |
      | A table of parsed ssh_configs.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **startup_items**
      |
      | Applications and binaries set as user/login startup items.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Access

  * - | **sudoers**
      |
      | Rules for running commands as other users via sudo.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **suid_bin**
      |
      | suid binaries in common locations.
    - | **Data Source:** File
      | **Data Component:** File Metadata

  * - | **syslog_events**
      |
      | Linux syslog events.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **system_controls**
      |
      | sysctl names, values, and settings information.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **system_info**
      |
      | System information for identification.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **time_machine_backups**
      |
      | Backups to drives using TimeMachine.
    - | **Data Source:** Drive
      | **Data Component:** Drive Modification

  * - | **time_machine_destinations**
      |
      | Locations backed up to using Time Machine.
    - | **Data Source:** Drive
      | **Data Component:** Drive Metadata

  * - | **ulimit_info**
      |
      | System resource usage limits.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **usb_devices**
      |
      | USB devices that are actively plugged into the host system.
    - | **Data Source:** Drive
      | **Data Component:** Drive Creation

  * - | **user_events**
      |
      | Track user events from the audit framework.
    - | **Data Source:** User Account
      | **Data Component:** User Account Authentication

  * - | **user_groups**
      |
      | Local system user group relationships.
    - | **Data Source:** Group
      | **Data Component:** Group Metadata

  * - | **user_ssh_keys**
      |
      | Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted.
    - | **Data Source:** User Account
      | **Data Component:** User Account Metadata

  * - | **userassist**
      |
      | UserAssist Registry Key tracks when a user executes an application from Windows Explorer.
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Access

  * - | **users**
      |
      | Local user accounts (including domain accounts that have logged on locally (Windows)).
    - | **Data Source:** User Account
      | **Data Component:** User Account Access

  * - | **video_info**
      |
      | Retrieve video card information of the machine.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **virtual_memory_info**
      |
      | Darwin Virtual Memory statistics.
    - | **Data Source:** Kernel
      | **Data Component:** Kernel Metadata

  * - | **wifi_status**
      |
      | OS X current WiFi status.
    - | **Data Source:** Sensor Health
      | **Data Component:** Network Status

  * - | **winbaseobj**
      |
      | Lists named Windows objects in the default object directories, across all terminal services sessions. Example Windows ojbect types include Mutexes, Events, Jobs and Semaphors.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **windows_crashes**
      |
      | Extracted information from Windows crash logs (Minidumps).
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **windows_optional_features**
      |
      | Lists names and installation states of windows features. Maps to Win32_OptionalFeature WMI class.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **windows_security_center**
      |
      | The health status of Window Security features. Health values can be "Good", "Poor". "Snoozed", "Not Monitored", and "Error".
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **windows_security_products**
      |
      | Enumeration of registered Windows security products.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **wmi_bios_info**
      |
      | Lists important information from the system bios.
    - | **Data Source:** Firmware
      | **Data Component:** Firmware Metadata

  * - | **wmi_cli_event_consumers**
      |
      | WMI CommandLineEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **wmi_event_filters**
      |
      | Lists WMI event filters.
    - | **Data Source:** WMI
      | **Data Component:** WMI Enumeration

  * - | **wmi_filter_consumer_binding**
      |
      | Lists the relationship between event consumers and filters.
    - | **Data Source:** WMI
      | **Data Component:** WMI Enumeration

  * - | **wmi_script_event_consumers**
      |
      | WMI ActiveScriptEventConsumer, which can be used for persistence on Windows. See https://www.blackhat.com/docs/us-15/materials/us-15-Graeber-Abusing-Windows-Management-Instrumentation-WMI-To-Build-A-Persistent%20Asynchronous-And-Fileless-Backdoor-wp.pdf for more details.
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **xprotect_entries**
      |
      | Database of the machine's XProtect signatures.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **xprotect_meta**
      |
      | Database of the machine's XProtect browser-related signatures.
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status

  * - | **xprotect_reports**
      |
      | Database of XProtect matches (if user generated/sent an XProtect report).
    - | **Data Source:** Sensor Health
      | **Data Component:** Host Status
.. /MAPPINGS_TABLE
