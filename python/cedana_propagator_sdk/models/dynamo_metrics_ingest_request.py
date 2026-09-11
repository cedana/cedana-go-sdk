from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .dynamo_metric_sample import DynamoMetricSample

@dataclass
class DynamoMetricsIngestRequest(AdditionalDataHolder, Parsable):
    """
    Batch of metric samples posted by the watcher after scraping /metrics.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[str] = None
    # The model property
    model: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The samples property
    samples: Optional[list[DynamoMetricSample]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamoMetricsIngestRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamoMetricsIngestRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamoMetricsIngestRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .dynamo_metric_sample import DynamoMetricSample

        from .dynamo_metric_sample import DynamoMetricSample

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "samples": lambda n : setattr(self, 'samples', n.get_collection_of_object_values(DynamoMetricSample)),
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
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_str_value("model", self.model)
        writer.write_str_value("namespace", self.namespace)
        writer.write_collection_of_object_values("samples", self.samples)
        writer.write_additional_data_value(self.additional_data)
    

