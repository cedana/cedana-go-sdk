from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class CostSavingsEstimate(AdditionalDataHolder, Parsable):
    """
    Cost savings estimate with user-provided hourly rate
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Cost of checkpoint overhead (time spent checkpointing)
    checkpoint_overhead_cost: Optional[float] = None
    # User-provided hourly compute cost
    hourly_rate: Optional[float] = None
    # Maximum potential data loss on failure (seconds) - worst case recovery point
    max_recovery_point_seconds: Optional[float] = None
    # Estimated maximum cost saved per failure event(time_protected - max_recovery_point) * hourly_rate / 3600
    max_savings_per_failure: Optional[float] = None
    # Net potential savings = max_savings - overhead_cost
    net_potential_savings: Optional[float] = None
    # Number of pods protected
    pods_protected: Optional[int] = None
    # Total time protected by checkpoints (seconds)
    time_protected_seconds: Optional[float] = None
    # Total checkpoints taken
    total_checkpoints: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostSavingsEstimate:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostSavingsEstimate
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostSavingsEstimate()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "checkpoint_overhead_cost": lambda n : setattr(self, 'checkpoint_overhead_cost', n.get_float_value()),
            "hourly_rate": lambda n : setattr(self, 'hourly_rate', n.get_float_value()),
            "max_recovery_point_seconds": lambda n : setattr(self, 'max_recovery_point_seconds', n.get_float_value()),
            "max_savings_per_failure": lambda n : setattr(self, 'max_savings_per_failure', n.get_float_value()),
            "net_potential_savings": lambda n : setattr(self, 'net_potential_savings', n.get_float_value()),
            "pods_protected": lambda n : setattr(self, 'pods_protected', n.get_int_value()),
            "time_protected_seconds": lambda n : setattr(self, 'time_protected_seconds', n.get_float_value()),
            "total_checkpoints": lambda n : setattr(self, 'total_checkpoints', n.get_int_value()),
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
        writer.write_float_value("checkpoint_overhead_cost", self.checkpoint_overhead_cost)
        writer.write_float_value("hourly_rate", self.hourly_rate)
        writer.write_float_value("max_recovery_point_seconds", self.max_recovery_point_seconds)
        writer.write_float_value("max_savings_per_failure", self.max_savings_per_failure)
        writer.write_float_value("net_potential_savings", self.net_potential_savings)
        writer.write_int_value("pods_protected", self.pods_protected)
        writer.write_float_value("time_protected_seconds", self.time_protected_seconds)
        writer.write_int_value("total_checkpoints", self.total_checkpoints)
        writer.write_additional_data_value(self.additional_data)
    

