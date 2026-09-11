from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class OtelCredsResponse(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The OTEL_EXPORTER_OTLP_ENDPOINT property
    o_t_e_l_e_x_p_o_r_t_e_r_o_t_l_p_e_n_d_p_o_i_n_t: Optional[str] = None
    # The OTEL_EXPORTER_OTLP_HEADERS property
    o_t_e_l_e_x_p_o_r_t_e_r_o_t_l_p_h_e_a_d_e_r_s: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> OtelCredsResponse:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: OtelCredsResponse
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return OtelCredsResponse()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "OTEL_EXPORTER_OTLP_ENDPOINT": lambda n : setattr(self, 'o_t_e_l_e_x_p_o_r_t_e_r_o_t_l_p_e_n_d_p_o_i_n_t', n.get_str_value()),
            "OTEL_EXPORTER_OTLP_HEADERS": lambda n : setattr(self, 'o_t_e_l_e_x_p_o_r_t_e_r_o_t_l_p_h_e_a_d_e_r_s', n.get_str_value()),
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
        writer.write_str_value("OTEL_EXPORTER_OTLP_ENDPOINT", self.o_t_e_l_e_x_p_o_r_t_e_r_o_t_l_p_e_n_d_p_o_i_n_t)
        writer.write_str_value("OTEL_EXPORTER_OTLP_HEADERS", self.o_t_e_l_e_x_p_o_r_t_e_r_o_t_l_p_h_e_a_d_e_r_s)
        writer.write_additional_data_value(self.additional_data)
    

