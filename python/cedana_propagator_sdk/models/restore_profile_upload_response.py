from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

@dataclass
class RestoreProfileUploadResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The profile_object_path property
    profile_object_path: Optional[str] = None
    # The restore_uuid property
    restore_uuid: Optional[UUID] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RestoreProfileUploadResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RestoreProfileUploadResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RestoreProfileUploadResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "profile_object_path": lambda n : setattr(self, 'profile_object_path', n.get_str_value()),
            "restore_uuid": lambda n : setattr(self, 'restore_uuid', n.get_uuid_value()),
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
        writer.write_str_value("profile_object_path", self.profile_object_path)
        writer.write_uuid_value("restore_uuid", self.restore_uuid)
        writer.write_additional_data_value(self.additional_data)
    

