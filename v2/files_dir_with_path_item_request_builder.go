// Code generated by Microsoft Kiota - DO NOT EDIT.
// Changes may cause incorrect behavior and will be lost if the code is regenerated.

package v2

import (
    "context"
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f "github.com/microsoft/kiota-abstractions-go"
    i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2 "github.com/cedana/cedana-go-sdk/models"
)

// FilesDirWithPathItemRequestBuilder builds and executes requests for operations under \v2\files\dir\{path}
type FilesDirWithPathItemRequestBuilder struct {
    i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.BaseRequestBuilder
}
// FilesDirWithPathItemRequestBuilderGetRequestConfiguration configuration for the request such as headers, query parameters, and middleware options.
type FilesDirWithPathItemRequestBuilderGetRequestConfiguration struct {
    // Request headers
    Headers *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestHeaders
    // Request options
    Options []i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestOption
}
// NewFilesDirWithPathItemRequestBuilderInternal instantiates a new FilesDirWithPathItemRequestBuilder and sets the default values.
func NewFilesDirWithPathItemRequestBuilderInternal(pathParameters map[string]string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*FilesDirWithPathItemRequestBuilder) {
    m := &FilesDirWithPathItemRequestBuilder{
        BaseRequestBuilder: *i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewBaseRequestBuilder(requestAdapter, "{+baseurl}/v2/files/dir/{path}", pathParameters),
    }
    return m
}
// NewFilesDirWithPathItemRequestBuilder instantiates a new FilesDirWithPathItemRequestBuilder and sets the default values.
func NewFilesDirWithPathItemRequestBuilder(rawUrl string, requestAdapter i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestAdapter)(*FilesDirWithPathItemRequestBuilder) {
    urlParams := make(map[string]string)
    urlParams["request-raw-url"] = rawUrl
    return NewFilesDirWithPathItemRequestBuilderInternal(urlParams, requestAdapter)
}
// Get read directory contents
// returns a []string when successful
// returns a HttpError error when the service returns a 500 status code
func (m *FilesDirWithPathItemRequestBuilder) Get(ctx context.Context, requestConfiguration *FilesDirWithPathItemRequestBuilderGetRequestConfiguration)([]string, error) {
    requestInfo, err := m.ToGetRequestInformation(ctx, requestConfiguration);
    if err != nil {
        return nil, err
    }
    errorMapping := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.ErrorMappings {
        "500": i4db02de4fa95db6167263a0a43a6a58c23904074eb83cc381a94eba9021abdb2.CreateHttpErrorFromDiscriminatorValue,
    }
    res, err := m.BaseRequestBuilder.RequestAdapter.SendPrimitiveCollection(ctx, requestInfo, "string", errorMapping)
    if err != nil {
        return nil, err
    }
    val := make([]string, len(res))
    for i, v := range res {
        if v != nil {
            val[i] = *(v.(*string))
        }
    }
    return val, nil
}
// ToGetRequestInformation read directory contents
// returns a *RequestInformation when successful
func (m *FilesDirWithPathItemRequestBuilder) ToGetRequestInformation(ctx context.Context, requestConfiguration *FilesDirWithPathItemRequestBuilderGetRequestConfiguration)(*i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.RequestInformation, error) {
    requestInfo := i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.NewRequestInformationWithMethodAndUrlTemplateAndPathParameters(i2ae4187f7daee263371cb1c977df639813ab50ffa529013b7437480d1ec0158f.GET, m.BaseRequestBuilder.UrlTemplate, m.BaseRequestBuilder.PathParameters)
    if requestConfiguration != nil {
        requestInfo.Headers.AddAll(requestConfiguration.Headers)
        requestInfo.AddRequestOptions(requestConfiguration.Options)
    }
    requestInfo.Headers.TryAdd("Accept", "application/json")
    return requestInfo, nil
}
// WithUrl returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
// returns a *FilesDirWithPathItemRequestBuilder when successful
func (m *FilesDirWithPathItemRequestBuilder) WithUrl(rawUrl string)(*FilesDirWithPathItemRequestBuilder) {
    return NewFilesDirWithPathItemRequestBuilder(rawUrl, m.BaseRequestBuilder.RequestAdapter);
}
