from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restore_overrides import RestoreOverrides
    from .restore_reason import RestoreReason

@dataclass
class RestorePod(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action_id property
    action_id: Optional[str] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # The overrides property
    overrides: Optional[RestoreOverrides] = None
    # The reason property
    reason: Optional[RestoreReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestorePod:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestorePod
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestorePod()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .restore_overrides import RestoreOverrides
        from .restore_reason import RestoreReason

        from .restore_overrides import RestoreOverrides
        from .restore_reason import RestoreReason

        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "overrides": lambda n : setattr(self, 'overrides', n.get_object_value(RestoreOverrides)),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(RestoreReason)),
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
        writer.write_str_value("action_id", self.action_id)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_object_value("overrides", self.overrides)
        writer.write_enum_value("reason", self.reason)
        writer.write_additional_data_value(self.additional_data)
    

