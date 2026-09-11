from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .job.job_request_builder import JobRequestBuilder
    from .path.path_request_builder import PathRequestBuilder

class CheckpointRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/slurm/checkpoint
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new CheckpointRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/slurm/checkpoint", path_parameters)
    
    @property
    def job(self) -> JobRequestBuilder:
        """
        The job property
        """
        from .job.job_request_builder import JobRequestBuilder

        return JobRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def path(self) -> PathRequestBuilder:
        """
        The path property
        """
        from .path.path_request_builder import PathRequestBuilder

        return PathRequestBuilder(self.request_adapter, self.path_parameters)
    

