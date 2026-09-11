from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .pipeline_filter_member4_type import PipelineFilterMember4_type
    from .slurm_jobs_filter_config import SlurmJobsFilterConfig

@dataclass
class PipelineFilterMember4(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Filter config for targeting explicit SLURM jobs by their numeric `slurm_job_id`(the value the UI's `SlurmJob` exposes). These are resolved to `slurm_jobs.id` UUIDsat policy-creation time and stored in `policy.resource_id`.
    config: Optional[SlurmJobsFilterConfig] = None
    # The type property
    type: Optional[PipelineFilterMember4_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PipelineFilterMember4:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PipelineFilterMember4
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PipelineFilterMember4()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .pipeline_filter_member4_type import PipelineFilterMember4_type
        from .slurm_jobs_filter_config import SlurmJobsFilterConfig

        from .pipeline_filter_member4_type import PipelineFilterMember4_type
        from .slurm_jobs_filter_config import SlurmJobsFilterConfig

        fields: dict[str, Callable[[Any], None]] = {
            "config": lambda n : setattr(self, 'config', n.get_object_value(SlurmJobsFilterConfig)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(PipelineFilterMember4_type)),
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
        writer.write_object_value("config", self.config)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

