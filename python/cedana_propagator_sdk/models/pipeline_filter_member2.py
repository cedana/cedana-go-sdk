from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pipeline_filter_member2_type import PipelineFilterMember2_type
    from .pods_filter_config import PodsFilterConfig

@dataclass
class PipelineFilterMember2(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The config property
    config: Optional[PodsFilterConfig] = None
    # The type property
    type: Optional[PipelineFilterMember2_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineFilterMember2:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineFilterMember2
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PipelineFilterMember2()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pipeline_filter_member2_type import PipelineFilterMember2_type
        from .pods_filter_config import PodsFilterConfig

        from .pipeline_filter_member2_type import PipelineFilterMember2_type
        from .pods_filter_config import PodsFilterConfig

        fields: dict[str, Callable[[Any], None]] = {
            "config": lambda n : setattr(self, 'config', n.get_object_value(PodsFilterConfig)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PipelineFilterMember2_type)),
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
    

