from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CostConfigUpsert(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The node_hourly_usd property
    node_hourly_usd: Optional[float] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The storage_gb_hour_usd property
    storage_gb_hour_usd: Optional[float] = None
    # The transfer_gb_usd property
    transfer_gb_usd: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostConfigUpsert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostConfigUpsert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostConfigUpsert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "node_hourly_usd": lambda n : setattr(self, 'node_hourly_usd', n.get_float_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "storage_gb_hour_usd": lambda n : setattr(self, 'storage_gb_hour_usd', n.get_float_value()),
            "transfer_gb_usd": lambda n : setattr(self, 'transfer_gb_usd', n.get_float_value()),
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
        writer.write_float_value("node_hourly_usd", self.node_hourly_usd)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_float_value("storage_gb_hour_usd", self.storage_gb_hour_usd)
        writer.write_float_value("transfer_gb_usd", self.transfer_gb_usd)
        writer.write_additional_data_value(self.additional_data)
    

