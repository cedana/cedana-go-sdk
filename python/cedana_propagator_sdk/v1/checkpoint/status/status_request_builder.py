from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_action_item_request_builder import WithAction_ItemRequestBuilder

class StatusRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/checkpoint/status
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StatusRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/checkpoint/status", path_parameters)
    
    def by_action_id(self,action_id: str) -> WithAction_ItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.checkpoint.status.item collection
        param action_id: Unique identifier of the item
        Returns: WithAction_ItemRequestBuilder
        """
        if action_id is None:
            raise TypeError("action_id cannot be null.")
        from .item.with_action_item_request_builder import WithAction_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["action_id"] = action_id
        return WithAction_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    

