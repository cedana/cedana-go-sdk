from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .policy_pipeline import PolicyPipeline

@dataclass
class PipelinePolicyRequest(AdditionalDataHolder, Parsable):
    """
    Request to create a policy using the pipeline format
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name property
    name: Optional[str] = None
    # Complete policy pipeline definition
    pipeline: Optional[PolicyPipeline] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelinePolicyRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelinePolicyRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PipelinePolicyRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .policy_pipeline import PolicyPipeline

        from .policy_pipeline import PolicyPipeline

        fields: dict[str, Callable[[Any], None]] = {
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "pipeline": lambda n : setattr(self, 'pipeline', n.get_object_value(PolicyPipeline)),
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
        writer.write_str_value("name", self.name)
        writer.write_object_value("pipeline", self.pipeline)
        writer.write_additional_data_value(self.additional_data)
    

