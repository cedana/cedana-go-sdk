from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .create.create_request_builder import CreateRequestBuilder
    from .item.with_policy_item_request_builder import WithPolicy_ItemRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder

class PipelineRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/policy/pipeline
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new PipelineRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/policy/pipeline", path_parameters)
    
    def by_policy_id(self,policy_id: UUID) -> WithPolicy_ItemRequestBuilder:
        """
        Gets an item from the cedana_propagator_sdk.v1.policy.pipeline.item collection
        param policy_id: Policy UUID
        Returns: WithPolicy_ItemRequestBuilder
        """
        if policy_id is None:
            raise TypeError("policy_id cannot be null.")
        from .item.with_policy_item_request_builder import WithPolicy_ItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["policy_id"] = policy_id
        return WithPolicy_ItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def create(self) -> CreateRequestBuilder:
        """
        The create property
        """
        from .create.create_request_builder import CreateRequestBuilder

        return CreateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        The list property
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    

