from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cost_leg import CostLeg
    from .cost_quality import CostQuality

@dataclass
class CostReport(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The baseline property
    baseline: Optional[CostLeg] = None
    # The hours property
    hours: Optional[int] = None
    # The node_seconds_saved property
    node_seconds_saved: Optional[float] = None
    # The savings_pct property
    savings_pct: Optional[float] = None
    # The savings_usd property
    savings_usd: Optional[float] = None
    # The treatment property
    treatment: Optional[CostLeg] = None
    # The treatment_escalation_rate property
    treatment_escalation_rate: Optional[float] = None
    # The treatment_idle_time_s property
    treatment_idle_time_s: Optional[float] = None
    # The treatment_quality property
    treatment_quality: Optional[CostQuality] = None
    # The treatment_release_latency_ms property
    treatment_release_latency_ms: Optional[float] = None
    # The variance property
    variance: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CostReport:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CostReport
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CostReport()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .cost_leg import CostLeg
        from .cost_quality import CostQuality

        from .cost_leg import CostLeg
        from .cost_quality import CostQuality

        fields: dict[str, Callable[[Any], None]] = {
            "baseline": lambda n : setattr(self, 'baseline', n.get_object_value(CostLeg)),
            "hours": lambda n : setattr(self, 'hours', n.get_int_value()),
            "node_seconds_saved": lambda n : setattr(self, 'node_seconds_saved', n.get_float_value()),
            "savings_pct": lambda n : setattr(self, 'savings_pct', n.get_float_value()),
            "savings_usd": lambda n : setattr(self, 'savings_usd', n.get_float_value()),
            "treatment": lambda n : setattr(self, 'treatment', n.get_object_value(CostLeg)),
            "treatment_escalation_rate": lambda n : setattr(self, 'treatment_escalation_rate', n.get_float_value()),
            "treatment_idle_time_s": lambda n : setattr(self, 'treatment_idle_time_s', n.get_float_value()),
            "treatment_quality": lambda n : setattr(self, 'treatment_quality', n.get_object_value(CostQuality)),
            "treatment_release_latency_ms": lambda n : setattr(self, 'treatment_release_latency_ms', n.get_float_value()),
            "variance": lambda n : setattr(self, 'variance', n.get_str_value()),
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
        writer.write_object_value("baseline", self.baseline)
        writer.write_int_value("hours", self.hours)
        writer.write_float_value("node_seconds_saved", self.node_seconds_saved)
        writer.write_float_value("savings_pct", self.savings_pct)
        writer.write_float_value("savings_usd", self.savings_usd)
        writer.write_object_value("treatment", self.treatment)
        writer.write_float_value("treatment_escalation_rate", self.treatment_escalation_rate)
        writer.write_float_value("treatment_idle_time_s", self.treatment_idle_time_s)
        writer.write_object_value("treatment_quality", self.treatment_quality)
        writer.write_float_value("treatment_release_latency_ms", self.treatment_release_latency_ms)
        writer.write_str_value("variance", self.variance)
        writer.write_additional_data_value(self.additional_data)
    

