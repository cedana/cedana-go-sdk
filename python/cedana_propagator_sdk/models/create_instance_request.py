from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .alert import Alert
    from .auto_delete import AutoDelete
    from .environment_variable import EnvironmentVariable
    from .launch_configuration import LaunchConfiguration
    from .volume_mount import VolumeMount

@dataclass
class CreateInstanceRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The alert property
    alert: Optional[Alert] = None
    # The auto_delete property
    auto_delete: Optional[AutoDelete] = None
    # The cloud property
    cloud: Optional[str] = None
    # The envs property
    envs: Optional[list[EnvironmentVariable]] = None
    # The launch_configuration property
    launch_configuration: Optional[LaunchConfiguration] = None
    # The name property
    name: Optional[str] = None
    # The os property
    os: Optional[str] = None
    # The region property
    region: Optional[str] = None
    # The shade_cloud property
    shade_cloud: Optional[bool] = None
    # The shade_instance_type property
    shade_instance_type: Optional[str] = None
    # The ssh_key_id property
    ssh_key_id: Optional[str] = None
    # The tags property
    tags: Optional[list[str]] = None
    # The template_id property
    template_id: Optional[str] = None
    # The volume_ids property
    volume_ids: Optional[list[str]] = None
    # The volume_mount property
    volume_mount: Optional[VolumeMount] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CreateInstanceRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CreateInstanceRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CreateInstanceRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .alert import Alert
        from .auto_delete import AutoDelete
        from .environment_variable import EnvironmentVariable
        from .launch_configuration import LaunchConfiguration
        from .volume_mount import VolumeMount

        from .alert import Alert
        from .auto_delete import AutoDelete
        from .environment_variable import EnvironmentVariable
        from .launch_configuration import LaunchConfiguration
        from .volume_mount import VolumeMount

        fields: dict[str, Callable[[Any], None]] = {
            "alert": lambda n : setattr(self, 'alert', n.get_object_value(Alert)),
            "auto_delete": lambda n : setattr(self, 'auto_delete', n.get_object_value(AutoDelete)),
            "cloud": lambda n : setattr(self, 'cloud', n.get_str_value()),
            "envs": lambda n : setattr(self, 'envs', n.get_collection_of_object_values(EnvironmentVariable)),
            "launch_configuration": lambda n : setattr(self, 'launch_configuration', n.get_object_value(LaunchConfiguration)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "os": lambda n : setattr(self, 'os', n.get_str_value()),
            "region": lambda n : setattr(self, 'region', n.get_str_value()),
            "shade_cloud": lambda n : setattr(self, 'shade_cloud', n.get_bool_value()),
            "shade_instance_type": lambda n : setattr(self, 'shade_instance_type', n.get_str_value()),
            "ssh_key_id": lambda n : setattr(self, 'ssh_key_id', n.get_str_value()),
            "tags": lambda n : setattr(self, 'tags', n.get_collection_of_primitive_values(str)),
            "template_id": lambda n : setattr(self, 'template_id', n.get_str_value()),
            "volume_ids": lambda n : setattr(self, 'volume_ids', n.get_collection_of_primitive_values(str)),
            "volume_mount": lambda n : setattr(self, 'volume_mount', n.get_object_value(VolumeMount)),
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
        writer.write_object_value("alert", self.alert)
        writer.write_object_value("auto_delete", self.auto_delete)
        writer.write_str_value("cloud", self.cloud)
        writer.write_collection_of_object_values("envs", self.envs)
        writer.write_object_value("launch_configuration", self.launch_configuration)
        writer.write_str_value("name", self.name)
        writer.write_str_value("os", self.os)
        writer.write_str_value("region", self.region)
        writer.write_bool_value("shade_cloud", self.shade_cloud)
        writer.write_str_value("shade_instance_type", self.shade_instance_type)
        writer.write_str_value("ssh_key_id", self.ssh_key_id)
        writer.write_collection_of_primitive_values("tags", self.tags)
        writer.write_str_value("template_id", self.template_id)
        writer.write_collection_of_primitive_values("volume_ids", self.volume_ids)
        writer.write_object_value("volume_mount", self.volume_mount)
        writer.write_additional_data_value(self.additional_data)
    

