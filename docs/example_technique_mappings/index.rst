Example Scenarios
=================

Examples are provided to depict how these mappings can be used to get from Sensor Events
to ATT&CK Data Sources to ATT&CK Techniques. It should be stated up front that there is
no easy, one-to-one mapping from data source to technique. In addition, not all events
are created equal in regard to visibility of specific techniques, and two events with
the same field names can in fact represent different data. Some amount of analyst
judgement is required and, whenever judgement is involved, there can be differences in
opinion. The mapping methodology and these examples are provided to demonstrate the
judgement and rationale to apply when identifying specific event visibility into
techniques. Of course, additonal customized considerations must also be given when
looking to provide insight into a specific environment.

.. toctree::

    windows
    linux
    cloudtrail
    network

Note that the initial SMAP work was developed using ATT&CKv13.1. The mappings include
some data components that are not represented in ATT&CKv13.1 and may not be represented
in more recent versions of ATT&CK. The reason for this is that ATT&CK does not include 
data components that do not currently have a relationship to a (sub-)technique. These 
mapped data components are being tracked by the ATT&CK team and will be considered for 
incorporation in future versions of ATT&CK as the overall ATT&CK catalog evolves.