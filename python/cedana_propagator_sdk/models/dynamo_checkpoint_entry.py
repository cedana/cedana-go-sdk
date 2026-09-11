from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DynamoCheckpointEntry(AdditionalDataHolder, Parsable):
    """
    One CEDANA_CHECKPOINT "slot" in the library. A name can have many individualcheckpoints over time (you can checkpoint the same env value repeatedly); thisaggregates them into a single slot row.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Number of (non-deprecated) checkpoints captured under this name
    checkpoint_count: Optional[int] = None
    # Timestamp of the most recent checkpoint under this name
    created_at: Optional[datetime.datetime] = None
    # Deployment whose CEDANA_CHECKPOINT env equals this checkpoint's name, if any.
    deployment_name: Optional[str] = None
    # Model served by that deployment (drives the model logo + "deploy from").
    model: Optional[str] = None
    # CEDANA_CHECKPOINT name (the stable restore key)
    name: Optional[str] = None
    # True if at least one checkpoint under this name is ready + restorable
    restorable: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamoCheckpointEntry:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamoCheckpointEntry
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamoCheckpointEntry()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_count": lambda n : setattr(self, 'checkpoint_count', n.get_int_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "deployment_name": lambda n : setattr(self, 'deployment_name', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "restorable": lambda n : setattr(self, 'restorable', n.get_bool_value()),
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
        writer.write_int_value("checkpoint_count", self.checkpoint_count)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("deployment_name", self.deployment_name)
        writer.write_str_value("model", self.model)
        writer.write_str_value("name", self.name)
        writer.write_bool_value("restorable", self.restorable)
        writer.write_additional_data_value(self.additional_data)
    

