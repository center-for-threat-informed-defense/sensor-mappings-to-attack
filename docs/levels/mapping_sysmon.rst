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

.. MAPPINGS_TABLE Generated at: 2025-03-20T10:08:37.277616Z

Enterprise
----------

.. list-table::
  :widths: 50 50
  :header-rows: 1

  * - EVENT
    - ATT&CK MAPPING

  * - | **1**
      |
      | A new process has been created
    - | **Data Source:** Process
      | **Data Component:** Process Creation

  * - | **2**
      |
      | A process changed a file creation time
    - | **Data Source:** File
      | **Data Component:** File Modification

  * - | **3**
      |
      | Network connection
    - | **Data Source:** Network Traffic
      | **Data Component:** Network Connection Creation

  * - | **4**
      |
      | Sysmon service state changed.
    - | **Data Source:** Service
      | **Data Component:** Service Metadata

  * - | **5**
      |
      | Process terminated
    - | **Data Source:** Process
      | **Data Component:** Process Termination

  * - | **6**
      |
      | Driver loaded
    - | **Data Source:** Driver
      | **Data Component:** Driver Load

  * - | **7**
      |
      | Image Loaded
    - | **Data Source:** Module
      | **Data Component:** Module Load

  * - | **8**
      |
      | The CreateRemoteThread event detects when a process creates a thread in another process.
    - | **Data Source:** Process
      | **Data Component:** Process Modification

  * - | **9**
      |
      | The RawAccessRead event detects when a process conducts reading operations from the drive using the \.\ denotation
    - | **Data Source:** File
      | **Data Component:** File Access

  * - | **10**
      |
      | ProcessAccess
    - | **Data Source:** Process
      | **Data Component:** Process Access

  * - | **11**
      |
      | FileCreate
    - | **Data Source:** File
      | **Data Component:** File Creation

  * - | **12**
      |
      | RegistryEvent (Object create and delete)
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Creation

  * - | **12**
      |
      | RegistryEvent (Object create and delete)
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Deletion

  * - | **13**
      |
      | RegistryEvent (Value Set)
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Modification

  * - | **14**
      |
      | RegistryEvent (Key and Value Rename)
    - | **Data Source:** Windows Registry
      | **Data Component:** Windows Registry Key Modification

  * - | **15**
      |
      | FileCreateStreamHash
    - | **Data Source:** File
      | **Data Component:** File Creation

  * - | **17**
      |
      | PipeEvent (Pipe Created)
    - | **Data Source:** Named Pipe
      | **Data Component:** Named Pipe Metadata

  * - | **18**
      |
      | PipeEvent (Pipe Connected)
    - | **Data Source:** Named Pipe
      | **Data Component:** Named Pipe Connection

  * - | **18**
      |
      | PipeEvent (Pipe Connected)
    - | **Data Source:** Named Pipe
      | **Data Component:** Named Pipe Metadata

  * - | **19**
      |
      | WmiEvent (WmiEventFilter activity detected).
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **19**
      |
      | WmiEvent (WmiEventFilter activity detected).
    - | **Data Source:** WMI
      | **Data Component:** WMI Deletion

  * - | **20**
      |
      | WmiEvent (WmiEventConsumer activity detected).
    - | **Data Source:** WMI
      | **Data Component:** WMI Creation

  * - | **20**
      |
      | WmiEvent (WmiEventConsumer activity detected).
    - | **Data Source:** WMI
      | **Data Component:** WMI Deletion

  * - | **23**
      |
      | FileDelete
    - | **Data Source:** File
      | **Data Component:** File Deletion

  * - | **26**
      |
      | File Delete logged.
    - | **Data Source:** File
      | **Data Component:** File Deletion

  * - | **30**
      |
      | EventID(30)
    - | **Data Source:** Process
      | **Data Component:** Process Metadata
.. /MAPPINGS_TABLE
