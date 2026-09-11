from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .slurm_checkpoint_kind import SlurmCheckpointKind
    from .slurm_checkpoint_reason import SlurmCheckpointReason

@dataclass
class CheckpointSlurmJob(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The action_id property
    action_id: Optional[str] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # The job_id property
    job_id: Optional[str] = None
    # The job_name property
    job_name: Optional[str] = None
    # The kind property
    kind: Optional[SlurmCheckpointKind] = None
    # The reason property
    reason: Optional[SlurmCheckpointReason] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> CheckpointSlurmJob:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: CheckpointSlurmJob
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return CheckpointSlurmJob()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .slurm_checkpoint_kind import SlurmCheckpointKind
        from .slurm_checkpoint_reason import SlurmCheckpointReason

        from .slurm_checkpoint_kind import SlurmCheckpointKind
        from .slurm_checkpoint_reason import SlurmCheckpointReason

        fields: dict[str, Callable[[Any], None]] = {
            "action_id": lambda n : setattr(self, 'action_id', n.get_str_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "job_id": lambda n : setattr(self, 'job_id', n.get_str_value()),
            "job_name": lambda n : setattr(self, 'job_name', n.get_str_value()),
            "kind": lambda n : setattr(self, 'kind', n.get_enum_value(SlurmCheckpointKind)),
            "reason": lambda n : setattr(self, 'reason', n.get_enum_value(SlurmCheckpointReason)),
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
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_str_value("job_id", self.job_id)
        writer.write_str_value("job_name", self.job_name)
        writer.write_enum_value("kind", self.kind)
        writer.write_enum_value("reason", self.reason)
        writer.write_additional_data_value(self.additional_data)
    

