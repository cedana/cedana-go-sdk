from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JobPolicyStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The job_ids property
    job_ids: Optional[list[str]] = None
    # The job_status property
    job_status: Optional[str] = None
    # The last_updated property
    last_updated: Optional[str] = None
    # The pod_count property
    pod_count: Optional[int] = None
    # The policy_id property
    policy_id: Optional[str] = None
    # The tracked_pods property
    tracked_pods: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JobPolicyStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JobPolicyStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JobPolicyStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "job_ids": lambda n : setattr(self, 'job_ids', n.get_collection_of_primitive_values(str)),
            "job_status": lambda n : setattr(self, 'job_status', n.get_str_value()),
            "last_updated": lambda n : setattr(self, 'last_updated', n.get_str_value()),
            "pod_count": lambda n : setattr(self, 'pod_count', n.get_int_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "tracked_pods": lambda n : setattr(self, 'tracked_pods', n.get_collection_of_primitive_values(str)),
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
        writer.write_collection_of_primitive_values("job_ids", self.job_ids)
        writer.write_str_value("job_status", self.job_status)
        writer.write_str_value("last_updated", self.last_updated)
        writer.write_int_value("pod_count", self.pod_count)
        writer.write_str_value("policy_id", self.policy_id)
        writer.write_collection_of_primitive_values("tracked_pods", self.tracked_pods)
        writer.write_additional_data_value(self.additional_data)
    

