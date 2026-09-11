from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .slurm_checkpoint_status import SlurmCheckpointStatus

@dataclass
class SlurmCheckpoint(AdditionalDataHolder, Parsable):
    """
    Checkpoint is basic unit for cedana service operationit stores all the information regarding the snapshot we can use to save and then restore state
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The checksum property
    checksum: Optional[str] = None
    # The gpu property
    gpu: Optional[str] = None
    # The id property
    id: Optional[UUID] = None
    # The name property
    name: Optional[str] = None
    # The status property
    status: Optional[SlurmCheckpointStatus] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmCheckpoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmCheckpoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmCheckpoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .slurm_checkpoint_status import SlurmCheckpointStatus

        from .slurm_checkpoint_status import SlurmCheckpointStatus

        fields: dict[str, Callable[[Any], None]] = {
            "checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "gpu": lambda n : setattr(self, 'gpu', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(SlurmCheckpointStatus)),
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
        writer.write_str_value("checksum", self.checksum)
        writer.write_str_value("gpu", self.gpu)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_enum_value("status", self.status)
        writer.write_additional_data_value(self.additional_data)
    

