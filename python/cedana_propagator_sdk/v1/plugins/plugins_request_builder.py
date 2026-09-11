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
    from ...models.http_error import HttpError
    from ...models.plugin import Plugin
    from .download.download_request_builder import DownloadRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class PluginsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/plugins
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PluginsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/plugins{?arch*,build*,compatibility*,names*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PluginsRequestBuilderGetQueryParameters]] = None) -> Optional[list[Plugin]]:
        """
        Supports direct query params (`names`, `compatibility`, `arch`, `build`)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Plugin]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.plugin import Plugin

        return await self.request_adapter.send_collection_async(request_info, Plugin, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PluginsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Supports direct query params (`names`, `compatibility`, `arch`, `build`)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> PluginsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PluginsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PluginsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def download(self) -> DownloadRequestBuilder:
        """
        The download property
        """
        from .download.download_request_builder import DownloadRequestBuilder

        return DownloadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PluginsRequestBuilderGetQueryParameters():
        """
        Supports direct query params (`names`, `compatibility`, `arch`, `build`)
        """
        # Architecture, e.g. amd64
        arch: Optional[str] = None

        # Build type: alpha|release
        build: Optional[str] = None

        # Exact version match, e.g. 0.9.2
        compatibility: Optional[str] = None

        # Comma-separated plugin names, e.g. cedana,runc; each may pin a version with name@version
        names: Optional[str] = None

    
    @dataclass
    class PluginsRequestBuilderGetRequestConfiguration(RequestConfiguration[PluginsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

