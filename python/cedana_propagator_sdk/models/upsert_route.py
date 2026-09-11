from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .upsert_target import UpsertTarget

@dataclass
class UpsertRoute(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The classifier_profile_id property
    classifier_profile_id: Optional[str] = None
    # The classifier_prompt property
    classifier_prompt: Optional[str] = None
    # The classifier_response_schema property
    classifier_response_schema: Optional[str] = None
    # The logical_model property
    logical_model: Optional[str] = None
    # The mode property
    mode: Optional[str] = None
    # The queue_timeout_ms property
    queue_timeout_ms: Optional[int] = None
    # The targets property
    targets: Optional[list[UpsertTarget]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> UpsertRoute:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: UpsertRoute
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return UpsertRoute()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .upsert_target import UpsertTarget

        from .upsert_target import UpsertTarget

        fields: dict[str, Callable[[Any], None]] = {
            "classifier_profile_id": lambda n : setattr(self, 'classifier_profile_id', n.get_str_value()),
            "classifier_prompt": lambda n : setattr(self, 'classifier_prompt', n.get_str_value()),
            "classifier_response_schema": lambda n : setattr(self, 'classifier_response_schema', n.get_str_value()),
            "logical_model": lambda n : setattr(self, 'logical_model', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "queue_timeout_ms": lambda n : setattr(self, 'queue_timeout_ms', n.get_int_value()),
            "targets": lambda n : setattr(self, 'targets', n.get_collection_of_object_values(UpsertTarget)),
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
        writer.write_str_value("classifier_profile_id", self.classifier_profile_id)
        writer.write_str_value("classifier_prompt", self.classifier_prompt)
        writer.write_str_value("classifier_response_schema", self.classifier_response_schema)
        writer.write_str_value("logical_model", self.logical_model)
        writer.write_str_value("mode", self.mode)
        writer.write_int_value("queue_timeout_ms", self.queue_timeout_ms)
        writer.write_collection_of_object_values("targets", self.targets)
        writer.write_additional_data_value(self.additional_data)
    

