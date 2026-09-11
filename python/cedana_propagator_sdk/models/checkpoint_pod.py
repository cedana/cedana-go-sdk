from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoint_kind import CheckpointKind
    from .checkpoint_overrides import CheckpointOverrides
    from .checkpoint_reason import CheckpointReason

@dataclass
class CheckpointPod(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action_id property
    action_id: Optional[str] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # The kind property
    kind: Optional[CheckpointKind] = None
    # The namespace property
    namespace: Optional[str] = None
    # The overrides property
    overrides: Optional[CheckpointOverrides] = None
    # The pod_id property
    pod_id: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # The reason property
    reason: Optional[CheckpointReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointPod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointPod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointPod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .checkpoint_kind import CheckpointKind
        from .checkpoint_overrides import CheckpointOverrides
        from .checkpoint_reason import CheckpointReason

        from .checkpoint_kind import CheckpointKind
        from .checkpoint_overrides import CheckpointOverrides
        from .checkpoint_reason import CheckpointReason

        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(CheckpointKind)),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "overrides": lambda n : setattr(self, 'overrides', n.get_object_value(CheckpointOverrides)),
            "pod_id": lambda n : setattr(self, 'pod_id', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(CheckpointReason)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_enum_value("kind", self.kind)
        writer.write_str_value("namespace", self.namespace)
        writer.write_object_value("overrides", self.overrides)
        writer.write_str_value("pod_id", self.pod_id)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_enum_value("reason", self.reason)
        writer.write_additional_data_value(self.additional_data)
    

