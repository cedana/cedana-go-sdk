from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SimulationResult(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cold_share property
    cold_share: Optional[float] = None
    # The evidence property
    evidence: Optional[str] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The projected_cold_p50_ms property
    projected_cold_p50_ms: Optional[float] = None
    # The projected_deadline_miss_rate property
    projected_deadline_miss_rate: Optional[float] = None
    # The projected_fallback_rate property
    projected_fallback_rate: Optional[float] = None
    # The projected_p50_ms property
    projected_p50_ms: Optional[float] = None
    # The projected_restore_p50_ms property
    projected_restore_p50_ms: Optional[float] = None
    # The requests_per_hour property
    requests_per_hour: Optional[float] = None
    # The restore_share property
    restore_share: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SimulationResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SimulationResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SimulationResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "cold_share": lambda n : setattr(self, 'cold_share', n.get_float_value()),
            "evidence": lambda n : setattr(self, 'evidence', n.get_str_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "projected_cold_p50_ms": lambda n : setattr(self, 'projected_cold_p50_ms', n.get_float_value()),
            "projected_deadline_miss_rate": lambda n : setattr(self, 'projected_deadline_miss_rate', n.get_float_value()),
            "projected_fallback_rate": lambda n : setattr(self, 'projected_fallback_rate', n.get_float_value()),
            "projected_p50_ms": lambda n : setattr(self, 'projected_p50_ms', n.get_float_value()),
            "projected_restore_p50_ms": lambda n : setattr(self, 'projected_restore_p50_ms', n.get_float_value()),
            "requests_per_hour": lambda n : setattr(self, 'requests_per_hour', n.get_float_value()),
            "restore_share": lambda n : setattr(self, 'restore_share', n.get_float_value()),
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
        writer.write_float_value("cold_share", self.cold_share)
        writer.write_str_value("evidence", self.evidence)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_float_value("projected_cold_p50_ms", self.projected_cold_p50_ms)
        writer.write_float_value("projected_deadline_miss_rate", self.projected_deadline_miss_rate)
        writer.write_float_value("projected_fallback_rate", self.projected_fallback_rate)
        writer.write_float_value("projected_p50_ms", self.projected_p50_ms)
        writer.write_float_value("projected_restore_p50_ms", self.projected_restore_p50_ms)
        writer.write_float_value("requests_per_hour", self.requests_per_hour)
        writer.write_float_value("restore_share", self.restore_share)
        writer.write_additional_data_value(self.additional_data)
    

