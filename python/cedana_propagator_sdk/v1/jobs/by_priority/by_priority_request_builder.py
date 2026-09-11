from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_priority_item_request_builder import WithPriorityItemRequestBuilder

class ByPriorityRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/jobs/by-priority
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new ByPriorityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/jobs/by-priority", path_parameters)
    
    def by_priority(self,priority: int) -> WithPriorityItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.jobs.byPriority.item collection
        param priority: Priority value to filter jobs by
        Returns: WithPriorityItemRequestBuilder
        """
        if priority is None:
            raise TypeError("priority cannot be null.")
        from .item.with_priority_item_request_builder import WithPriorityItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["priority"] = priority
        return WithPriorityItemRequestBuilder(self.request_adapter, url_tpl_params)
    

