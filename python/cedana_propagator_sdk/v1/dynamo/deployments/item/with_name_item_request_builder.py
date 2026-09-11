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
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from .....models.dynamo_deployment_view import DynamoDeploymentView
    from .....models.http_error import HttpError
    from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder
    from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder
    from .metrics.metrics_request_builder import MetricsRequestBuilder
    from .pod_startup_times.pod_startup_times_request_builder import PodStartupTimesRequestBuilder
    from .scrape.scrape_request_builder import ScrapeRequestBuilder
    from .startup_comparison.startup_comparison_request_builder import StartupComparisonRequestBuilder

class WithNameItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/dynamo/deployments/{name}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithNameItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/dynamo/deployments/{name}?cluster_id={cluster_id}{&namespace*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[WithNameItemRequestBuilderDeleteQueryParameters]] = None) -> Optional[str]:
        """
        Publishes a delete event for the DynamoGraphDeployment and removes the DB record.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "404": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithNameItemRequestBuilderGetQueryParameters]] = None) -> Optional[DynamoDeploymentView]:
        """
        Returns a single DynamoGraphDeployment by name.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[DynamoDeploymentView]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from .....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "404": HttpError,
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.dynamo_deployment_view import DynamoDeploymentView

        return await self.request_adapter.send_async(request_info, DynamoDeploymentView, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[WithNameItemRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Publishes a delete event for the DynamoGraphDeployment and removes the DB record.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithNameItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a single DynamoGraphDeployment by name.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithNameItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithNameItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithNameItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def checkpoint(self) -> CheckpointRequestBuilder:
        """
        The checkpoint property
        """
        from .checkpoint.checkpoint_request_builder import CheckpointRequestBuilder

        return CheckpointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkpoints(self) -> CheckpointsRequestBuilder:
        """
        The checkpoints property
        """
        from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder

        return CheckpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def metrics(self) -> MetricsRequestBuilder:
        """
        The metrics property
        """
        from .metrics.metrics_request_builder import MetricsRequestBuilder

        return MetricsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pod_startup_times(self) -> PodStartupTimesRequestBuilder:
        """
        The podStartupTimes property
        """
        from .pod_startup_times.pod_startup_times_request_builder import PodStartupTimesRequestBuilder

        return PodStartupTimesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def scrape(self) -> ScrapeRequestBuilder:
        """
        The scrape property
        """
        from .scrape.scrape_request_builder import ScrapeRequestBuilder

        return ScrapeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startup_comparison(self) -> StartupComparisonRequestBuilder:
        """
        The startupComparison property
        """
        from .startup_comparison.startup_comparison_request_builder import StartupComparisonRequestBuilder

        return StartupComparisonRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithNameItemRequestBuilderDeleteQueryParameters():
        """
        Publishes a delete event for the DynamoGraphDeployment and removes the DB record.
        """
        # UUID of the cluster to filter by
        cluster_id: Optional[UUID] = None

        # Kubernetes namespace
        namespace: Optional[str] = None

    
    @dataclass
    class WithNameItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[WithNameItemRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithNameItemRequestBuilderGetQueryParameters():
        """
        Returns a single DynamoGraphDeployment by name.
        """
        # UUID of the cluster to filter by
        cluster_id: Optional[UUID] = None

        # Kubernetes namespace
        namespace: Optional[str] = None

    
    @dataclass
    class WithNameItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithNameItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

