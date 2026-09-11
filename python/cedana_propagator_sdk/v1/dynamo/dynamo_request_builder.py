from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder
    from .deploy.deploy_request_builder import DeployRequestBuilder
    from .deployments.deployments_request_builder import DeploymentsRequestBuilder

class DynamoRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /v1/dynamo
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DynamoRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/v1/dynamo", path_parameters)
    
    @property
    def checkpoints(self) -> CheckpointsRequestBuilder:
        """
        The checkpoints property
        """
        from .checkpoints.checkpoints_request_builder import CheckpointsRequestBuilder

        return CheckpointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deploy(self) -> DeployRequestBuilder:
        """
        The deploy property
        """
        from .deploy.deploy_request_builder import DeployRequestBuilder

        return DeployRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deployments(self) -> DeploymentsRequestBuilder:
        """
        The deployments property
        """
        from .deployments.deployments_request_builder import DeploymentsRequestBuilder

        return DeploymentsRequestBuilder(self.request_adapter, self.path_parameters)
    

