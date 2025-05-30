// Code generated by Microsoft Kiota - DO NOT EDIT.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

package models

import (
    i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91 "github.com/microsoft/kiota-abstractions-go/serialization"
)

type RestorePod struct {
    // The action_id property
    action_id *string
    // Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additionalData map[string]any
    // The cluster_id property
    cluster_id *string
}
// NewRestorePod instantiates a new RestorePod and sets the default values.
func NewRestorePod()(*RestorePod) {
    m := &RestorePod{
    }
    m.SetAdditionalData(make(map[string]any))
    return m
}
// CreateRestorePodFromDiscriminatorValue creates a new instance of the appropriate class based on discriminator value
// returns a Parsable when successful
func CreateRestorePodFromDiscriminatorValue(parseNode i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.Parsable, error) {
    return NewRestorePod(), nil
}
// GetActionId gets the action_id property value. The action_id property
// returns a *string when successful
func (m *RestorePod) GetActionId()(*string) {
    return m.action_id
}
// GetAdditionalData gets the AdditionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
// returns a map[string]any when successful
func (m *RestorePod) GetAdditionalData()(map[string]any) {
    return m.additionalData
}
// GetClusterId gets the cluster_id property value. The cluster_id property
// returns a *string when successful
func (m *RestorePod) GetClusterId()(*string) {
    return m.cluster_id
}
// GetFieldDeserializers the deserialization information for the current model
// returns a map[string]func(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(error) when successful
func (m *RestorePod) GetFieldDeserializers()(map[string]func(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(error)) {
    res := make(map[string]func(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(error))
    res["action_id"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetActionId(val)
        }
        return nil
    }
    res["cluster_id"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetClusterId(val)
        }
        return nil
    }
    return res
}
// Serialize serializes information the current object
func (m *RestorePod) Serialize(writer i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.SerializationWriter)(error) {
    {
        err := writer.WriteStringValue("action_id", m.GetActionId())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteStringValue("cluster_id", m.GetClusterId())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteAdditionalData(m.GetAdditionalData())
        if err != nil {
            return err
        }
    }
    return nil
}
// SetActionId sets the action_id property value. The action_id property
func (m *RestorePod) SetActionId(value *string)() {
    m.action_id = value
}
// SetAdditionalData sets the AdditionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
func (m *RestorePod) SetAdditionalData(value map[string]any)() {
    m.additionalData = value
}
// SetClusterId sets the cluster_id property value. The cluster_id property
func (m *RestorePod) SetClusterId(value *string)() {
    m.cluster_id = value
}
type RestorePodable interface {
    i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.AdditionalDataHolder
    i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.Parsable
    GetActionId()(*string)
    GetClusterId()(*string)
    SetActionId(value *string)()
    SetClusterId(value *string)()
}
