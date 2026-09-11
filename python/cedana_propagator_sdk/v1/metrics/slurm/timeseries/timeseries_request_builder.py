from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cpu_load.cpu_load_request_builder import CpuLoadRequestBuilder
    from .memory.memory_request_builder import MemoryRequestBuilder

class TimeseriesRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/metrics/slurm/timeseries
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new TimeseriesRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/metrics/slurm/timeseries", path_parameters)
    
    @property
    def cpu_load(self) -> CpuLoadRequestBuilder:
        """
        The cpuLoad property
        """
        from .cpu_load.cpu_load_request_builder import CpuLoadRequestBuilder

        return CpuLoadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def memory(self) -> MemoryRequestBuilder:
        """
        The memory property
        """
        from .memory.memory_request_builder import MemoryRequestBuilder

        return MemoryRequestBuilder(self.request_adapter, self.path_parameters)
    

