from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class InferenceKeyView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The budget_usd property
    budget_usd: Optional[float] = None
    # The created_at property
    created_at: Optional[datetime.datetime] = None
    # The key_id property
    key_id: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The rate_limit_rps property
    rate_limit_rps: Optional[int] = None
    # The revoked_at property
    revoked_at: Optional[datetime.datetime] = None
    # The tenant_id property
    tenant_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InferenceKeyView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceKeyView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InferenceKeyView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "budget_usd": lambda n : setattr(self, 'budget_usd', n.get_float_value()),
            "created_at": lambda n : setattr(self, 'created_at', n.get_datetime_value()),
            "key_id": lambda n : setattr(self, 'key_id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "rate_limit_rps": lambda n : setattr(self, 'rate_limit_rps', n.get_int_value()),
            "revoked_at": lambda n : setattr(self, 'revoked_at', n.get_datetime_value()),
            "tenant_id": lambda n : setattr(self, 'tenant_id', n.get_str_value()),
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
        writer.write_float_value("budget_usd", self.budget_usd)
        writer.write_datetime_value("created_at", self.created_at)
        writer.write_str_value("key_id", self.key_id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("rate_limit_rps", self.rate_limit_rps)
        writer.write_datetime_value("revoked_at", self.revoked_at)
        writer.write_str_value("tenant_id", self.tenant_id)
        writer.write_additional_data_value(self.additional_data)
    

