// Code generated by Microsoft Kiota - DO NOT EDIT.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

package v2

import (
    "context"
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f "github.com/microsoft/kiota-abstractions-go"
    i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2 "github.com/cedana/cedana-go-sdk/models"
)

// CheckpointsInfoInfoItemRequestBuilder builds and executes requests for operations under \v2\checkpoints\info\{id}
type CheckpointsInfoInfoItemRequestBuilder struct {
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.BaseRequestBuilder
}
// CheckpointsInfoInfoItemRequestBuilderPutRequestConfiguration configuration for the request such as headers, query parameters, and middleware options.
type CheckpointsInfoInfoItemRequestBuilderPutRequestConfiguration struct {
    // Request headers
    Headers *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestHeaders
    // Request options
    Options []i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestOption
}
// NewCheckpointsInfoInfoItemRequestBuilderInternal instantiates a new CheckpointsInfoInfoItemRequestBuilder and sets the default values.
func NewCheckpointsInfoInfoItemRequestBuilderInternal(pathParameters map[string]string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*CheckpointsInfoInfoItemRequestBuilder) {
    m := &CheckpointsInfoInfoItemRequestBuilder{
        BaseRequestBuilder: *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewBaseRequestBuilder(requestAdapter, "{+baseurl}/v2/checkpoints/info/{id}", pathParameters),
    }
    return m
}
// NewCheckpointsInfoInfoItemRequestBuilder instantiates a new CheckpointsInfoInfoItemRequestBuilder and sets the default values.
func NewCheckpointsInfoInfoItemRequestBuilder(rawUrl string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*CheckpointsInfoInfoItemRequestBuilder) {
    urlParams := make(map[string]string)
    urlParams["request-raw-url"] = rawUrl
    return NewCheckpointsInfoInfoItemRequestBuilderInternal(urlParams, requestAdapter)
}
// Put add information about the checkpointed pod and runtime
// returns a *string when successful
// returns a HttpError error when the service returns a 404 status code
// returns a HttpError error when the service returns a 500 status code
func (m *CheckpointsInfoInfoItemRequestBuilder) Put(ctx context.Context, body i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CheckpointInfoable, requestConfiguration *CheckpointsInfoInfoItemRequestBuilderPutRequestConfiguration)(*string, error) {
    requestInfo, err := m.ToPutRequestInformation(ctx, body, requestConfiguration);
    if err != nil {
        return nil, err
    }
    errorMapping := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.ErrorMappings {
        "404": i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CreateHttpErrorFromDiscriminatorValue,
        "500": i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CreateHttpErrorFromDiscriminatorValue,
    }
    res, err := m.BaseRequestBuilder.RequestAdapter.SendPrimitive(ctx, requestInfo, "string", errorMapping)
    if err != nil {
        return nil, err
    }
    if res == nil {
        return nil, nil
    }
    return res.(*string), nil
}
// ToPutRequestInformation add information about the checkpointed pod and runtime
// returns a *RequestInformation when successful
func (m *CheckpointsInfoInfoItemRequestBuilder) ToPutRequestInformation(ctx context.Context, body i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CheckpointInfoable, requestConfiguration *CheckpointsInfoInfoItemRequestBuilderPutRequestConfiguration)(*i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestInformation, error) {
    requestInfo := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewRequestInformationWithMethodAndUrlTemplateAndPathParameters(i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.PUT, m.BaseRequestBuilder.UrlTemplate, m.BaseRequestBuilder.PathParameters)
    if requestConfiguration != nil {
        requestInfo.Headers.AddAll(requestConfiguration.Headers)
        requestInfo.AddRequestOptions(requestConfiguration.Options)
    }
    requestInfo.Headers.TryAdd("Accept", "text/plain;q=0.9")
    err := requestInfo.SetContentFromParsable(ctx, m.BaseRequestBuilder.RequestAdapter, "application/json", body)
    if err != nil {
        return nil, err
    }
    return requestInfo, nil
}
// WithUrl returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
// returns a *CheckpointsInfoInfoItemRequestBuilder when successful
func (m *CheckpointsInfoInfoItemRequestBuilder) WithUrl(rawUrl string)(*CheckpointsInfoInfoItemRequestBuilder) {
    return NewCheckpointsInfoInfoItemRequestBuilder(rawUrl, m.BaseRequestBuilder.RequestAdapter);
}
