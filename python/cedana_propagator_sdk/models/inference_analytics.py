from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .serving_analytics import ServingAnalytics
    from .startup_analytics import StartupAnalytics
    from .storage_analytics import StorageAnalytics

@dataclass
class InferenceAnalytics(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The evidence property
    evidence: Optional[str] = None
    # The experiment_id property
    experiment_id: Optional[UUID] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The sample_count property
    sample_count: Optional[int] = None
    # The serving property
    serving: Optional[ServingAnalytics] = None
    # The startup property
    startup: Optional[StartupAnalytics] = None
    # The storage property
    storage: Optional[StorageAnalytics] = None
    # The window_hours property
    window_hours: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InferenceAnalytics:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InferenceAnalytics
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InferenceAnalytics()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .serving_analytics import ServingAnalytics
        from .startup_analytics import StartupAnalytics
        from .storage_analytics import StorageAnalytics

        from .serving_analytics import ServingAnalytics
        from .startup_analytics import StartupAnalytics
        from .storage_analytics import StorageAnalytics

        fields: dict[str, Callable[[Any], None]] = {
            "evidence": lambda n : setattr(self, 'evidence', n.get_str_value()),
            "experiment_id": lambda n : setattr(self, 'experiment_id', n.get_uuid_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "sample_count": lambda n : setattr(self, 'sample_count', n.get_int_value()),
            "serving": lambda n : setattr(self, 'serving', n.get_object_value(ServingAnalytics)),
            "startup": lambda n : setattr(self, 'startup', n.get_object_value(StartupAnalytics)),
            "storage": lambda n : setattr(self, 'storage', n.get_object_value(StorageAnalytics)),
            "window_hours": lambda n : setattr(self, 'window_hours', n.get_int_value()),
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
        writer.write_str_value("evidence", self.evidence)
        writer.write_uuid_value("experiment_id", self.experiment_id)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_int_value("sample_count", self.sample_count)
        writer.write_object_value("serving", self.serving)
        writer.write_object_value("startup", self.startup)
        writer.write_object_value("storage", self.storage)
        writer.write_int_value("window_hours", self.window_hours)
        writer.write_additional_data_value(self.additional_data)
    

