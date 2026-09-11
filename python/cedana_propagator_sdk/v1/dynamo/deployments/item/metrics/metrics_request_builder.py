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
    from ......models.dynamo_metrics_ingest_request import DynamoMetricsIngestRequest
    from ......models.dynamo_metric_point import DynamoMetricPoint
    from ......models.http_error import HttpError

class MetricsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/dynamo/deployments/{name}/metrics
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new MetricsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/dynamo/deployments/{name}/metrics{?cluster_id*,from_ms*,hours*,namespace*,to_ms*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MetricsRequestBuilderGetQueryParameters]] = None) -> Optional[list[DynamoMetricPoint]]:
        """
        Query Dynamo inference metrics for a deployment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[DynamoMetricPoint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ......models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.dynamo_metric_point import DynamoMetricPoint

        return await self.request_adapter.send_collection_async(request_info, DynamoMetricPoint, error_mapping)
    
    async def post(self,body: DynamoMetricsIngestRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[str]:
        """
        Ingest a batch of Dynamo inference metrics from the watcher.
        param body: Batch of metric samples posted by the watcher after scraping /metrics.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ......models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "500": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "str", error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MetricsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Query Dynamo inference metrics for a deployment.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: DynamoMetricsIngestRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Ingest a batch of Dynamo inference metrics from the watcher.
        param body: Batch of metric samples posted by the watcher after scraping /metrics.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> MetricsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MetricsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MetricsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MetricsRequestBuilderGetQueryParameters():
        """
        Query Dynamo inference metrics for a deployment.
        """
        cluster_id: Optional[str] = None

        # Optional absolute range start (Unix ms). If set with `to_ms`, overrides `hours`.
        from_ms: Optional[int] = None

        # Relative window in hours (default 1, max 720 = metrics TTL). Ignored when`from_ms`/`to_ms` are set. Anchored to the LATEST datapoint (not now()) soa deleted deployment still returns its historical data.
        hours: Optional[int] = None

        namespace: Optional[str] = None

        # Optional absolute range end (Unix ms). If set with `from_ms`, overrides `hours`.
        to_ms: Optional[int] = None

    
    @dataclass
    class MetricsRequestBuilderGetRequestConfiguration(RequestConfiguration[MetricsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MetricsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

