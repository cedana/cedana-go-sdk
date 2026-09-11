from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.checkpoint_request_view import CheckpointRequestView
    from ......models.http_error import HttpError
    from ......models.request_checkpoint import RequestCheckpoint
    from ......models.update_checkpoint_request import UpdateCheckpointRequest

class CheckpointRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/profiles/{profile_id}/checkpoint
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CheckpointRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/profiles/{profile_id}/checkpoint", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CheckpointRequestView]:
        """
        The latest checkpoint request for a profile, outstanding or finished
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CheckpointRequestView]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.checkpoint_request_view import CheckpointRequestView

        return await self.request_adapter.send_async(request_info, CheckpointRequestView, error_mapping)
    
    async def patch(self,body: UpdateCheckpointRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CheckpointRequestView]:
        """
        Report progress on a checkpoint request (controller only)
        param body: What the controller reports back about a request it picked up.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CheckpointRequestView]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ......models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "404": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.checkpoint_request_view import CheckpointRequestView

        return await self.request_adapter.send_async(request_info, CheckpointRequestView, error_mapping)
    
    async def post(self,body: RequestCheckpoint, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CheckpointRequestView]:
        """
        Ask for a checkpoint of this profile's worker now. Covers the two cases theautomatic path refuses: a restored worker, and replacing an existing checkpoint.
        param body: What a caller asks for when it wants a checkpoint taken now.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CheckpointRequestView]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": HttpError,
            "409": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.checkpoint_request_view import CheckpointRequestView

        return await self.request_adapter.send_async(request_info, CheckpointRequestView, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        The latest checkpoint request for a profile, outstanding or finished
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: UpdateCheckpointRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Report progress on a checkpoint request (controller only)
        param body: What the controller reports back about a request it picked up.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PATCH, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_post_request_information(self,body: RequestCheckpoint, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Ask for a checkpoint of this profile's worker now. Covers the two cases theautomatic path refuses: a restored worker, and replacing an existing checkpoint.
        param body: What a caller asks for when it wants a checkpoint taken now.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> CheckpointRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: CheckpointRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return CheckpointRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class CheckpointRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CheckpointRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class CheckpointRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

