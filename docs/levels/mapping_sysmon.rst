Sysmon
======

Browse the Sysmon mappings on this page, download the mappings (in CSV/STIX format), or
visualize the sensor coverage in ATT&CK Navigator.

.. raw:: html

    <p>
        <a class="btn btn-primary" target="_blank" href="../../csv/Sysmon-sensors-mappings-enterprise.csv">
        <i class="fa fa-table"></i> Download CSV</a>

        <a class="btn btn-primary" target="_blank" href="../../stix/Sysmon-mappings-enterprise.json">
        <i class="fa fa-file-excel-o"></i> Download STIX</a>

        <a class="btn btn-primary" target="_blank" href="https://mitre-attack.github.io/attack-navigator/#layerURL=https://center-for-threat-informed-defense.github.io/sensor-mappings-to-attack/navigator/Sysmon-heatmap.json">
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

  * - 1
    - A new process has been created
    - Process
    - process creation

  * - 2
    - A process changed a file creation time
    - File
    - file modification

  * - 3
    - Network connection
    - network traffic
    - network connection creation

  * - 4
    - Sysmon service state changed
    - service
    - service metadata

  * - 5
    - Process terminated
    - Process
    - process termination

  * - 6
    - Driver loaded
    - Driver
    - Driver load

  * - 7
    - Image Loaded
    - module
    - module load

  * - 8
    - The CreateRemoteThread event detects when a process creates a thread in another process.
    - Process
    - process modification

  * - 9
    - The RawAccessRead event detects when a process conducts reading operations from the drive using the \.\ denotation
    - File
    - file access

  * - 10
    - ProcessAccess
    - Process
    - process access

  * - 11
    - FileCreate
    - File
    - file creation

  * - 12
    - RegistryEvent (Object create and delete)
    - windows registry
    - windows registry key creation

  * - 12
    - RegistryEvent (Object create and delete)
    - windows registry
    - windows registry key deletion

  * - 13
    - RegistryEvent (Value Set)
    - windows registry
    - windows registry key modification

  * - 14
    - RegistryEvent (Key and Value Rename)
    - windows registry
    - windows registry key modification

  * - 15
    - FileCreateStreamHash
    - File
    - file creation

  * - 17
    - PipeEvent (Pipe Created)
    - named pipe
    - named pipe created

  * - 18
    - PipeEvent (Pipe Connected)
    - Named Pipe
    - Named Pipe Connection

  * - 19
    - WmiEvent (WmiEventFilter activity detected).
    - wmi
    - wmi creation

  * - 19
    - WmiEvent (WmiEventFilter activity detected).
    - wmi
    - wmi deletion

  * - 20
    - WmiEvent (WmiEventConsumer activity detected).
    - wmi
    - wmi creation

  * - 20
    - WmiEvent (WmiEventConsumer activity detected).
    - wmi
    - wmi deletion

  * - 23
    - FileDelete
    - File
    - file deletion

  * - 25
    - Process Tampering
    - Process
    - process modification

  * - 26
    - File Delete logged
    - File
    - file deletion

  * - 30
    - EventID(30)
    - Process
    - process metadata
.. /MAPPINGS_TABLE
