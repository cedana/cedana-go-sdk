from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class UsageBucket(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The avg_backend_ms property
    avg_backend_ms: Optional[float] = None
    # The avg_routing_ms property
    avg_routing_ms: Optional[float] = None
    # The avg_ttft_ms property
    avg_ttft_ms: Optional[float] = None
    # The bucket property
    bucket: Optional[datetime.datetime] = None
    # The cold_start_avoided_ms property
    cold_start_avoided_ms: Optional[int] = None
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
    # The successes property
    successes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UsageBucket:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UsageBucket
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UsageBucket()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_backend_ms": lambda n : setattr(self, 'avg_backend_ms', n.get_float_value()),
            "avg_routing_ms": lambda n : setattr(self, 'avg_routing_ms', n.get_float_value()),
            "avg_ttft_ms": lambda n : setattr(self, 'avg_ttft_ms', n.get_float_value()),
            "bucket": lambda n : setattr(self, 'bucket', n.get_datetime_value()),
            "cold_start_avoided_ms": lambda n : setattr(self, 'cold_start_avoided_ms', n.get_int_value()),
            "completion_tokens": lambda n : setattr(self, 'completion_tokens', n.get_int_value()),
            "deadline_misses": lambda n : setattr(self, 'deadline_misses', n.get_int_value()),
            "fallbacks": lambda n : setattr(self, 'fallbacks', n.get_int_value()),
            "prompt_tokens": lambda n : setattr(self, 'prompt_tokens', n.get_int_value()),
            "requests": lambda n : setattr(self, 'requests', n.get_int_value()),
            "successes": lambda n : setattr(self, 'successes', n.get_int_value()),
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
        writer.write_float_value("avg_backend_ms", self.avg_backend_ms)
        writer.write_float_value("avg_routing_ms", self.avg_routing_ms)
        writer.write_float_value("avg_ttft_ms", self.avg_ttft_ms)
        writer.write_datetime_value("bucket", self.bucket)
        writer.write_int_value("cold_start_avoided_ms", self.cold_start_avoided_ms)
        writer.write_int_value("completion_tokens", self.completion_tokens)
        writer.write_int_value("deadline_misses", self.deadline_misses)
        writer.write_int_value("fallbacks", self.fallbacks)
        writer.write_int_value("prompt_tokens", self.prompt_tokens)
        writer.write_int_value("requests", self.requests)
        writer.write_int_value("successes", self.successes)
        writer.write_additional_data_value(self.additional_data)
    

