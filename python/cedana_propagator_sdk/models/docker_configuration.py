from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .environment_variable import EnvironmentVariable
    from .port_mapping import PortMapping
    from .registry_credentials import RegistryCredentials
    from .volume_mapping import VolumeMapping

@dataclass
class DockerConfiguration(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The args property
    args: Optional[str] = None
    # The envs property
    envs: Optional[list[EnvironmentVariable]] = None
    # The image property
    image: Optional[str] = None
    # The port_mappings property
    port_mappings: Optional[list[PortMapping]] = None
    # The registry_credentials property
    registry_credentials: Optional[RegistryCredentials] = None
    # The shared_memory_in_gb property
    shared_memory_in_gb: Optional[int] = None
    # The volume_mounts property
    volume_mounts: Optional[list[VolumeMapping]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DockerConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DockerConfiguration
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DockerConfiguration()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .environment_variable import EnvironmentVariable
        from .port_mapping import PortMapping
        from .registry_credentials import RegistryCredentials
        from .volume_mapping import VolumeMapping

        from .environment_variable import EnvironmentVariable
        from .port_mapping import PortMapping
        from .registry_credentials import RegistryCredentials
        from .volume_mapping import VolumeMapping

        fields: dict[str, Callable[[Any], None]] = {
            "args": lambda n : setattr(self, 'args', n.get_str_value()),
            "envs": lambda n : setattr(self, 'envs', n.get_collection_of_object_values(EnvironmentVariable)),
            "image": lambda n : setattr(self, 'image', n.get_str_value()),
            "port_mappings": lambda n : setattr(self, 'port_mappings', n.get_collection_of_object_values(PortMapping)),
            "registry_credentials": lambda n : setattr(self, 'registry_credentials', n.get_object_value(RegistryCredentials)),
            "shared_memory_in_gb": lambda n : setattr(self, 'shared_memory_in_gb', n.get_int_value()),
            "volume_mounts": lambda n : setattr(self, 'volume_mounts', n.get_collection_of_object_values(VolumeMapping)),
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
        writer.write_str_value("args", self.args)
        writer.write_collection_of_object_values("envs", self.envs)
        writer.write_str_value("image", self.image)
        writer.write_collection_of_object_values("port_mappings", self.port_mappings)
        writer.write_object_value("registry_credentials", self.registry_credentials)
        writer.write_int_value("shared_memory_in_gb", self.shared_memory_in_gb)
        writer.write_collection_of_object_values("volume_mounts", self.volume_mounts)
        writer.write_additional_data_value(self.additional_data)
    

