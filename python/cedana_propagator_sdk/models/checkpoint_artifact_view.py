from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .artifact_residency import ArtifactResidency

@dataclass
class CheckpointArtifactView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The artifact_id property
    artifact_id: Optional[str] = None
    # The checkpoint_mode property
    checkpoint_mode: Optional[str] = None
    # The checksum property
    checksum: Optional[str] = None
    # The compatibility_key property
    compatibility_key: Optional[str] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The exact_model property
    exact_model: Optional[str] = None
    # The hosting_mode property
    hosting_mode: Optional[str] = None
    # When a worker last became ready from this artefact.
    last_restored_at: Optional[datetime.datetime] = None
    # The logical_bytes property
    logical_bytes: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # Worker pods started from this artefact, ready or not. The gap againstobserved_restores is the interesting part.
    observed_restore_attempts: Optional[int] = None
    # Worker pods started from this artefact that went on to serve. Counted from thepods that ran, so it answers how many times the checkpoint was actually used.
    observed_restores: Optional[int] = None
    # The parent_artifact_id property
    parent_artifact_id: Optional[str] = None
    # The physical_bytes property
    physical_bytes: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The residency property
    residency: Optional[ArtifactResidency] = None
    # Unmaintained; do not display. Only restore_count_increment on the artifact PATCHwrites it, and no caller sends that. Use observed_restores.
    restore_count: Optional[int] = None
    # The reused_bytes property
    reused_bytes: Optional[int] = None
    # The source property
    source: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The storage_tier property
    storage_tier: Optional[str] = None
    # The updated_at property
    updated_at: Optional[datetime.datetime] = None
    # The uri property
    uri: Optional[str] = None
    # The written_bytes property
    written_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointArtifactView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointArtifactView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointArtifactView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .artifact_residency import ArtifactResidency

        from .artifact_residency import ArtifactResidency

        fields: dict[str, Callable[[Any], None]] = {
            "artifact_id": lambda n : setattr(self, 'artifact_id', n.get_str_value()),
            "checkpoint_mode": lambda n : setattr(self, 'checkpoint_mode', n.get_str_value()),
            "checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "compatibility_key": lambda n : setattr(self, 'compatibility_key', n.get_str_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "exact_model": lambda n : setattr(self, 'exact_model', n.get_str_value()),
            "hosting_mode": lambda n : setattr(self, 'hosting_mode', n.get_str_value()),
            "last_restored_at": lambda n : setattr(self, 'last_restored_at', n.get_datetime_value()),
            "logical_bytes": lambda n : setattr(self, 'logical_bytes', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "observed_restore_attempts": lambda n : setattr(self, 'observed_restore_attempts', n.get_int_value()),
            "observed_restores": lambda n : setattr(self, 'observed_restores', n.get_int_value()),
            "parent_artifact_id": lambda n : setattr(self, 'parent_artifact_id', n.get_str_value()),
            "physical_bytes": lambda n : setattr(self, 'physical_bytes', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "residency": lambda n : setattr(self, 'residency', n.get_object_value(ArtifactResidency)),
            "restore_count": lambda n : setattr(self, 'restore_count', n.get_int_value()),
            "reused_bytes": lambda n : setattr(self, 'reused_bytes', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "storage_tier": lambda n : setattr(self, 'storage_tier', n.get_str_value()),
            "updated_at": lambda n : setattr(self, 'updated_at', n.get_datetime_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
            "written_bytes": lambda n : setattr(self, 'written_bytes', n.get_int_value()),
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
        writer.write_str_value("artifact_id", self.artifact_id)
        writer.write_str_value("checkpoint_mode", self.checkpoint_mode)
        writer.write_str_value("checksum", self.checksum)
        writer.write_str_value("compatibility_key", self.compatibility_key)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("exact_model", self.exact_model)
        writer.write_str_value("hosting_mode", self.hosting_mode)
        writer.write_datetime_value("last_restored_at", self.last_restored_at)
        writer.write_int_value("logical_bytes", self.logical_bytes)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_int_value("observed_restore_attempts", self.observed_restore_attempts)
        writer.write_int_value("observed_restores", self.observed_restores)
        writer.write_str_value("parent_artifact_id", self.parent_artifact_id)
        writer.write_int_value("physical_bytes", self.physical_bytes)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_object_value("residency", self.residency)
        writer.write_int_value("restore_count", self.restore_count)
        writer.write_int_value("reused_bytes", self.reused_bytes)
        writer.write_str_value("source", self.source)
        writer.write_str_value("status", self.status)
        writer.write_str_value("storage_tier", self.storage_tier)
        writer.write_datetime_value("updated_at", self.updated_at)
        writer.write_str_value("uri", self.uri)
        writer.write_int_value("written_bytes", self.written_bytes)
        writer.write_additional_data_value(self.additional_data)
    

