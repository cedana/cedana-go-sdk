from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dynamo_checkpoint_summary_pods import DynamoCheckpointSummary_pods

@dataclass
class DynamoCheckpointSummary(AdditionalDataHolder, Parsable):
    """
    A lightweight summary of checkpoints taken for a Dynamo deployment's workers.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # True if at least one checkpoint with status='ready' exists
    has_cache: Optional[bool] = None
    # Timestamp of the most recent checkpoint
    latest: Optional[datetime.datetime] = None
    # Per-pod breakdown: pod_name → checkpoint count
    pods: Optional[DynamoCheckpointSummary_pods] = None
    # Total number of ready checkpoints across all worker pods
    total: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamoCheckpointSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamoCheckpointSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamoCheckpointSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dynamo_checkpoint_summary_pods import DynamoCheckpointSummary_pods

        from .dynamo_checkpoint_summary_pods import DynamoCheckpointSummary_pods

        fields: dict[str, Callable[[Any], None]] = {
            "has_cache": lambda n : setattr(self, 'has_cache', n.get_bool_value()),
            "latest": lambda n : setattr(self, 'latest', n.get_datetime_value()),
            "pods": lambda n : setattr(self, 'pods', n.get_object_value(DynamoCheckpointSummary_pods)),
            "total": lambda n : setattr(self, 'total', n.get_int_value()),
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
        writer.write_bool_value("has_cache", self.has_cache)
        writer.write_datetime_value("latest", self.latest)
        writer.write_object_value("pods", self.pods)
        writer.write_int_value("total", self.total)
        writer.write_additional_data_value(self.additional_data)
    

