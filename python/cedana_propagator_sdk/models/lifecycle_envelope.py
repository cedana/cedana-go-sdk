from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class LifecycleEnvelope(AdditionalDataHolder, Parsable):
    """
    Shared envelope for trusted lifecycle events.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Checkpoint/restore action UUID when the event belongs to one.
    action_id: Optional[UUID] = None
    # Model activation row UUID when applicable.
    activation_id: Optional[UUID] = None
    # Checkpoint artifact UUID for checkpoint events.
    artifact_id: Optional[UUID] = None
    # The boot_id property
    boot_id: Optional[str] = None
    # Nebius cluster (`clusters.id` UUID).
    cluster_id: Optional[UUID] = None
    # Idempotency key: generated once per logical event and reused acrosstransport retries (RabbitMQ redelivery, HTTP retry).
    event_id: Optional[UUID] = None
    # Activation observed generation.
    generation: Optional[int] = None
    # One of SUPPORTED_LIFECYCLE_KINDS.
    kind: Optional[str] = None
    # Node the event came from (checkpoint tmpfs artifacts are boot-tied).
    node_uid: Optional[UUID] = None
    # When the event happened at the source (RFC3339 UTC).
    occurred_at: Optional[datetime.datetime] = None
    # Deployment profile id (e.g. `qwen3-30b-a3b-l40s-fp8`).
    profile_id: Optional[str] = None
    # MUST be 1; anything else is dead-lettered on ingestion.
    schema_version: Optional[int] = None
    # Per-(cluster_id, activation_id) monotonic counter; 0 when not applicable.
    sequence: Optional[int] = None
    # k8s pod/DGD UID when relevant.
    workload_uid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LifecycleEnvelope:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LifecycleEnvelope
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LifecycleEnvelope()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_uuid_value()),
            "activation_id": lambda n : setattr(self, 'activation_id', n.get_uuid_value()),
            "artifact_id": lambda n : setattr(self, 'artifact_id', n.get_uuid_value()),
            "boot_id": lambda n : setattr(self, 'boot_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_uuid_value()),
            "event_id": lambda n : setattr(self, 'event_id', n.get_uuid_value()),
            "generation": lambda n : setattr(self, 'generation', n.get_int_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_str_value()),
            "node_uid": lambda n : setattr(self, 'node_uid', n.get_uuid_value()),
            "occurred_at": lambda n : setattr(self, 'occurred_at', n.get_datetime_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "schema_version": lambda n : setattr(self, 'schema_version', n.get_int_value()),
            "sequence": lambda n : setattr(self, 'sequence', n.get_int_value()),
            "workload_uid": lambda n : setattr(self, 'workload_uid', n.get_str_value()),
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
        writer.write_uuid_value("action_id", self.action_id)
        writer.write_uuid_value("activation_id", self.activation_id)
        writer.write_uuid_value("artifact_id", self.artifact_id)
        writer.write_str_value("boot_id", self.boot_id)
        writer.write_uuid_value("cluster_id", self.cluster_id)
        writer.write_uuid_value("event_id", self.event_id)
        writer.write_int_value("generation", self.generation)
        writer.write_str_value("kind", self.kind)
        writer.write_uuid_value("node_uid", self.node_uid)
        writer.write_datetime_value("occurred_at", self.occurred_at)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("schema_version", self.schema_version)
        writer.write_int_value("sequence", self.sequence)
        writer.write_str_value("workload_uid", self.workload_uid)
        writer.write_additional_data_value(self.additional_data)
    

