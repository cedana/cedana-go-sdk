from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .plugin_binary import PluginBinary
    from .plugin_type import PluginType
    from .status import Status

@dataclass
class Plugin(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The binaries property
    binaries: Optional[list[PluginBinary]] = None
    # The latest_version property
    latest_version: Optional[str] = None
    # The libraries property
    libraries: Optional[list[PluginBinary]] = None
    # The name property
    name: Optional[str] = None
    # The published_at property
    published_at: Optional[datetime.datetime] = None
    # The size property
    size: Optional[int] = None
    # The status property
    status: Optional[Status] = None
    # The type property
    type: Optional[PluginType] = None
    # The version property
    version: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Plugin:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Plugin
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Plugin()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .plugin_binary import PluginBinary
        from .plugin_type import PluginType
        from .status import Status

        from .plugin_binary import PluginBinary
        from .plugin_type import PluginType
        from .status import Status

        fields: dict[str, Callable[[Any], None]] = {
            "binaries": lambda n : setattr(self, 'binaries', n.get_collection_of_object_values(PluginBinary)),
            "latest_version": lambda n : setattr(self, 'latest_version', n.get_str_value()),
            "libraries": lambda n : setattr(self, 'libraries', n.get_collection_of_object_values(PluginBinary)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "published_at": lambda n : setattr(self, 'published_at', n.get_datetime_value()),
            "size": lambda n : setattr(self, 'size', n.get_int_value()),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Status)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PluginType)),
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
        writer.write_collection_of_object_values("binaries", self.binaries)
        writer.write_str_value("latest_version", self.latest_version)
        writer.write_collection_of_object_values("libraries", self.libraries)
        writer.write_str_value("name", self.name)
        writer.write_datetime_value("published_at", self.published_at)
        writer.write_int_value("size", self.size)
        writer.write_enum_value("status", self.status)
        writer.write_enum_value("type", self.type)
        writer.write_str_value("version", self.version)
        writer.write_additional_data_value(self.additional_data)
    

