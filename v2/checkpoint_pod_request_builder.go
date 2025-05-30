// Code generated by Microsoft Kiota - DO NOT EDIT.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

package v2

import (
    "context"
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f "github.com/microsoft/kiota-abstractions-go"
    i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2 "github.com/cedana/cedana-go-sdk/models"
)

// CheckpointPodRequestBuilder builds and executes requests for operations under \v2\checkpoint\pod
type CheckpointPodRequestBuilder struct {
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.BaseRequestBuilder
}
// CheckpointPodRequestBuilderPostRequestConfiguration configuration for the request such as headers, query parameters, and middleware options.
type CheckpointPodRequestBuilderPostRequestConfiguration struct {
    // Request headers
    Headers *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestHeaders
    // Request options
    Options []i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestOption
}
// NewCheckpointPodRequestBuilderInternal instantiates a new CheckpointPodRequestBuilder and sets the default values.
func NewCheckpointPodRequestBuilderInternal(pathParameters map[string]string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*CheckpointPodRequestBuilder) {
    m := &CheckpointPodRequestBuilder{
        BaseRequestBuilder: *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewBaseRequestBuilder(requestAdapter, "{+baseurl}/v2/checkpoint/pod", pathParameters),
    }
    return m
}
// NewCheckpointPodRequestBuilder instantiates a new CheckpointPodRequestBuilder and sets the default values.
func NewCheckpointPodRequestBuilder(rawUrl string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*CheckpointPodRequestBuilder) {
    urlParams := make(map[string]string)
    urlParams["request-raw-url"] = rawUrl
    return NewCheckpointPodRequestBuilderInternal(urlParams, requestAdapter)
}
// Post checkpoint a pod
// returns a *string when successful
// returns a HttpError error when the service returns a 404 status code
// returns a HttpError error when the service returns a 500 status code
func (m *CheckpointPodRequestBuilder) Post(ctx context.Context, body i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CheckpointPodable, requestConfiguration *CheckpointPodRequestBuilderPostRequestConfiguration)(*string, error) {
    requestInfo, err := m.ToPostRequestInformation(ctx, body, requestConfiguration);
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
// ToPostRequestInformation checkpoint a pod
// returns a *RequestInformation when successful
func (m *CheckpointPodRequestBuilder) ToPostRequestInformation(ctx context.Context, body i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CheckpointPodable, requestConfiguration *CheckpointPodRequestBuilderPostRequestConfiguration)(*i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestInformation, error) {
    requestInfo := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewRequestInformationWithMethodAndUrlTemplateAndPathParameters(i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.POST, m.BaseRequestBuilder.UrlTemplate, m.BaseRequestBuilder.PathParameters)
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
// returns a *CheckpointPodRequestBuilder when successful
func (m *CheckpointPodRequestBuilder) WithUrl(rawUrl string)(*CheckpointPodRequestBuilder) {
    return NewCheckpointPodRequestBuilder(rawUrl, m.BaseRequestBuilder.RequestAdapter);
}
