from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .activity.activity_request_builder import ActivityRequestBuilder
    from .jobs.jobs_request_builder import JobsRequestBuilder
    from .job_status.job_status_request_builder import JobStatusRequestBuilder
    from .pods.pods_request_builder import PodsRequestBuilder

class WithPolicy_ItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/policy/{policy_id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithPolicy_ItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/policy/{policy_id}", path_parameters)
    
    @property
    def activity(self) -> ActivityRequestBuilder:
        """
        The activity property
        """
        from .activity.activity_request_builder import ActivityRequestBuilder

        return ActivityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def job_status(self) -> JobStatusRequestBuilder:
        """
        The jobStatus property
        """
        from .job_status.job_status_request_builder import JobStatusRequestBuilder

        return JobStatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def jobs(self) -> JobsRequestBuilder:
        """
        The jobs property
        """
        from .jobs.jobs_request_builder import JobsRequestBuilder

        return JobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pods(self) -> PodsRequestBuilder:
        """
        The pods property
        """
        from .pods.pods_request_builder import PodsRequestBuilder

        return PodsRequestBuilder(self.request_adapter, self.path_parameters)
    

