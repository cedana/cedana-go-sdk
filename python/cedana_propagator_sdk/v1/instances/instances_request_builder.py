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
    from ...models.create_instance_request import CreateInstanceRequest
    from ...models.create_instance_response import CreateInstanceResponse
    from ...models.http_error import HttpError
    from ...models.instance_info import InstanceInfo
    from .bursting_status.bursting_status_request_builder import BurstingStatusRequestBuilder
    from .item.with_instance_item_request_builder import WithInstance_ItemRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class InstancesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/instances
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new InstancesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/instances", path_parameters)
    
    def by_instance_id(self,instance_id: str) -> WithInstance_ItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.instances.item collection
        param instance_id: Instance ID to delete
        Returns: WithInstance_ItemRequestBuilder
        """
        if instance_id is None:
            raise TypeError("instance_id cannot be null.")
        from .item.with_instance_item_request_builder import WithInstance_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["instance_id"] = instance_id
        return WithInstance_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[InstanceInfo]]:
        """
        List instances
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[InstanceInfo]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.instance_info import InstanceInfo

        return await self.request_adapter.send_collection_async(request_info, InstanceInfo, error_mapping)
    
    async def post(self,body: CreateInstanceRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CreateInstanceResponse]:
        """
        Create instance
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CreateInstanceResponse]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ...models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.create_instance_response import CreateInstanceResponse

        return await self.request_adapter.send_async(request_info, CreateInstanceResponse, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        List instances
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateInstanceRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create instance
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> InstancesRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: InstancesRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return InstancesRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bursting_status(self) -> BurstingStatusRequestBuilder:
        """
        The burstingStatus property
        """
        from .bursting_status.bursting_status_request_builder import BurstingStatusRequestBuilder

        return BurstingStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class InstancesRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class InstancesRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

