from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .deployment_step import DeploymentStep

@dataclass
class DeploymentProgress(AdditionalDataHolder, Parsable):
    """
    How far a profile has got, and how long each stage took.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The activation_started_at property
    activation_started_at: Optional[datetime.datetime] = None
    # Measured activation-start-to-ready, absent until the profile is ready. Atime-to-ready, and only a cold start when start_kind is not restore.
    cold_start_ms: Optional[int] = None
    # The phase property
    phase: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    # The ready property
    ready: Optional[bool] = None
    # The ready_at property
    ready_at: Optional[datetime.datetime] = None
    # The checkpoint the worker was told to restore from, when it was.
    restore_checkpoint_path: Optional[str] = None
    # How the worker behind this activation started: restore, cold, or null when nolive worker pod is known.
    start_kind: Optional[str] = None
    # The steps property
    steps: Optional[list[DeploymentStep]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DeploymentProgress:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DeploymentProgress
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DeploymentProgress()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .deployment_step import DeploymentStep

        from .deployment_step import DeploymentStep

        fields: dict[str, Callable[[Any], None]] = {
            "activation_started_at": lambda n : setattr(self, 'activation_started_at', n.get_datetime_value()),
            "cold_start_ms": lambda n : setattr(self, 'cold_start_ms', n.get_int_value()),
            "phase": lambda n : setattr(self, 'phase', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
            "ready": lambda n : setattr(self, 'ready', n.get_bool_value()),
            "ready_at": lambda n : setattr(self, 'ready_at', n.get_datetime_value()),
            "restore_checkpoint_path": lambda n : setattr(self, 'restore_checkpoint_path', n.get_str_value()),
            "start_kind": lambda n : setattr(self, 'start_kind', n.get_str_value()),
            "steps": lambda n : setattr(self, 'steps', n.get_collection_of_object_values(DeploymentStep)),
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
        writer.write_datetime_value("activation_started_at", self.activation_started_at)
        writer.write_int_value("cold_start_ms", self.cold_start_ms)
        writer.write_str_value("phase", self.phase)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_bool_value("ready", self.ready)
        writer.write_datetime_value("ready_at", self.ready_at)
        writer.write_str_value("restore_checkpoint_path", self.restore_checkpoint_path)
        writer.write_str_value("start_kind", self.start_kind)
        writer.write_collection_of_object_values("steps", self.steps)
        writer.write_additional_data_value(self.additional_data)
    

