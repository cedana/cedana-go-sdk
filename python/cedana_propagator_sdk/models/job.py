from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .process_state import ProcessState

@dataclass
class Job(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The JID property
    j_i_d: Optional[str] = None
    # The Log property
    log: Optional[str] = None
    # The State property
    state: Optional[ProcessState] = None
    # The Type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Job:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Job
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Job()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .process_state import ProcessState

        from .process_state import ProcessState

        fields: dict[str, Callable[[Any], None]] = {
            "JID": lambda n : setattr(self, 'j_i_d', n.get_str_value()),
            "Log": lambda n : setattr(self, 'log', n.get_str_value()),
            "State": lambda n : setattr(self, 'state', n.get_object_value(ProcessState)),
            "Type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("JID", self.j_i_d)
        writer.write_str_value("Log", self.log)
        writer.write_object_value("State", self.state)
        writer.write_str_value("Type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

