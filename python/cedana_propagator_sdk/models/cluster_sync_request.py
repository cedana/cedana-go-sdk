from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .k8s_resource import K8sResource

@dataclass
class ClusterSyncRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # A Kubernetes resource tagged by "type", with the resource's raw JSON fields alongside the tag
    resource: Optional[K8sResource] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ClusterSyncRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ClusterSyncRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ClusterSyncRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .k8s_resource import K8sResource

        from .k8s_resource import K8sResource

        fields: dict[str, Callable[[Any], None]] = {
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "resource": lambda n : setattr(self, 'resource', n.get_object_value(K8sResource)),
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
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_object_value("resource", self.resource)
        writer.write_additional_data_value(self.additional_data)
    

