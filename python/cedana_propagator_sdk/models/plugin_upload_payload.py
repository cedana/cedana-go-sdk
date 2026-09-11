from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PluginUploadPayload(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The arch property
    arch: Optional[str] = None
    # The build property
    build: Optional[str] = None
    # The checksum property
    checksum: Optional[str] = None
    # The repository property
    repository: Optional[str] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PluginUploadPayload:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PluginUploadPayload
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PluginUploadPayload()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "arch": lambda n : setattr(self, 'arch', n.get_str_value()),
            "build": lambda n : setattr(self, 'build', n.get_str_value()),
            "checksum": lambda n : setattr(self, 'checksum', n.get_str_value()),
            "repository": lambda n : setattr(self, 'repository', n.get_str_value()),
            "version": lambda n : setattr(self, 'version', n.get_str_value()),
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
        writer.write_str_value("arch", self.arch)
        writer.write_str_value("build", self.build)
        writer.write_str_value("checksum", self.checksum)
        writer.write_str_value("repository", self.repository)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

