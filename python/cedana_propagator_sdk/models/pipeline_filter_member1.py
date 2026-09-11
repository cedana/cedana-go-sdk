from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .namespace_filter_config import NamespaceFilterConfig
    from .pipeline_filter_member1_type import PipelineFilterMember1_type

@dataclass
class PipelineFilterMember1(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The config property
    config: Optional[NamespaceFilterConfig] = None
    # The type property
    type: Optional[PipelineFilterMember1_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineFilterMember1:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineFilterMember1
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PipelineFilterMember1()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .namespace_filter_config import NamespaceFilterConfig
        from .pipeline_filter_member1_type import PipelineFilterMember1_type

        from .namespace_filter_config import NamespaceFilterConfig
        from .pipeline_filter_member1_type import PipelineFilterMember1_type

        fields: dict[str, Callable[[Any], None]] = {
            "config": lambda n : setattr(self, 'config', n.get_object_value(NamespaceFilterConfig)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PipelineFilterMember1_type)),
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
        writer.write_object_value("config", self.config)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

