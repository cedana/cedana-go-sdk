from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StorageTierSummary(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The artifacts property
    artifacts: Optional[int] = None
    # The bytes property
    bytes: Optional[int] = None
    # The residency_hours property
    residency_hours: Optional[float] = None
    # The tier property
    tier: Optional[str] = None
    # The transfers property
    transfers: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StorageTierSummary:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StorageTierSummary
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StorageTierSummary()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "artifacts": lambda n : setattr(self, 'artifacts', n.get_int_value()),
            "bytes": lambda n : setattr(self, 'bytes', n.get_int_value()),
            "residency_hours": lambda n : setattr(self, 'residency_hours', n.get_float_value()),
            "tier": lambda n : setattr(self, 'tier', n.get_str_value()),
            "transfers": lambda n : setattr(self, 'transfers', n.get_int_value()),
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
        writer.write_int_value("artifacts", self.artifacts)
        writer.write_int_value("bytes", self.bytes)
        writer.write_float_value("residency_hours", self.residency_hours)
        writer.write_str_value("tier", self.tier)
        writer.write_int_value("transfers", self.transfers)
        writer.write_additional_data_value(self.additional_data)
    

