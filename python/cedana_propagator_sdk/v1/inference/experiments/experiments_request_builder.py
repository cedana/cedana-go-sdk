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
    from ....models.create_experiment import CreateExperiment
    from ....models.experiment import Experiment
    from ....models.experiment_summary import ExperimentSummary
    from ....models.http_error import HttpError
    from .item.experiments_item_request_builder import ExperimentsItemRequestBuilder

class ExperimentsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/inference/experiments
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ExperimentsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/inference/experiments", path_parameters)
    
    def by_id(self,id: UUID) -> ExperimentsItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.inference.experiments.item collection
        param id: Experiment ID
        Returns: ExperimentsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.experiments_item_request_builder import ExperimentsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ExperimentsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[ExperimentSummary]]:
        """
        List experiments
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[ExperimentSummary]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.experiment_summary import ExperimentSummary

        return await self.request_adapter.send_collection_async(request_info, ExperimentSummary, error_mapping)
    
    async def post(self,body: CreateExperiment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[Experiment]:
        """
        Create a load-test experiment
        param body: The request body
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[Experiment]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        from ....models.http_error import HttpError

        error_mapping: dict[str, type[ParsableFactory]] = {
            "400": HttpError,
            "XXX": HttpError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.experiment import Experiment

        return await self.request_adapter.send_async(request_info, Experiment, error_mapping)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        List experiments
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def to_post_request_information(self,body: CreateExperiment, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Create a load-test experiment
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
    
    def with_url(self,raw_url: str) -> ExperimentsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ExperimentsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ExperimentsRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ExperimentsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ExperimentsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

