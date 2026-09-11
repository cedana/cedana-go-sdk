from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CostBreakdownRow(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_count property
    activation_count: Optional[int] = None
    # The active_duration_s property
    active_duration_s: Optional[float] = None
    # The compute_usd property
    compute_usd: Optional[float] = None
    # The fallback_usd property
    fallback_usd: Optional[float] = None
    # The idle_time_s property
    idle_time_s: Optional[float] = None
    # The node_seconds property
    node_seconds: Optional[float] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The release_latency_ms property
    release_latency_ms: Optional[float] = None
    # The storage_usd property
    storage_usd: Optional[float] = None
    # The tokens_served property
    tokens_served: Optional[int] = None
    # The transfer_usd property
    transfer_usd: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostBreakdownRow:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostBreakdownRow
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostBreakdownRow()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "activation_count": lambda n : setattr(self, 'activation_count', n.get_int_value()),
            "active_duration_s": lambda n : setattr(self, 'active_duration_s', n.get_float_value()),
            "compute_usd": lambda n : setattr(self, 'compute_usd', n.get_float_value()),
            "fallback_usd": lambda n : setattr(self, 'fallback_usd', n.get_float_value()),
            "idle_time_s": lambda n : setattr(self, 'idle_time_s', n.get_float_value()),
            "node_seconds": lambda n : setattr(self, 'node_seconds', n.get_float_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "release_latency_ms": lambda n : setattr(self, 'release_latency_ms', n.get_float_value()),
            "storage_usd": lambda n : setattr(self, 'storage_usd', n.get_float_value()),
            "tokens_served": lambda n : setattr(self, 'tokens_served', n.get_int_value()),
            "transfer_usd": lambda n : setattr(self, 'transfer_usd', n.get_float_value()),
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
        writer.write_int_value("activation_count", self.activation_count)
        writer.write_float_value("active_duration_s", self.active_duration_s)
        writer.write_float_value("compute_usd", self.compute_usd)
        writer.write_float_value("fallback_usd", self.fallback_usd)
        writer.write_float_value("idle_time_s", self.idle_time_s)
        writer.write_float_value("node_seconds", self.node_seconds)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_float_value("release_latency_ms", self.release_latency_ms)
        writer.write_float_value("storage_usd", self.storage_usd)
        writer.write_int_value("tokens_served", self.tokens_served)
        writer.write_float_value("transfer_usd", self.transfer_usd)
        writer.write_additional_data_value(self.additional_data)
    

