from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class DynamoDeployment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The backend property
    backend: Optional[str] = None
    # The cedana_managed property
    cedana_managed: Optional[bool] = None
    # The cluster_id property
    cluster_id: Optional[UUID] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The id property
    id: Optional[UUID] = None
    # The model property
    model: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The namespace property
    namespace: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # The worker_replicas property
    worker_replicas: Optional[int] = None
    # The worker_replicas_ready property
    worker_replicas_ready: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DynamoDeployment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DynamoDeployment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DynamoDeployment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "backend": lambda n : setattr(self, 'backend', n.get_str_value()),
            "cedana_managed": lambda n : setattr(self, 'cedana_managed', n.get_bool_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_uuid_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "worker_replicas": lambda n : setattr(self, 'worker_replicas', n.get_int_value()),
            "worker_replicas_ready": lambda n : setattr(self, 'worker_replicas_ready', n.get_int_value()),
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
        writer.write_str_value("backend", self.backend)
        writer.write_bool_value("cedana_managed", self.cedana_managed)
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_uuid_value("id", self.id)
        writer.write_str_value("model", self.model)
        writer.write_str_value("name", self.name)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("status", self.status)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_int_value("worker_replicas", self.worker_replicas)
        writer.write_int_value("worker_replicas_ready", self.worker_replicas_ready)
        writer.write_additional_data_value(self.additional_data)
    

