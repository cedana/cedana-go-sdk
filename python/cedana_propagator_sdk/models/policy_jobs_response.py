from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_job_info import PolicyJobInfo

@dataclass
class PolicyJobsResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The affected_jobs property
    affected_jobs: Optional[list[PolicyJobInfo]] = None
    # The count property
    count: Optional[int] = None
    # The policy_id property
    policy_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PolicyJobsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PolicyJobsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PolicyJobsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_job_info import PolicyJobInfo

        from .policy_job_info import PolicyJobInfo

        fields: dict[str, Callable[[Any], None]] = {
            "affected_jobs": lambda n : setattr(self, 'affected_jobs', n.get_collection_of_object_values(PolicyJobInfo)),
            "count": lambda n : setattr(self, 'count', n.get_int_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
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
        writer.write_collection_of_object_values("affected_jobs", self.affected_jobs)
        writer.write_int_value("count", self.count)
        writer.write_str_value("policy_id", self.policy_id)
        writer.write_additional_data_value(self.additional_data)
    

