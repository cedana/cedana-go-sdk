from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RegisterArtifact(AdditionalDataHolder, Parsable):
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
    # The logical_bytes property
    logical_bytes: Optional[int] = None
    # The parent_artifact_id property
    parent_artifact_id: Optional[str] = None
    # The physical_bytes property
    physical_bytes: Optional[int] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The reused_bytes property
    reused_bytes: Optional[int] = None
    # The source property
    source: Optional[str] = None
    # The storage_tier property
    storage_tier: Optional[str] = None
    # The uri property
    uri: Optional[str] = None
    # The written_bytes property
    written_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RegisterArtifact:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RegisterArtifact
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RegisterArtifact()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "artifact_id": lambda n : setattr(self, 'artifact_id', n.get_str_value()),
            "checkpoint_mode": lambda n : setattr(self, 'checkpoint_mode', n.get_str_value()),
            "checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "compatibility_key": lambda n : setattr(self, 'compatibility_key', n.get_str_value()),
            "logical_bytes": lambda n : setattr(self, 'logical_bytes', n.get_int_value()),
            "parent_artifact_id": lambda n : setattr(self, 'parent_artifact_id', n.get_str_value()),
            "physical_bytes": lambda n : setattr(self, 'physical_bytes', n.get_int_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "reused_bytes": lambda n : setattr(self, 'reused_bytes', n.get_int_value()),
            "source": lambda n : setattr(self, 'source', n.get_str_value()),
            "storage_tier": lambda n : setattr(self, 'storage_tier', n.get_str_value()),
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
        writer.write_int_value("logical_bytes", self.logical_bytes)
        writer.write_str_value("parent_artifact_id", self.parent_artifact_id)
        writer.write_int_value("physical_bytes", self.physical_bytes)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("reused_bytes", self.reused_bytes)
        writer.write_str_value("source", self.source)
        writer.write_str_value("storage_tier", self.storage_tier)
        writer.write_str_value("uri", self.uri)
        writer.write_int_value("written_bytes", self.written_bytes)
        writer.write_additional_data_value(self.additional_data)
    

