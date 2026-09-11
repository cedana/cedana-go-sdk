from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import ComposedTypeWrapper, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pipeline_filter_member1 import PipelineFilterMember1
    from .pipeline_filter_member2 import PipelineFilterMember2
    from .pipeline_filter_member3 import PipelineFilterMember3
    from .pipeline_filter_member4 import PipelineFilterMember4

@dataclass
class PipelineFilter(ComposedTypeWrapper, Parsable):
    """
    Composed type wrapper for classes PipelineFilterMember1, PipelineFilterMember2, PipelineFilterMember3, PipelineFilterMember4
    """
    # Composed type representation for type PipelineFilterMember1
    pipeline_filter_member1: Optional[PipelineFilterMember1] = None
    # Composed type representation for type PipelineFilterMember2
    pipeline_filter_member2: Optional[PipelineFilterMember2] = None
    # Composed type representation for type PipelineFilterMember3
    pipeline_filter_member3: Optional[PipelineFilterMember3] = None
    # Composed type representation for type PipelineFilterMember4
    pipeline_filter_member4: Optional[PipelineFilterMember4] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineFilter:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineFilter
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        try:
            child_node = parse_node.get_child_node("")
            mapping_value = child_node.get_str_value() if child_node else None
        except AttributeError:
            mapping_value = None
        result = PipelineFilter()
        return result
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pipeline_filter_member1 import PipelineFilterMember1
        from .pipeline_filter_member2 import PipelineFilterMember2
        from .pipeline_filter_member3 import PipelineFilterMember3
        from .pipeline_filter_member4 import PipelineFilterMember4

        if self.pipeline_filter_member1:
            return self.pipeline_filter_member1.get_field_deserializers()
        if self.pipeline_filter_member2:
            return self.pipeline_filter_member2.get_field_deserializers()
        if self.pipeline_filter_member3:
            return self.pipeline_filter_member3.get_field_deserializers()
        if self.pipeline_filter_member4:
            return self.pipeline_filter_member4.get_field_deserializers()
        return {}
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        if self.pipeline_filter_member1:
            writer.write_object_value(None, self.pipeline_filter_member1)
        elif self.pipeline_filter_member2:
            writer.write_object_value(None, self.pipeline_filter_member2)
        elif self.pipeline_filter_member3:
            writer.write_object_value(None, self.pipeline_filter_member3)
        elif self.pipeline_filter_member4:
            writer.write_object_value(None, self.pipeline_filter_member4)
    

