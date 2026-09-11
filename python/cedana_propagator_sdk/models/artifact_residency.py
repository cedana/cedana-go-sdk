from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class ArtifactResidency(AdditionalDataHolder, Parsable):
    """
    Whether an artefact can still be restored from, and why. status is only what thecontrol plane last recorded, which a reboot does not update.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Boot id recorded when the checkpoint was taken.
    artifact_boot_id: Optional[str] = None
    # True when the storage tier ties the artefact to a single boot of asingle node (`memory`, `local`). Durable tiers survive reboots.
    boot_tied: Optional[bool] = None
    # Whether the engine flags still match what the next worker would start with. Thecompatibility key does not cover them.
    flags_verified: Optional[bool] = None
    # Boot id the node is reporting now, per the latest cluster sync.
    node_boot_id: Optional[str] = None
    # The node_last_sync property
    node_last_sync: Optional[datetime.datetime] = None
    # The node_name property
    node_name: Optional[str] = None
    # The node_status property
    node_status: Optional[str] = None
    # One sentence an operator can act on, naming the evidence.
    reason: Optional[str] = None
    # restorable when every check in the controller's rejectArtifact passes; otherwisethe value names the check that failed.
    state: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ArtifactResidency:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArtifactResidency
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ArtifactResidency()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "artifact_boot_id": lambda n : setattr(self, 'artifact_boot_id', n.get_str_value()),
            "boot_tied": lambda n : setattr(self, 'boot_tied', n.get_bool_value()),
            "flags_verified": lambda n : setattr(self, 'flags_verified', n.get_bool_value()),
            "node_boot_id": lambda n : setattr(self, 'node_boot_id', n.get_str_value()),
            "node_last_sync": lambda n : setattr(self, 'node_last_sync', n.get_datetime_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "node_status": lambda n : setattr(self, 'node_status', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
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
        writer.write_str_value("artifact_boot_id", self.artifact_boot_id)
        writer.write_bool_value("boot_tied", self.boot_tied)
        writer.write_bool_value("flags_verified", self.flags_verified)
        writer.write_str_value("node_boot_id", self.node_boot_id)
        writer.write_datetime_value("node_last_sync", self.node_last_sync)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("node_status", self.node_status)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("state", self.state)
        writer.write_additional_data_value(self.additional_data)
    

