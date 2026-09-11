from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .restore_error.restore_error_request_builder import Restore_errorRequestBuilder
    from .restore_start.restore_start_request_builder import Restore_startRequestBuilder
    from .restore_success.restore_success_request_builder import Restore_successRequestBuilder

class EventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/restores/events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/restores/events", path_parameters)
    
    @property
    def restore_error(self) -> Restore_errorRequestBuilder:
        """
        The restore_error property
        """
        from .restore_error.restore_error_request_builder import Restore_errorRequestBuilder

        return Restore_errorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_start(self) -> Restore_startRequestBuilder:
        """
        The restore_start property
        """
        from .restore_start.restore_start_request_builder import Restore_startRequestBuilder

        return Restore_startRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore_success(self) -> Restore_successRequestBuilder:
        """
        The restore_success property
        """
        from .restore_success.restore_success_request_builder import Restore_successRequestBuilder

        return Restore_successRequestBuilder(self.request_adapter, self.path_parameters)
    

