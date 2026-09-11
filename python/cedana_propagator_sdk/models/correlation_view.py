from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .artifact_ref import ArtifactRef
    from .correlation_usage import CorrelationUsage
    from .name_count import NameCount

@dataclass
class CorrelationView(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activations property
    activations: Optional[list[NameCount]] = None
    # The artifacts property
    artifacts: Optional[list[ArtifactRef]] = None
    # The experiment_id property
    experiment_id: Optional[UUID] = None
    # The intents property
    intents: Optional[list[NameCount]] = None
    # The name property
    name: Optional[str] = None
    # The observations property
    observations: Optional[list[NameCount]] = None
    # The policy_decisions property
    policy_decisions: Optional[list[NameCount]] = None
    # The scenario property
    scenario: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # The usage property
    usage: Optional[CorrelationUsage] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CorrelationView:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CorrelationView
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CorrelationView()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .artifact_ref import ArtifactRef
        from .correlation_usage import CorrelationUsage
        from .name_count import NameCount

        from .artifact_ref import ArtifactRef
        from .correlation_usage import CorrelationUsage
        from .name_count import NameCount

        fields: dict[str, Callable[[Any], None]] = {
            "activations": lambda n : setattr(self, 'activations', n.get_collection_of_object_values(NameCount)),
            "artifacts": lambda n : setattr(self, 'artifacts', n.get_collection_of_object_values(ArtifactRef)),
            "experiment_id": lambda n : setattr(self, 'experiment_id', n.get_uuid_value()),
            "intents": lambda n : setattr(self, 'intents', n.get_collection_of_object_values(NameCount)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "observations": lambda n : setattr(self, 'observations', n.get_collection_of_object_values(NameCount)),
            "policy_decisions": lambda n : setattr(self, 'policy_decisions', n.get_collection_of_object_values(NameCount)),
            "scenario": lambda n : setattr(self, 'scenario', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "usage": lambda n : setattr(self, 'usage', n.get_object_value(CorrelationUsage)),
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
        writer.write_collection_of_object_values("activations", self.activations)
        writer.write_collection_of_object_values("artifacts", self.artifacts)
        writer.write_uuid_value("experiment_id", self.experiment_id)
        writer.write_collection_of_object_values("intents", self.intents)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("observations", self.observations)
        writer.write_collection_of_object_values("policy_decisions", self.policy_decisions)
        writer.write_str_value("scenario", self.scenario)
        writer.write_str_value("status", self.status)
        writer.write_object_value("usage", self.usage)
        writer.write_additional_data_value(self.additional_data)
    

