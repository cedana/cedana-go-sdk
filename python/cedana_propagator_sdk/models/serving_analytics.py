from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ServingAnalytics(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The average_ttft_ms property
    average_ttft_ms: Optional[float] = None
    # The completion_tokens property
    completion_tokens: Optional[int] = None
    # The deadline_misses property
    deadline_misses: Optional[int] = None
    # The fallbacks property
    fallbacks: Optional[int] = None
    # The prompt_tokens property
    prompt_tokens: Optional[int] = None
    # The requests property
    requests: Optional[int] = None
    # The tokens_per_second property
    tokens_per_second: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ServingAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ServingAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ServingAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "average_ttft_ms": lambda n : setattr(self, 'average_ttft_ms', n.get_float_value()),
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "deadline_misses": lambda n : setattr(self, 'deadline_misses', n.get_int_value()),
            "fallbacks": lambda n : setattr(self, 'fallbacks', n.get_int_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "requests": lambda n : setattr(self, 'requests', n.get_int_value()),
            "tokens_per_second": lambda n : setattr(self, 'tokens_per_second', n.get_float_value()),
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
        writer.write_float_value("average_ttft_ms", self.average_ttft_ms)
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_int_value("deadline_misses", self.deadline_misses)
        writer.write_int_value("fallbacks", self.fallbacks)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_int_value("requests", self.requests)
        writer.write_float_value("tokens_per_second", self.tokens_per_second)
        writer.write_additional_data_value(self.additional_data)
    

