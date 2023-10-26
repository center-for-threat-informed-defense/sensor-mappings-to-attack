import datetime
from schema import Schema, Optional


data_component_schema = Schema(
    {
        # STIX x-mitre-data-component specific properties
        "modified": str,
        "name": str,
        Optional("description"): str,

        # ATT&CK custom properties
        "x_mitre_data_source_ref": str,
        "x_mitre_modified_by_ref": str,
        "x_mitre_domains": [ str ],
        "x_mitre_version": str,
        "x_mitre_attack_spec_version": str,
        Optional("x_mitre_deprecated", False): bool,
    },
    ignore_extra_keys=True
)

data_source_schema = Schema(
    {
        # STIX x-mitre-data-source specific properties
        "modified": str,
        "name": str,
        Optional("description"): str,

        # ATT&CK custom properties
        "x_mitre_modified_by_ref": str,
        Optional("x_mitre_platforms"): [ str ],
        Optional("x_mitre_deprecated", False): bool,
        "x_mitre_domains": [ str ],
        "x_mitre_version": str,
        "x_mitre_attack_spec_version": str,
        "x_mitre_contributors": [ str ],
        Optional("x_mitre_collection_layers"): [ str ]
    },
    ignore_extra_keys=True
)

sensor_mapping_schema = Schema(
    {
        "event_id": str,
        Optional("description"): str,
        "data_source": str,
        "data_component": str,
        "source": str,
        "relationship": str,
        "target": str,
        Optional("x_mitre_data_source_id"): str
    },
    ignore_extra_keys=True
)