// Code generated by Microsoft Kiota - DO NOT EDIT.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

package v2

import (
    "context"
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f "github.com/microsoft/kiota-abstractions-go"
    i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2 "github.com/cedana/cedana-go-sdk/models"
)

// ClusterClusterItemRequestBuilder builds and executes requests for operations under \v2\cluster\{id}
type ClusterClusterItemRequestBuilder struct {
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.BaseRequestBuilder
}
// ClusterClusterItemRequestBuilderDeleteRequestConfiguration configuration for the request such as headers, query parameters, and middleware options.
type ClusterClusterItemRequestBuilderDeleteRequestConfiguration struct {
    // Request headers
    Headers *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestHeaders
    // Request options
    Options []i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestOption
}
// NewClusterClusterItemRequestBuilderInternal instantiates a new ClusterClusterItemRequestBuilder and sets the default values.
func NewClusterClusterItemRequestBuilderInternal(pathParameters map[string]string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*ClusterClusterItemRequestBuilder) {
    m := &ClusterClusterItemRequestBuilder{
        BaseRequestBuilder: *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewBaseRequestBuilder(requestAdapter, "{+baseurl}/v2/cluster/{id}", pathParameters),
    }
    return m
}
// NewClusterClusterItemRequestBuilder instantiates a new ClusterClusterItemRequestBuilder and sets the default values.
func NewClusterClusterItemRequestBuilder(rawUrl string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*ClusterClusterItemRequestBuilder) {
    urlParams := make(map[string]string)
    urlParams["request-raw-url"] = rawUrl
    return NewClusterClusterItemRequestBuilderInternal(urlParams, requestAdapter)
}
// Delete marks a cluster as deleted in the Cedana propagator.This does not physically delete the cluster record, but updates its status to "deleted".
// returns a []byte when successful
// returns a HttpError error when the service returns a 400 status code
// returns a HttpError error when the service returns a 404 status code
// returns a HttpError error when the service returns a 500 status code
func (m *ClusterClusterItemRequestBuilder) Delete(ctx context.Context, requestConfiguration *ClusterClusterItemRequestBuilderDeleteRequestConfiguration)([]byte, error) {
    requestInfo, err := m.ToDeleteRequestInformation(ctx, requestConfiguration);
    if err != nil {
        return nil, err
    }
    errorMapping := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.ErrorMappings {
        "400": i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CreateHttpErrorFromDiscriminatorValue,
        "404": i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CreateHttpErrorFromDiscriminatorValue,
        "500": i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CreateHttpErrorFromDiscriminatorValue,
    }
    res, err := m.BaseRequestBuilder.RequestAdapter.SendPrimitive(ctx, requestInfo, "[]byte", errorMapping)
    if err != nil {
        return nil, err
    }
    if res == nil {
        return nil, nil
    }
    return res.([]byte), nil
}
// ToDeleteRequestInformation marks a cluster as deleted in the Cedana propagator.This does not physically delete the cluster record, but updates its status to "deleted".
// returns a *RequestInformation when successful
func (m *ClusterClusterItemRequestBuilder) ToDeleteRequestInformation(ctx context.Context, requestConfiguration *ClusterClusterItemRequestBuilderDeleteRequestConfiguration)(*i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestInformation, error) {
    requestInfo := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewRequestInformationWithMethodAndUrlTemplateAndPathParameters(i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.DELETE, m.BaseRequestBuilder.UrlTemplate, m.BaseRequestBuilder.PathParameters)
    if requestConfiguration != nil {
        requestInfo.Headers.AddAll(requestConfiguration.Headers)
        requestInfo.AddRequestOptions(requestConfiguration.Options)
    }
    return requestInfo, nil
}
// WithUrl returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
// returns a *ClusterClusterItemRequestBuilder when successful
func (m *ClusterClusterItemRequestBuilder) WithUrl(rawUrl string)(*ClusterClusterItemRequestBuilder) {
    return NewClusterClusterItemRequestBuilder(rawUrl, m.BaseRequestBuilder.RequestAdapter);
}
