from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .metric_sample import MetricSample

@dataclass
class MetricsBatch(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The samples property
    samples: Optional[list[MetricSample]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MetricsBatch:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MetricsBatch
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MetricsBatch()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .metric_sample import MetricSample

        from .metric_sample import MetricSample

        fields: dict[str, Callable[[Any], None]] = {
            "samples": lambda n : setattr(self, 'samples', n.get_collection_of_object_values(MetricSample)),
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
        writer.write_collection_of_object_values("samples", self.samples)
        writer.write_additional_data_value(self.additional_data)
    

