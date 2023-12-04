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

.. MAPPINGS_TABLE Generated at: 2023-12-04T02:13:58.207379Z

Enterprise
----------

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
    - Process Creation

  * - 2
    - A process changed a file creation time
    - File
    - File Modification

  * - 3
    - Network connection
    - Network Traffic
    - Network Connection Creation

  * - 4
    - Sysmon service state changed.
    - Service
    - Service Metadata

  * - 5
    - Process terminated
    - Process
    - Process Termination

  * - 6
    - Driver loaded
    - Driver
    - Driver Load

  * - 7
    - Image Loaded
    - Module
    - Module Load

  * - 8
    - The CreateRemoteThread event detects when a process creates a thread in another process.
    - Process
    - Process Modification

  * - 9
    - The RawAccessRead event detects when a process conducts reading operations from the drive using the \.\ denotation
    - File
    - File Access

  * - 10
    - ProcessAccess
    - Process
    - Process Access

  * - 11
    - FileCreate
    - File
    - File Creation

  * - 12
    - RegistryEvent (Object create and delete)
    - Windows Registry
    - Windows Registry Key Creation

  * - 12
    - RegistryEvent (Object create and delete)
    - Windows Registry
    - Windows Registry Key Deletion

  * - 13
    - RegistryEvent (Value Set)
    - Windows Registry
    - Windows Registry Key Modification

  * - 14
    - RegistryEvent (Key and Value Rename)
    - Windows Registry
    - Windows Registry Key Modification

  * - 15
    - FileCreateStreamHash
    - File
    - File Creation

  * - 17
    - PipeEvent (Pipe Created)
    - Named Pipe
    - Named Pipe Metadata

  * - 18
    - PipeEvent (Pipe Connected)
    - Named Pipe
    - Named Pipe Connection

  * - 18
    - PipeEvent (Pipe Connected)
    - Named Pipe
    - Named Pipe Metadata

  * - 19
    - WmiEvent (WmiEventFilter activity detected).
    - WMI
    - WMI Creation

  * - 19
    - WmiEvent (WmiEventFilter activity detected).
    - WMI
    - WMI Deletion

  * - 20
    - WmiEvent (WmiEventConsumer activity detected).
    - WMI
    - WMI Creation

  * - 20
    - WmiEvent (WmiEventConsumer activity detected).
    - WMI
    - WMI Deletion

  * - 23
    - FileDelete
    - File
    - File Deletion

  * - 26
    - File Delete logged.
    - File
    - File Deletion

  * - 30
    - EventID(30)
    - Process
    - Process Metadata
.. /MAPPINGS_TABLE
