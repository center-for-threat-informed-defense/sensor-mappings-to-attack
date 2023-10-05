OSQuery Mappings
================
.. MAPPINGS_TABLE Generated at: 2023-10-03T10:40:58.770502Z

.. list-table::
  :widths: 40 30 20 25
  :header-rows: 1

  * - EVENT ID
    - EVENT DESCRIPTION
    - ATT&CK DATA SOURCE
    - ATT&CK DATA COMPONENT

  * - augeas  
    - Configuration files parsed by augeas  
    - File  
    - File Access
  
  * - smbios_tables 
    - BIOS (DMI) structure common details and content.  
    - Firmware  
    - Firmware Metadata
    
  * - wmi_bios_info 
    - Lists important information from the system bios. 
    - Firmware  
    - Firmware Metadata
    
  * - oem_strings 
    - OEM defined strings retrieved from SMBIOS.  
    - Firmware  
    - Firmware Metadata
    
  * - platform_info 
    - Information about EFI/UEFI/ROM and platform/boot. 
    - Firmware  
    - Firmware Metadata
    
  * - chrome_extension_content_scripts  
    - Content scripts associated with Chrome extensions 
    - Application Log 
    - Application Log Content
    
  * - chrome_extensions 
    - Chrome browser extensions 
    - Application Log 
    - Application Log Content
    
  * - firefox_addons  
    - Firefox browser extensions, webapps, and addons.  
    - Application Log 
    - Application Log Content
    
  * - ie_extensions 
    - Internet Explorer browser extensions. 
    - Application Log 
    - Application Log Content
    
  * - opera_extensions  
    - Opera browser extensions. 
    - Application Log 
    - Application Log Content
    
  * - safari_extensions 
    - Safari browser extension details for all users. 
    - Application Log 
    - Application Log Content
    
  * - browser_plugins 
    - All C/NPAPI browser plugin details for all users. 
    - Application Log 
    - Application Log Content
    
  * - shell_history 
    - A line-delimited (command) table of per-user .*_history data. 
    - Command 
    - Command Metadata
    
  * - hardware_events 
    - Hardware (PCI/USB/HID) events from UDEV or IOKit. 
    - Sensor Health 
    - Host Status
    
  * - mounts  
    - System mounted devices and filesystems (not process specific).  
    - Network Share 
    - Network Share Access
    
  * - pci_devices 
    - PCI devices active on the host system.  
    - Firmware  
    - Firmware Metadata
    
  * - hardware_events 
    - Hardware (PCI/USB/HID) events from UDEV or IOKit. 
    - Sensor Health 
    - Host Status
    
  * - hardware_events 
    - Hardware (PCI/USB/HID) events from UDEV or IOKit. 
    - Sensor Health 
    - Host Status
    
  * - disk_info 
    - Retrieve basic information about the physical disks of a system.  
    - Drive 
    - Drive Access
    
  * - disk_encryption 
    - Disk encryption status and information. 
    - Drive 
    - Drive Access
    
  * - logical_drives  
    - Details for logical drives on the system. A logical drive generally represents a single partition.  
    - Drive 
    - Drive Access
    
  * - disk_events 
    - Track DMG disk image events (appearance/disappearance) when opened  
    - Drive 
    - Drive Access
    
  * - device_partitions 
    - Use TSK to enumerate details about partitions on a disk device. 
    - Drive 
    - Drive Access
    
  * - drivers 
    - Details for in-use Windows device drivers. This does not display installed but unused drivers.  
    - Driver  
    - Driver Metadata
    
  * - authenticode  
    - File (executable, bundle, installer, disk) code signing status. 
    - File  
    - File Metadata
    
  * - file_events 
    - Track time/action changes to files specified in configuration data. 
    - File  
    - File Creation
    
  * - file_events 
    - Track time/action changes to files specified in configuration data. 
    - File  
    - File Modification
    
  * - file_events 
    - Track time/action changes to files specified in configuration data. 
    - File  
    - File Deletion
    
  * - ntfs_journal_events 
    - Track time/action changes to files specified in configuration data. 
    - File  
    - File Metadata
    
  * - elf_dynamic 
    - ELF dynamic section information.  
    - File  
    - File Metadata
    
  * - elf_info  
    - ELF file information. 
    - File  
    - File Metadata
    
  * - elf_sections  
    - ELF section information.  
    - File  
    - File Metadata
    
  * - elf_segments  
    - ELF segments information. 
    - File  
    - File Metadata
    
  * - elf_symbols 
    - ELF symbol list.  
    - File  
    - File Metadata
    
  * - extended_attributes 
    - Returns the extended attributes for files (similar to Windows ADS). 
    - File  
    - File Metadata
    
  * - hash  
    - Filesystem hash data. 
    - Driver  
    - Drive Metadata
    
  * - file  
    - Interactive filesystem attributes and metadata. 
    - File  
    - File Metadata
    
  * - magic 
    - Magic number recognition library table. 
    - File  
    - File Metadata
    
  * - ntfs_acl_permissions  
    - Retrieve NTFS ACL permission information for files and directories. 
    - File  
    - File Metadata
    
  * - signature 
    - File (executable, bundle, installer, disk) code signing status. 
    - File  
    - File Metadata
    
  * - ntfs_journal_events 
    - Track time/action changes to files specified in configuration data. 
    - File  
    - File Metadata
    
  * - acpi_tables 
    - Firmware ACPI functional table common metadata and content. 
    - Firmware  
    - Firmware Metadata
    
  * - memory_array_mapped_addresses 
    - Data associated for address mapping of physical memory arrays.  
    - Kernel  
    - Kernel Metadata
    
  * - memory_device_mapped_addresses  
    - Data associated for address mapping of physical memory devices. 
    - Kernel  
    - Kernel Metadata
    
  * - memory_error_info 
    - Data associated with errors of a physical memory array. 
    - Sensor Health 
    - Host Status
    
  * - memory_arrays 
    - Data associated with collection of memory devices that operate to form a memory address.  
    - Kernel  
    - Kernel Metadata
    
  * - memory_devices  
    - Physical memory device (type 17) information retrieved from SMBIOS. 
    - Kernel  
    - Kernel Metadata
    
  * - shared_memory 
    - OS shared memory regions. 
    - Kernel  
    - Kernel Metadata
    
  * - virtual_memory_info 
    - Darwin Virtual Memory statistics. 
    - Kernel  
    - Kernel Metadata
    
  * - arp_cache 
    - Address resolution cache, both static and dynamic (from ARP, NDP) 
    - Sensor Health 
    - Network Status
    
  * - dns_cache 
    - Enumerate the DNS cache using the undocumented DnsGetCacheDataTable function in dnsapi.dll. 
    - Sensor Health 
    - Network Status
    
  * - dns_resolvers 
    - Resolvers used by this host.  
    - Sensor Health 
    - Network Status
    
  * - lldp_neighbors  
    - LLDP neighbors of interfaces. 
    - Sensor Health 
    - Network Status
    
  * - etc_protocols 
    - Line-parsed /etc/protocols. 
    - Sensor Health 
    - Network Status
    
  * - etc_hosts 
    - Line-parsed /etc/hosts. 
    - Sensor Health 
    - Network Status
    
  * - etc_services  
    - Line-parsed /etc/services.  
    - Sensor Health 
    - Network Status
    
  * - routes  
    - The active route table for the host system. 
    - Sensor Health 
    - Network Status
    
  * - interface_details 
    - Detailed information and stats of network interfaces. 
    - Sensor Health 
    - Network Status
    
  * - interfaces  
    - Network interfaces and relevant metadata. 
    - Sensor Health 
    - Network Status
    
  * - interface_ipv6  
    - IPv6 configuration and stats of network interfaces. 
    - Sensor Health 
    - Network Status
    
  * - wifi_status 
    - OS X current WiFi status. 
    - Sensor Health 
    - Network Status
    
  * - shared_folders  
    - Folders available to others via SMB or AFP. 
    - Network Share 
    - Network Share Access
    
  * - nfs_shares  
    - NFS shares exported by the host.  
    - Network Share 
    - Network Share Access
    
  * - office_mru  
    - View recently opened Office documents.  
    - File  
    - File Access
    
  * - portage_keywords  
    - A summary about portage configurations like keywords, mask and unmask.  
    - Sensor Health 
    - Host Status
    
  * - portage_use 
    - List of enabled portage USE values for specific package.  
    - Sensor Health 
    - Host Status
    
  * - deb_packages  
    - The installed DEB package database. 
    - Sensor Health 
    - Host Status
    
  * - homebrew_packages 
    - The installed homebrew package database.  
    - Application Log 
    - Application Log Content
    
  * - npm_packages  
    - Lists all npm packages in a directory or globally installed in a system.  
    - Sensor Health 
    - Host Status
    
  * - portage_packages  
    - List of currently installed packages. 
    - Sensor Health 
    - Host Status
    
  * - programs  
    - Represents products as they are installed by Windows Installer. A product generally correlates to one installation package on Windows. Some fields may be blank as Windows installation details are left to the discretion of the product author. 
    - Sensor Health 
    - Host Status
    
  * - python_packages 
    - Python packages installed in a system.  
    - Sensor Health 
    - Host Status
    
  * - rpm_package_files 
    - RPM packages that are currently installed on the host system. 
    - Sensor Health 
    - Host Status
    
  * - rpm_packages  
    - RPM packages that are currently installed on the host system. 
    - Sensor Health 
    - Host Status
    
  * - apt_sources 
    - Current list of APT repositories or software channels.  
    - Sensor Health 
    - Host Status
    
  * - pipes 
    - Named and Anonymous pipes.  
    - Named Pipe  
    - Named Pipe Enumeration
    
  * - plist 
    - Read and parse a plist file.  
    - File  
    - File Access
    
  * - powershell_events 
    - Powershell script blocks reconstructed to their full script content, this table requires script block logging to be enabled.  
    - Script  
    - Script Execution
    
  * - process_events  
    - Track time/action process executions. 
    - Process 
    - Process Metadata
    
  * - process_envs  
    - A key/value table of environment variables for each process.  
    - Process 
    - Process Metadata
    
  * - listening_ports 
    - Processes with listening (bound) network sockets/ports. 
    - Sensor Health 
    - Network Status
    
  * - process_memory_map  
    - Process memory mapped files and pseudo device/regions.  
    - Process 
    - Process Metadata
    
  * - process_namespaces  
    - Linux namespaces for processes running on the host system.  
    - Process 
    - Process Metadata
    
  * - process_open_files  
    - File descriptors for each process.  
    - Process 
    - Process Metadata
    
  * - process_open_pipes  
    - Pipes and partner processes for each process. 
    - Process 
    - Process Metadata
    
  * - process_open_sockets  
    - Processes which have open network sockets on the system.  
    - Process 
    - Process Metadata
    
  * - process_file_events 
    - A File Integrity Monitor implementation using the audit service.  
    - File  
    - File Metadata
    
  * - processes 
    - All running processes on the host system. 
    - Process 
    - Process Enumeration
    
  * - appcompat_shims 
    - Application Compatibility shims are a way to persist malware. This table presents the AppCompat Shim information from the registry in a nice format.   
    - Windows Registry  
    - Windows Registry Key Access
    
  * - registry  
    - All of the Windows registry hives.  
    - Windows Registry  
    - Windows Registry Key Access
    
  * - userassist  
    - UserAssist Registry Key tracks when a user executes an application from Windows Explorer. 
    - Windows Registry  
    - Windows Registry Key Access
    
  * - selinux_events  
    - Track SELinux events. 
    - Sensor Health 
    - Host Status
    
  * - selinux_settings  
    - Track active SELinux settings.  
    - Sensor Health 
    - Host Status
    
  * - services  
    - Lists all installed Windows services and their relevant data. 
    - Service 
    - Service Enumeration
    
  * - socket_events 
    - Track network socket opens and closes.  
    - Network Traffic 
    - Network Traffic Content
    
  * - authorized_keys 
    - A line-delimited authorized_keys table  
    - User Account  
    - User Account Metadata
    
  * - ssh_configs 
    - A table of parsed ssh_configs.  
    - Sensor Health 
    - Network Status
    
  * - known_hosts 
    - A line-delimited known_hosts table. 
    - Sensor Health 
    - Network Status
    
  * - ad_config 
    - OS X Active Directory configuration.  
    - Active Directory  
    - Active Directory Metadata
    
  * - sandboxes 
    - OS X application sandboxes container details. 
    - Image 
    - Image Metadata
    
  * - app_schemes 
    - OS X application schemes and handlers (e.g., http, file, mailto). 
    - Sensor Health 
    - Host Status
    
  * - patches 
    - Lists all the patches applied. Note: This does not include patches applied via MSI or downloaded from Windows Update (e.g. Service Packs).  
    - Sensor Health 
    - Host Status
    
  * - authorization_mechanisms  
    - OS X Authorization mechanisms database. 
    - Kernel  
    - Kernel Module Load
    
  * - authorizations  
    - OS X Authorization rights database. 
    - User Account  
    - User Account Metadata
    
  * - autoexec  
    - Aggregate of executables that will automatically execute on the target machine. This is an amalgamation of other tables like services, scheduled_tasks, startup_items and more. 
    - Windows Registry  
    - Windows Registry Key Access
    
  * - background_activities_moderator 
    - Background Activities Moderator (BAM) tracks application execution. 
    - Process 
    - Process Metadata
    
  * - winbaseobj  
    - Lists named Windows objects in the default object directories, across all terminal services sessions. Example Windows ojbect types include Mutexes, Events, Jobs and Semaphors. 
    - Sensor Health 
    - Host Status
    
  * - system_info 
    - System information for identification.  
    - Sensor Health 
    - Host Status
    
  * - battery 
    - Provides information about the internal battery of a Macbook. 
    - Sensor Health 
    - Host Status
    
  * - bitlocker_info  
    - Retrieve bitlocker status of the machine. 
    - Driver  
    - Driver Metadata
    
  * - block_devices 
    - Block (buffered access) device file nodes: disks, ramdisks, and DMG containers. 
    - Sensor Health 
    - Host Status
    
  * - certificates  
    - Certificate Authorities installed in Keychains/ca-bundles.  
    - Certificate 
    - Certificate Registration
    
  * - chassis_info  
    - Display information pertaining to the chassis and its security status.  
    - Sensor Health 
    - Host Status
    
  * - cpuid 
    - Useful CPU features from the cpuid ASM call.  
    - Sensor Health 
    - Host Status
    
  * - cpu_info  
    - Info about the CPU running on the machine.  
    - Sensor Health 
    - Host Status
    
  * - cpu_time  
    - Displays information from /proc/stat file about the time the cpu cores spent in different parts of the system.  
    - Sensor Health 
    - Host Status
    
  * - windows_crashes 
    - Extracted information from Windows crash logs (Minidumps).  
    - Sensor Health 
    - Host Status
    
  * - crashes 
    - Application, System, and Mobile App crash logs. 
    - Sensor Health 
    - Host Status
    
  * - crontab 
    - Line parsed values from system and user cron/tab. 
    - Scheduled Job 
    - Scheduled Job Metadata
    
  * - default_environment 
    - Default environment variables and values. 
    - Sensor Health 
    - Host Status
    
  * - preferences 
    - OS X defaults and managed preferences.  
    - Sensor Health 
    - Host Status
    
  * - device_file 
    - Similar to the file table, but use TSK and allow block address access 
    - Drive 
    - Drive Access
    
  * - device_firmware 
    - A best-effort list of discovered firmware versions. 
    - Sensor Health 
    - Host Status
    
  * - device_hash 
    - Similar to the hash table, but use TSK and allow block address access 
    - File  
    - File Metadata
    
  * - asl 
    - Queries the Apple System Log data structure for system events 
    - Sensor Health 
    - Host Status
    
  * - event_taps  
    - Returns information about installed event taps. 
    - Sensor Health 
    - Host Status
    
  * - fan_speed_sensors 
    - Fan speeds. 
    - Sensor Health 
    - Host Status
    
  * - alf 
    - OS X application layer firewall (ALF) service details.  
    - Firewall  
    - Firewall Metadata
    
  * - alf_explicit_auths  
    - ALF services explicitly allowed to perform networking.  
    - Firewall  
    - Firewall Enumeration
    
  * - alf_exceptions  
    - OS X application layer firewall (ALF) service exceptions  
    - Firewall  
    - Firewall Rule Modification
    
  * - gatekeeper_apps 
    - Gatekeeper apps a user has allowed to run.  
    - Service 
    - Service Metadata
    
  * - gatekeeper  
    - OS X Gatekeeper Details.  
    - Service 
    - Service Metadata
    
  * - video_info  
    - Retrieve video card information of the machine. 
    - Sensor Health 
    - Host Status
    
  * - hvci_status 
    - Retrieve HVCI info of the machine.  
    - Sensor Health 
    - Host Status
    
  * - ibridge_info  
    - Information about the Apple iBridge hardware controller.  
    - Sensor Health 
    - Host Status
    
  * - windows_optional_features 
    - Lists names and installation states of windows features. Maps to Win32_OptionalFeature WMI class. 
    - Sensor Health 
    - Host Status
    
  * - apps  
    - OS X applications installed in known search paths (e.g., /Applications) 
    - Sensor Health 
    - Host Status
    
  * - sip_config  
    - Apple's System Integrity Protection (rootless) status.  
    - Sensor Health 
    - Host Status
    
  * - intel_me_info 
    - Intel ME/CSE Info.  
    - Sensor Health 
    - Host Status
    
  * - iokit_devicetree  
    - The IOKit registry matching the DeviceTree plane. 
    - Driver  
    - Driver Metadata
    
  * - iokit_registry  
    - The full IOKit registry without selecting a plane.  
    - Driver  
    - Driver Metadata
    
  * - kernel_extensions 
    - OS X's kernel extensions, both loaded and within the load search path.  
    - Kernel  
    - Kernel Metadata
    
  * - kernel_info 
    - Basic active kernel information.  
    - Kernel  
    - Kernel Metadata
    
  * - kernel_panics 
    - System kernel panic logs. 
    - Sensor Health 
    - Host Status
    
  * - system_controls 
    - sysctl names, values, and settings information. 
    - Sensor Health 
    - Host Status
    
  * - kva_speculative_info  
    - Display kernel virtual address and speculative execution information for the system.  
    - Kernel  
    - Kernel Metadata
    
  * - keychain_acls 
    - Applications that have ACL entries in the keychain. 
    - Sensor Health 
    - Host Status
    
  * - keychain_items  
    - Generic details about keychain items. 
    - Sensor Health 
    - Host Status
    
  * - launchd 
    - LaunchAgents and LaunchDaemons from default search paths. 
    - Scheduled Job 
    - Scheduled Job Metadata
    
  * - launchd_overrides 
    - Override keys, per user, for LaunchDaemons and Agents.  
    - Scheduled Job 
    - Scheduled Job Metadata
    
  * - fbsd_kmods  
    - Loaded FreeBSD kernel modules.  
    - Kernel  
    - Kernel Module Load
    
  * - kernel_modules  
    - Linux kernel modules both loaded and within the load search path. 
    - Kernel  
    - Kernel Module Load
    
  * - groups  
    - Local system groups.  
    - Group 
    - Group Metadata
  
  * - logged_in_users 
    - Users with an active shell on the system. 
    - Logon Session 
    - Logon Session Metadata
    
  * - last  
    - System logins and logouts.  
    - Logon Session 
    - Logon Session Metadata
    
  * - managed_policies  
    - The managed configuration policies from AD, MDM, MCX, etc.  
    - Active Directory  
    - Active Directory Object Access
    
  * - memory_info 
    - Main memory information in bytes. 
    - Sensor Health 
    - Host Status
    
  * - memory_map  
    - OS memory region map. 
    - Sensor Health 
    - Host Status
    
  * - connectivity  
    - Booleans about Windows network connectivity.  
    - Sensor Health 
    - Host Status
    
  * - ntdomains 
    - Display basic NT domain information of a Windows machine. 
    - Sensor Health 
    - Host Status
    
  * - os_version  
    - A single row containing the operating system name and version.  
    - Sensor Health 
    - Host Status
    
  * - package_bom 
    - OS X package bill of materials (BOM) file list. 
    - File  
    - File Metadata
    
  * - package_receipts  
    - OS X package receipt details. 
    - Process 
    - Process Metadata
    
  * - iptables  
    - Linux IP packet filtering and NAT tool. 
    - Firewall  
    - Firewall Enumeration
    
  * - cups_jobs 
    - Returns all completed print jobs from cups. 
    - Sensor Health 
    - Host Status
    
  * - cups_destinations 
    - Returns all configured printers.  
    - Sensor Health 
    - Host Status
    
  * - quicklook_cache 
    - Files and thumbnails within OS X's Quicklook Cache. 
    - File  
    - File Metadata
    
  * - windows_security_products 
    - Enumeration of registered Windows security products.  
    - Sensor Health 
    - Host Status
    
  * - ulimit_info 
    - System resource usage limits. 
    - Sensor Health 
    - Host Status
    
  * - running_apps 
    - macOS applications currently running on the host system.  
    - Process 
    - Process Creation
    
  * - screenlock  
    - macOS screenlock status for the current logged in user context. 
    - User Interface  
    - System Settings
    
  * - apparmor_events 
    - Track AppArmor (security auditing) events.  
    - Sensor Health 
    - Host Status
    
  * - apparmor_profiles 
    - Track active AppArmor profiles. 
    - Sensor Health 
    - Host Status
    
  * - windows_security_center 
    - The health status of Window Security features. Health values can be "Good", "Poor". "Snoozed", "Not Monitored", and "Error".  
    - Sensor Health 
    - Host Status
    
  * - shared_resources  
    - Displays shared resources on a computer system running Windows. This may be a disk drive, printer, interprocess communication, or other sharable device.  
    - Sensor Health 
    - Host Status
    
  * - sharing_preferences 
    - OS X Sharing preferences. 
    - Network Share 
    - Network Share Access
    
  * - shimcache 
    - Application Compatibility Cache, contains artifacts of execution. 
    - File  
    - File Metadata
    
  * - mdfind  
    - Run searches against the spotlight database.  
    - File  
    - File Metadata
    
  * - mdls  
    - Query file metadata in the Spotlight database.  
    - File  
    - File Metadata
    
  * - startup_items 
    - Applications and binaries set as user/login startup items.  
    - Windows Registry  
    - Windows Registry Key Access
    
  * - sudoers 
    - Rules for running commands as other users via sudo. 
    - Sensor Health 
    - Host Status
    
  * - suid_bin  
    - suid binaries in common locations.  
    - File  
    - File Metadata
    
  * - syslog_events 
    - Linux syslog events.  
    - Sensor Health 
    - Host Status
    
  * - time_machine_backups  
    - Backups to drives using TimeMachine.  
    - Drive 
    - Drive Modification
    
  * - time_machine_destinations 
    - Locations backed up to using Time Machine.  
    - Drive 
    - Drive Metadata
    
  * - usb_devices 
    - USB devices that are actively plugged into the host system. 
    - Drive 
    - Drive Creation
    
  * - xprotect_meta 
    - Database of the machine's XProtect browser-related signatures.  
    - Sensor Health 
    - Host Status
    
  * - xprotect_entries  
    - Database of the machine's XProtect signatures.  
    - Sensor Health 
    - Host Status
    
  * - xprotect_reports  
    - Database of XProtect matches (if user generated/sent an XProtect report). 
    - Sensor Health 
    - Host Status
    
  * - scheduled_tasks 
    - Lists all of the tasks in the Windows task scheduler. 
    - Scheduled Task  
    - Scheduled Task Enumeration
    
  * - account_policy_data 
    - Additional OS X user account data from the AccountPolicy section of OpenDirectory.  
    - User Account  
    - User Account Metadata
    
  * - users 
    - Local user accounts (including domain accounts that have logged on locally (Windows)).  
    - User Account  
    - User Account Access
    
  * - user_events 
    - Track user events from the audit framework. 
    - User Account  
    - User Account Authentication
    
  * - user_groups 
    - Local system user group relationships.  
    - Group 
    - Group Metadata
    
  * - logon_sessions  
    - Windows Logon Session.  
    - Logon Session 
    - Logon Session Metadata
    
  * - shadow  
    - Local system users encrypted passwords and related information. Please note, that you usually need superuser rights to access `/etc/shadow`.  
    - User Account  
    - User Account Metadata
  * - user_ssh_keys 
    - Returns the private keys in the users ~/.ssh directory and whether or not they are encrypted. 
    - User Account  
    - User Account Metadata
    
  * - wmi_cli_event_consumers 
    - WMI CommandLineEventConsumer, which can be used for persistence on Windows.  
    - WMI 
    - WMI Creation
    
  * - wmi_filter_consumer_binding 
    - Lists the relationship between event consumers and filters. 
    - WMI 
    - WMI Enumeration
    
  * - wmi_event_filters 
    - Lists WMI event filters.  
    - WMI 
    - WMI Enumeration
    
  * - wmi_script_event_consumers  
    - WMI ActiveScriptEventConsumer, which can be used for persistence on Windows. 
    - WMI 
    - WMI Creation
.. /MAPPINGS_TABLE