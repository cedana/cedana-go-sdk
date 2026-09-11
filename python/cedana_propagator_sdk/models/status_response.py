from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoint_operation_status import CheckpointOperationStatus

@dataclass
class StatusResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The details property
    details: Optional[str] = None
    # The status property
    status: Optional[CheckpointOperationStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StatusResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StatusResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StatusResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .checkpoint_operation_status import CheckpointOperationStatus

        from .checkpoint_operation_status import CheckpointOperationStatus

        fields: dict[str, Callable[[Any], None]] = {
            "details": lambda n : setattr(self, 'details', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(CheckpointOperationStatus)),
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
        writer.write_str_value("details", self.details)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

