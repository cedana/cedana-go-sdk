// Code generated by Microsoft Kiota - DO NOT EDIT.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

package models

import (
    i561e97a8befe7661a44c8f54600992b4207a3a0cf6770e5559949bc276de2e22 "github.com/google/uuid"
    i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91 "github.com/microsoft/kiota-abstractions-go/serialization"
)

type PodResponse struct {
    // Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additionalData map[string]any
    // The age property
    age *string
    // The id property
    id *i561e97a8befe7661a44c8f54600992b4207a3a0cf6770e5559949bc276de2e22.UUID
    // The name property
    name *string
    // The namespace property
    namespace *string
    // The node property
    node *string
    // The ready property
    ready *string
    // The restarts property
    restarts *int32
    // The status property
    status *string
}
// NewPodResponse instantiates a new PodResponse and sets the default values.
func NewPodResponse()(*PodResponse) {
    m := &PodResponse{
    }
    m.SetAdditionalData(make(map[string]any))
    return m
}
// CreatePodResponseFromDiscriminatorValue creates a new instance of the appropriate class based on discriminator value
// returns a Parsable when successful
func CreatePodResponseFromDiscriminatorValue(parseNode i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.Parsable, error) {
    return NewPodResponse(), nil
}
// GetAdditionalData gets the AdditionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
// returns a map[string]any when successful
func (m *PodResponse) GetAdditionalData()(map[string]any) {
    return m.additionalData
}
// GetAge gets the age property value. The age property
// returns a *string when successful
func (m *PodResponse) GetAge()(*string) {
    return m.age
}
// GetFieldDeserializers the deserialization information for the current model
// returns a map[string]func(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(error) when successful
func (m *PodResponse) GetFieldDeserializers()(map[string]func(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(error)) {
    res := make(map[string]func(i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode)(error))
    res["age"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetAge(val)
        }
        return nil
    }
    res["id"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetUUIDValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetId(val)
        }
        return nil
    }
    res["name"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetName(val)
        }
        return nil
    }
    res["namespace"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetNamespace(val)
        }
        return nil
    }
    res["node"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetNode(val)
        }
        return nil
    }
    res["ready"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetReady(val)
        }
        return nil
    }
    res["restarts"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetInt32Value()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetRestarts(val)
        }
        return nil
    }
    res["status"] = func (n i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.ParseNode) error {
        val, err := n.GetStringValue()
        if err != nil {
            return err
        }
        if val != nil {
            m.SetStatus(val)
        }
        return nil
    }
    return res
}
// GetId gets the id property value. The id property
// returns a *UUID when successful
func (m *PodResponse) GetId()(*i561e97a8befe7661a44c8f54600992b4207a3a0cf6770e5559949bc276de2e22.UUID) {
    return m.id
}
// GetName gets the name property value. The name property
// returns a *string when successful
func (m *PodResponse) GetName()(*string) {
    return m.name
}
// GetNamespace gets the namespace property value. The namespace property
// returns a *string when successful
func (m *PodResponse) GetNamespace()(*string) {
    return m.namespace
}
// GetNode gets the node property value. The node property
// returns a *string when successful
func (m *PodResponse) GetNode()(*string) {
    return m.node
}
// GetReady gets the ready property value. The ready property
// returns a *string when successful
func (m *PodResponse) GetReady()(*string) {
    return m.ready
}
// GetRestarts gets the restarts property value. The restarts property
// returns a *int32 when successful
func (m *PodResponse) GetRestarts()(*int32) {
    return m.restarts
}
// GetStatus gets the status property value. The status property
// returns a *string when successful
func (m *PodResponse) GetStatus()(*string) {
    return m.status
}
// Serialize serializes information the current object
func (m *PodResponse) Serialize(writer i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.SerializationWriter)(error) {
    {
        err := writer.WriteStringValue("age", m.GetAge())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteUUIDValue("id", m.GetId())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteStringValue("name", m.GetName())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteStringValue("namespace", m.GetNamespace())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteStringValue("node", m.GetNode())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteStringValue("ready", m.GetReady())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteInt32Value("restarts", m.GetRestarts())
        if err != nil {
            return err
        }
    }
    {
        err := writer.WriteStringValue("status", m.GetStatus())
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
// SetAdditionalData sets the AdditionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
func (m *PodResponse) SetAdditionalData(value map[string]any)() {
    m.additionalData = value
}
// SetAge sets the age property value. The age property
func (m *PodResponse) SetAge(value *string)() {
    m.age = value
}
// SetId sets the id property value. The id property
func (m *PodResponse) SetId(value *i561e97a8befe7661a44c8f54600992b4207a3a0cf6770e5559949bc276de2e22.UUID)() {
    m.id = value
}
// SetName sets the name property value. The name property
func (m *PodResponse) SetName(value *string)() {
    m.name = value
}
// SetNamespace sets the namespace property value. The namespace property
func (m *PodResponse) SetNamespace(value *string)() {
    m.namespace = value
}
// SetNode sets the node property value. The node property
func (m *PodResponse) SetNode(value *string)() {
    m.node = value
}
// SetReady sets the ready property value. The ready property
func (m *PodResponse) SetReady(value *string)() {
    m.ready = value
}
// SetRestarts sets the restarts property value. The restarts property
func (m *PodResponse) SetRestarts(value *int32)() {
    m.restarts = value
}
// SetStatus sets the status property value. The status property
func (m *PodResponse) SetStatus(value *string)() {
    m.status = value
}
type PodResponseable interface {
    i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.AdditionalDataHolder
    i878a80d2330e89d26896388a3f487eef27b0a0e6c010c493bf80be1452208f91.Parsable
    GetAge()(*string)
    GetId()(*i561e97a8befe7661a44c8f54600992b4207a3a0cf6770e5559949bc276de2e22.UUID)
    GetName()(*string)
    GetNamespace()(*string)
    GetNode()(*string)
    GetReady()(*string)
    GetRestarts()(*int32)
    GetStatus()(*string)
    SetAge(value *string)()
    SetId(value *i561e97a8befe7661a44c8f54600992b4207a3a0cf6770e5559949bc276de2e22.UUID)()
    SetName(value *string)()
    SetNamespace(value *string)()
    SetNode(value *string)()
    SetReady(value *string)()
    SetRestarts(value *int32)()
    SetStatus(value *string)()
}
