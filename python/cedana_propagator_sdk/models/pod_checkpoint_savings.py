from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PodCheckpointSavings(AdditionalDataHolder, Parsable):
    """
    Per-pod checkpoint savings data
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Average interval between checkpoints (seconds)
    avg_interval_seconds: Optional[float] = None
    # Node capacity type: "spot" or "on-demand"
    capacity_type: Optional[str] = None
    # The checkpoint_count property
    checkpoint_count: Optional[int] = None
    # The cluster_id property
    cluster_id: Optional[str] = None
    # Estimated savings (if spot instance)
    estimated_savings: Optional[float] = None
    # The first_checkpoint property
    first_checkpoint: Optional[datetime.datetime] = None
    # The gpu property
    gpu: Optional[str] = None
    # Number of automatic heartbeat checkpoints
    heartbeat_checkpoints: Optional[int] = None
    # Node instance type (e.g., "m5.xlarge", "n1-standard-4")
    instance_type: Optional[str] = None
    # The last_checkpoint property
    last_checkpoint: Optional[datetime.datetime] = None
    # Number of manual checkpoints
    manual_checkpoints: Optional[int] = None
    # Maximum interval - worst case data loss on failure (seconds)
    max_recovery_point_seconds: Optional[float] = None
    # Minimum interval between checkpoints (seconds)
    min_interval_seconds: Optional[float] = None
    # The namespace property
    namespace: Optional[str] = None
    # Node name (for linking to node details page)
    node_name: Optional[str] = None
    # Node region
    node_region: Optional[str] = None
    # On-demand price per hour (from user config)
    ondemand_price_per_hour: Optional[float] = None
    # The platform property
    platform: Optional[str] = None
    # The pod_name property
    pod_name: Optional[str] = None
    # Ratio of time protected to checkpoint overhead (higher = more efficient)
    protection_efficiency_ratio: Optional[float] = None
    # The refreshed_at property
    refreshed_at: Optional[datetime.datetime] = None
    # Spot price per hour (from user config)
    spot_price_per_hour: Optional[float] = None
    # Total time (seconds) between first and last checkpoint - time "protected"
    time_protected_seconds: Optional[float] = None
    # Total time spent checkpointing (nanoseconds)
    total_checkpoint_duration_ns: Optional[int] = None
    # Total data checkpointed (bytes)
    total_checkpoint_size_bytes: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PodCheckpointSavings:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PodCheckpointSavings
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PodCheckpointSavings()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "avg_interval_seconds": lambda n : setattr(self, 'avg_interval_seconds', n.get_float_value()),
            "capacity_type": lambda n : setattr(self, 'capacity_type', n.get_str_value()),
            "checkpoint_count": lambda n : setattr(self, 'checkpoint_count', n.get_int_value()),
            "cluster_id": lambda n : setattr(self, 'cluster_id', n.get_str_value()),
            "estimated_savings": lambda n : setattr(self, 'estimated_savings', n.get_float_value()),
            "first_checkpoint": lambda n : setattr(self, 'first_checkpoint', n.get_datetime_value()),
            "gpu": lambda n : setattr(self, 'gpu', n.get_str_value()),
            "heartbeat_checkpoints": lambda n : setattr(self, 'heartbeat_checkpoints', n.get_int_value()),
            "instance_type": lambda n : setattr(self, 'instance_type', n.get_str_value()),
            "last_checkpoint": lambda n : setattr(self, 'last_checkpoint', n.get_datetime_value()),
            "manual_checkpoints": lambda n : setattr(self, 'manual_checkpoints', n.get_int_value()),
            "max_recovery_point_seconds": lambda n : setattr(self, 'max_recovery_point_seconds', n.get_float_value()),
            "min_interval_seconds": lambda n : setattr(self, 'min_interval_seconds', n.get_float_value()),
            "namespace": lambda n : setattr(self, 'namespace', n.get_str_value()),
            "node_name": lambda n : setattr(self, 'node_name', n.get_str_value()),
            "node_region": lambda n : setattr(self, 'node_region', n.get_str_value()),
            "ondemand_price_per_hour": lambda n : setattr(self, 'ondemand_price_per_hour', n.get_float_value()),
            "platform": lambda n : setattr(self, 'platform', n.get_str_value()),
            "pod_name": lambda n : setattr(self, 'pod_name', n.get_str_value()),
            "protection_efficiency_ratio": lambda n : setattr(self, 'protection_efficiency_ratio', n.get_float_value()),
            "refreshed_at": lambda n : setattr(self, 'refreshed_at', n.get_datetime_value()),
            "spot_price_per_hour": lambda n : setattr(self, 'spot_price_per_hour', n.get_float_value()),
            "time_protected_seconds": lambda n : setattr(self, 'time_protected_seconds', n.get_float_value()),
            "total_checkpoint_duration_ns": lambda n : setattr(self, 'total_checkpoint_duration_ns', n.get_int_value()),
            "total_checkpoint_size_bytes": lambda n : setattr(self, 'total_checkpoint_size_bytes', n.get_int_value()),
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
        writer.write_float_value("avg_interval_seconds", self.avg_interval_seconds)
        writer.write_str_value("capacity_type", self.capacity_type)
        writer.write_int_value("checkpoint_count", self.checkpoint_count)
        writer.write_str_value("cluster_id", self.cluster_id)
        writer.write_float_value("estimated_savings", self.estimated_savings)
        writer.write_datetime_value("first_checkpoint", self.first_checkpoint)
        writer.write_str_value("gpu", self.gpu)
        writer.write_int_value("heartbeat_checkpoints", self.heartbeat_checkpoints)
        writer.write_str_value("instance_type", self.instance_type)
        writer.write_datetime_value("last_checkpoint", self.last_checkpoint)
        writer.write_int_value("manual_checkpoints", self.manual_checkpoints)
        writer.write_float_value("max_recovery_point_seconds", self.max_recovery_point_seconds)
        writer.write_float_value("min_interval_seconds", self.min_interval_seconds)
        writer.write_str_value("namespace", self.namespace)
        writer.write_str_value("node_name", self.node_name)
        writer.write_str_value("node_region", self.node_region)
        writer.write_float_value("ondemand_price_per_hour", self.ondemand_price_per_hour)
        writer.write_str_value("platform", self.platform)
        writer.write_str_value("pod_name", self.pod_name)
        writer.write_float_value("protection_efficiency_ratio", self.protection_efficiency_ratio)
        writer.write_datetime_value("refreshed_at", self.refreshed_at)
        writer.write_float_value("spot_price_per_hour", self.spot_price_per_hour)
        writer.write_float_value("time_protected_seconds", self.time_protected_seconds)
        writer.write_int_value("total_checkpoint_duration_ns", self.total_checkpoint_duration_ns)
        writer.write_int_value("total_checkpoint_size_bytes", self.total_checkpoint_size_bytes)
        writer.write_additional_data_value(self.additional_data)
    

