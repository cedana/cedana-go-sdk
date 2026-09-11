from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RetentionPolicyUpsert(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The enabled property
    enabled: Optional[bool] = None
    # The max_age_days property
    max_age_days: Optional[int] = None
    # The max_count property
    max_count: Optional[int] = None
    # The min_tier property
    min_tier: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The policy_id property
    policy_id: Optional[str] = None
    # The profile_id property
    profile_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RetentionPolicyUpsert:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RetentionPolicyUpsert
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RetentionPolicyUpsert()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "enabled": lambda n : setattr(self, 'enabled', n.get_bool_value()),
            "max_age_days": lambda n : setattr(self, 'max_age_days', n.get_int_value()),
            "max_count": lambda n : setattr(self, 'max_count', n.get_int_value()),
            "min_tier": lambda n : setattr(self, 'min_tier', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "policy_id": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "profile_id": lambda n : setattr(self, 'profile_id', n.get_str_value()),
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
        writer.write_bool_value("enabled", self.enabled)
        writer.write_int_value("max_age_days", self.max_age_days)
        writer.write_int_value("max_count", self.max_count)
        writer.write_str_value("min_tier", self.min_tier)
        writer.write_str_value("name", self.name)
        writer.write_str_value("policy_id", self.policy_id)
        writer.write_str_value("profile_id", self.profile_id)
        writer.write_additional_data_value(self.additional_data)
    

