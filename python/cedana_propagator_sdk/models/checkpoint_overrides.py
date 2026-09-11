from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CheckpointOverrides(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The asynchronous property
    asynchronous: Optional[bool] = None
    # The compression property
    compression: Optional[str] = None
    # The criu_opts property
    criu_opts: Optional[str] = None
    # The directory property
    directory: Optional[str] = None
    # GPU delta (incremental) checkpoint; None = cluster default
    incremental: Optional[bool] = None
    # The streams property
    streams: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointOverrides:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointOverrides
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointOverrides()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "asynchronous": lambda n : setattr(self, 'asynchronous', n.get_bool_value()),
            "compression": lambda n : setattr(self, 'compression', n.get_str_value()),
            "criu_opts": lambda n : setattr(self, 'criu_opts', n.get_str_value()),
            "directory": lambda n : setattr(self, 'directory', n.get_str_value()),
            "incremental": lambda n : setattr(self, 'incremental', n.get_bool_value()),
            "streams": lambda n : setattr(self, 'streams', n.get_int_value()),
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
        writer.write_bool_value("asynchronous", self.asynchronous)
        writer.write_str_value("compression", self.compression)
        writer.write_str_value("criu_opts", self.criu_opts)
        writer.write_str_value("directory", self.directory)
        writer.write_bool_value("incremental", self.incremental)
        writer.write_int_value("streams", self.streams)
        writer.write_additional_data_value(self.additional_data)
    

