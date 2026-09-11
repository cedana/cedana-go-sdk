from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item.operations_item_request_builder import OperationsItemRequestBuilder

class OperationsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/operations
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new OperationsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/operations", path_parameters)
    
    def by_id(self,id: UUID) -> OperationsItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.operations.item collection
        param id: Checkpoint id or restore uuid
        Returns: OperationsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.operations_item_request_builder import OperationsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return OperationsItemRequestBuilder(self.request_adapter, url_tpl_params)
    

