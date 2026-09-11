from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class SlurmEvent(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The derived_ec property
    derived_ec: Optional[int] = None
    # The exit_code property
    exit_code: Optional[int] = None
    # Node that triggered the failure, if any.
    failed_node: Optional[str] = None
    # The job_id property
    job_id: Optional[int] = None
    # The kill_requid property
    kill_requid: Optional[int] = None
    # The partition property
    partition: Optional[str] = None
    # Human-readable exit reason from slurmdbd (derived_es).
    reason: Optional[str] = None
    # The status property
    status: Optional[str] = None
    # Seconds the job spent suspended (preemption-with-checkpoint signal).
    time_suspended: Optional[int] = None
    # Epoch seconds; falls back to start_time, then submit_time, then 0.
    timestamp: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SlurmEvent:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SlurmEvent
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SlurmEvent()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "derived_ec": lambda n : setattr(self, 'derived_ec', n.get_int_value()),
            "exit_code": lambda n : setattr(self, 'exit_code', n.get_int_value()),
            "failed_node": lambda n : setattr(self, 'failed_node', n.get_str_value()),
            "job_id": lambda n : setattr(self, 'job_id', n.get_int_value()),
            "kill_requid": lambda n : setattr(self, 'kill_requid', n.get_int_value()),
            "partition": lambda n : setattr(self, 'partition', n.get_str_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "time_suspended": lambda n : setattr(self, 'time_suspended', n.get_int_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_int_value()),
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
        writer.write_int_value("derived_ec", self.derived_ec)
        writer.write_int_value("exit_code", self.exit_code)
        writer.write_str_value("failed_node", self.failed_node)
        writer.write_int_value("job_id", self.job_id)
        writer.write_int_value("kill_requid", self.kill_requid)
        writer.write_str_value("partition", self.partition)
        writer.write_str_value("reason", self.reason)
        writer.write_str_value("status", self.status)
        writer.write_int_value("time_suspended", self.time_suspended)
        writer.write_int_value("timestamp", self.timestamp)
        writer.write_additional_data_value(self.additional_data)
    

