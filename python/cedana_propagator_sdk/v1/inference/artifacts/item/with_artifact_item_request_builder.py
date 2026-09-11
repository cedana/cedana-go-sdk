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
    from .....models.checkpoint_artifact_view import CheckpointArtifactView
    from .....models.http_error import HttpError
    from .....models.update_artifact import UpdateArtifact
    from .ancestry.ancestry_request_builder import AncestryRequestBuilder
    from .promote.promote_request_builder import PromoteRequestBuilder

class WithArtifact_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/artifacts/{artifact_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithArtifact_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/artifacts/{artifact_id}{?force*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[WithArtifact_ItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[bytes]:
        """
        Soft-delete an artefact (golden requires force)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": HttpError,
            "409": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CheckpointArtifactView]:
        """
        Get a checkpoint artefact
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CheckpointArtifactView]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.checkpoint_artifact_view import CheckpointArtifactView

        return await self.request_adapter.send_async(request_info, CheckpointArtifactView, error_mapping)
    
    async def patch(self,body: UpdateArtifact, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CheckpointArtifactView]:
        """
        Update artefact status / restore count
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CheckpointArtifactView]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "404": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.checkpoint_artifact_view import CheckpointArtifactView

        return await self.request_adapter.send_async(request_info, CheckpointArtifactView, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[WithArtifact_ItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Soft-delete an artefact (golden requires force)
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Get a checkpoint artefact
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_patch_request_information(self,body: UpdateArtifact, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Update artefact status / restore count
        param body: The request body
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
    
    def with_url(self,raw_url: str) -> WithArtifact_ItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithArtifact_ItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithArtifact_ItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def ancestry(self) -> AncestryRequestBuilder:
        """
        The ancestry property
        """
        from .ancestry.ancestry_request_builder import AncestryRequestBuilder

        return AncestryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def promote(self) -> PromoteRequestBuilder:
        """
        The promote property
        """
        from .promote.promote_request_builder import PromoteRequestBuilder

        return PromoteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithArtifact_ItemRequestBuilderDeleteQueryParameters():
        """
        Soft-delete an artefact (golden requires force)
        """
        force: Optional[bool] = None

    
    @dataclass
    class WithArtifact_ItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[WithArtifact_ItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithArtifact_ItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithArtifact_ItemRequestBuilderPatchRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

