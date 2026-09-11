from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .startup_latency_summary import StartupLatencySummary

@dataclass
class StartupComparison(AdditionalDataHolder, Parsable):
    """
    Cold-start versus Cedana-restore startup latency for a deployment.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cold property
    cold: Optional[StartupLatencySummary] = None
    # Milliseconds saved by restore at p50.
    p50_saved_ms: Optional[int] = None
    # Cold p50 divided by restore p50. Values above 1 mean restore is faster.
    p50_speedup: Optional[float] = None
    # The restore property
    restore: Optional[StartupLatencySummary] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StartupComparison:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StartupComparison
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StartupComparison()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .startup_latency_summary import StartupLatencySummary

        from .startup_latency_summary import StartupLatencySummary

        fields: dict[str, Callable[[Any], None]] = {
            "cold": lambda n : setattr(self, 'cold', n.get_object_value(StartupLatencySummary)),
            "p50_saved_ms": lambda n : setattr(self, 'p50_saved_ms', n.get_int_value()),
            "p50_speedup": lambda n : setattr(self, 'p50_speedup', n.get_float_value()),
            "restore": lambda n : setattr(self, 'restore', n.get_object_value(StartupLatencySummary)),
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
        writer.write_object_value("cold", self.cold)
        writer.write_int_value("p50_saved_ms", self.p50_saved_ms)
        writer.write_float_value("p50_speedup", self.p50_speedup)
        writer.write_object_value("restore", self.restore)
        writer.write_additional_data_value(self.additional_data)
    

