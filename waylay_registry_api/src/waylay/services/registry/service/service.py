"""Registry Service."""

from waylay.sdk import (
    ApiClient, WaylayService
)

from ..api.jobs_api import JobsApi
from ..api.model_functions_api import ModelFunctionsApi
from ..api.plug_functions_api import PlugFunctionsApi
from ..api.runtimes_api import RuntimesApi
from ..api.schemas_api import SchemasApi
from ..api.webscript_functions_api import WebscriptFunctionsApi
from ..api.default_api import DefaultApi


class RegistryService(WaylayService):
    """Registry Service Class."""

    jobs: JobsApi
    model_functions: ModelFunctionsApi
    plug_functions: PlugFunctionsApi
    runtimes: RuntimesApi
    schemas: SchemasApi
    webscript_functions: WebscriptFunctionsApi
    default: DefaultApi

    def __init__(self, api_client: ApiClient, *args, **kwargs):
        """Create the registry service."""

        super().__init__(api_client, *args, **kwargs)
        self.jobs = JobsApi(api_client)
        self.model_functions = ModelFunctionsApi(api_client)
        self.plug_functions = PlugFunctionsApi(api_client)
        self.runtimes = RuntimesApi(api_client)
        self.schemas = SchemasApi(api_client)
        self.webscript_functions = WebscriptFunctionsApi(api_client)
        self.default = DefaultApi(api_client)

    def configure(self, api_client: ApiClient, *args, **kwargs):
        """Configure the registry service with updated client configuration."""
        super().configure(api_client, *args, **kwargs)
        self.jobs._api_client = (api_client)
        self.model_functions._api_client = (api_client)
        self.plug_functions._api_client = (api_client)
        self.runtimes._api_client = (api_client)
        self.schemas._api_client = (api_client)
        self.webscript_functions._api_client = (api_client)
        self.default._api_client = (api_client)
