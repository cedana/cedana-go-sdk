from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AuthorizeRequest(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The estimated_prompt_tokens property
    estimated_prompt_tokens: Optional[int] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The request_id property
    request_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AuthorizeRequest:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AuthorizeRequest
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AuthorizeRequest()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "estimated_prompt_tokens": lambda n : setattr(self, 'estimated_prompt_tokens', n.get_int_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "request_id": lambda n : setattr(self, 'request_id', n.get_str_value()),
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
        writer.write_int_value("estimated_prompt_tokens", self.estimated_prompt_tokens)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("request_id", self.request_id)
        writer.write_additional_data_value(self.additional_data)
    

