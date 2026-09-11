from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job_priorities_response_priority_counts import JobPrioritiesResponse_priority_counts

@dataclass
class JobPrioritiesResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The priorities property
    priorities: Optional[list[int]] = None
    # The priority_counts property
    priority_counts: Optional[JobPrioritiesResponse_priority_counts] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPrioritiesResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPrioritiesResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPrioritiesResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .job_priorities_response_priority_counts import JobPrioritiesResponse_priority_counts

        from .job_priorities_response_priority_counts import JobPrioritiesResponse_priority_counts

        fields: dict[str, Callable[[Any], None]] = {
            "priorities": lambda n : setattr(self, 'priorities', n.get_collection_of_primitive_values(int)),
            "priority_counts": lambda n : setattr(self, 'priority_counts', n.get_object_value(JobPrioritiesResponse_priority_counts)),
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
        writer.write_collection_of_primitive_values("priorities", self.priorities)
        writer.write_object_value("priority_counts", self.priority_counts)
        writer.write_additional_data_value(self.additional_data)
    

