# coding: utf-8
"""Waylay Function Registry api.

This code was generated from the OpenAPI documentation of 'Waylay Function Registry'

Generated by OpenAPI Generator (https://openapi-generator.tech)

Do not edit the class manually.
"""

from __future__ import annotations  # for Python 3.7–3.9
import io
import warnings

import enum
from enum import Enum
from pydantic import (
    validate_call,
    Field,
    StrictFloat,
    StrictStr,
    StrictInt,
    StrictBool,
    StrictBytes,
    ConfigDict,
    TypeAdapter,
)
from typing import (
    Dict,
    List,
    Literal,
    Optional,
    Tuple,
    Union,
    Any,
    overload,
    TYPE_CHECKING,
    Type,
    TypeVar,
)
from typing_extensions import (
    Annotated,  # >=3.9,
    NotRequired,  # >=3.11
)

from waylay.sdk.plugin import WithApiClient
from waylay.sdk.api import (
    ApiValueError,
    Request,
    Response,
    HeaderTypes,
    QueryParamTypes,
    RequestFiles,
    RequestData,
    RequestContent,
)
from waylay.sdk.api._models import Model

if TYPE_CHECKING:
    from waylay.services.registry.queries.jobs_api import EventsQuery

    from waylay.services.registry.models import EventWithCloseSSE

    from waylay.services.registry.models import EventWithCloseSSE

    from waylay.services.registry.models import JobType

    from waylay.services.registry.queries.jobs_api import GetQuery

    from waylay.services.registry.models import JobResponse

    from waylay.services.registry.models import JobResponse

    from waylay.services.registry.queries.jobs_api import ListQuery

    from waylay.services.registry.models import JobsResponse

    from waylay.services.registry.models import JobsResponse


try:
    from waylay.services.registry.queries.jobs_api import EventsQuery

    from waylay.services.registry.models import EventWithCloseSSE

    from waylay.services.registry.models import EventWithCloseSSE

    from waylay.services.registry.models import JobType

    from waylay.services.registry.queries.jobs_api import GetQuery

    from waylay.services.registry.models import JobResponse

    from waylay.services.registry.models import JobResponse

    from waylay.services.registry.queries.jobs_api import ListQuery

    from waylay.services.registry.models import JobsResponse

    from waylay.services.registry.models import JobsResponse

    MODELS_AVAILABLE = True
except ImportError:
    MODELS_AVAILABLE = False

    if not TYPE_CHECKING:
        EventsQuery = dict

        EventWithCloseSSE = Model

        JobType = str

        GetQuery = dict

        JobResponse = Model

        ListQuery = dict

        JobsResponse = Model


from waylay.sdk.api import ApiClient, RESTTimeout

T = TypeVar("T")


class JobsApi(WithApiClient):
    """JobsApi service methods.

    NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    @overload
    async def events(
        self,
        *,
        query: EventsQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> EventWithCloseSSE: ...

    @overload
    async def events(
        self,
        *,
        query: EventsQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def events(
        self,
        *,
        query: EventsQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def events(
        self,
        *,
        query: EventsQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def events(
        self,
        *,
        query: EventsQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def events(
        self,
        *,
        query: EventsQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> EventWithCloseSSE | T | Response | Model:
        """Stream Events.

        Get an SSE stream of all job events for the users tenant.  The stream can be filtered on job type or on a specific job id.   When filtering on job id, the server will send a <code>close</code> event  upon completion of the job. The client should handle this event by closing the stream.
        :param query: URL Query parameters.
        :type query: EventsQuery | QueryParamTypes, optional
        :param query['type'] (dict) <br> query.type (Query) : The type of the job.
        :type query['type']: JobType
        :param query['id'] (dict) <br> query.id (Query) : The id of the job.
        :type query['id']: str
        :param query['children'] (dict) <br> query.children (Query) : If set to <code>true</code>, the event stream will include events of the job's dependants. E.g., when subscribing to a verify job with `children=true`, you will also receive the events of the underlying build and deploy jobs. Defaults to <code>false</code>.
        :type query['children']: bool
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(EventsQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": EventWithCloseSSE if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/registry/v2/jobs/events",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def get(
        self,
        type: JobType,
        id: StrictStr,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> JobResponse: ...

    @overload
    async def get(
        self,
        type: JobType,
        id: StrictStr,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def get(
        self,
        type: JobType,
        id: StrictStr,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def get(
        self,
        type: JobType,
        id: StrictStr,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def get(
        self,
        type: JobType,
        id: StrictStr,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def get(
        self,
        type: JobType,
        id: StrictStr,
        *,
        query: GetQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> JobResponse | T | Response | Model:
        """Get Job.

        Get a background job by type and id.
        :param type: (required)
        :type type: JobType
        :param id: (required)
        :type id: str
        :param query: URL Query parameters.
        :type query: GetQuery | QueryParamTypes, optional
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {
            "type": str(type),
            "id": str(id),
        }

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(GetQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": JobResponse if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/registry/v2/jobs/{type}/{id}",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> JobsResponse: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: Literal[""] = "",
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[True],
        select_path: Literal["_not_used_"] = "_not_used_",
        response_type: Literal[None] = None,  # not used
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Response: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: Literal[None] = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> Model: ...

    @overload
    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: Literal[False] = False,
        select_path: str,
        response_type: T,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> T: ...

    async def list(
        self,
        *,
        query: ListQuery | QueryParamTypes | None = None,
        raw_response: StrictBool = False,
        select_path: str = "",
        response_type: T | None = None,
        headers: HeaderTypes | None = None,
        **kwargs,
    ) -> JobsResponse | T | Response | Model:
        """List Jobs.

        List all background jobs for the users tenant.
        :param query: URL Query parameters.
        :type query: ListQuery | QueryParamTypes, optional
        :param query['limit'] (dict) <br> query.limit (Query) : The maximum number of items to be return from this query. Has a deployment-defined default and maximum value.
        :type query['limit']: float
        :param query['type'] (dict) <br> query.type (Query) : Filter on job type
        :type query['type']: List[JobTypeSchema]
        :param query['state'] (dict) <br> query.state (Query) : Filter on job state
        :type query['state']: List[JobStateResult]
        :param query['functionType'] (dict) <br> query.function_type (Query) : Filter on function type
        :type query['functionType']: List[FunctionType]
        :param query['createdBefore'] (dict) <br> query.created_before (Query) : Filter on jobs that created before the given timestamp or age
        :type query['createdBefore']: TimestampSpec
        :param query['createdAfter'] (dict) <br> query.created_after (Query) : Filter on jobs that created after the given timestamp or age
        :type query['createdAfter']: TimestampSpec
        :param raw_response: If true, return the http Response object instead of returning an api model object, or throwing an ApiError.
        :param select_path: Denotes the json path applied to the response object before returning it.
                Set it to the empty string `""` to receive the full response object.
        :param response_type: If specified, the response is parsed into an instance of the specified type.
        :param headers: Header parameters for this request
        :type headers: dict, optional
        :param `**kwargs`: Additional parameters passed on to the http client.
            See below.
        :Keyword Arguments:
            * timeout: a single numeric timeout in seconds,
                or a tuple of _connect_, _read_, _write_ and _pool_ timeouts.
            * stream: if true, the response will be in streaming mode
            * cookies
            * extensions
            * auth
            * follow_redirects: bool

        :return: Returns the result object if the http request succeeded with status code '2XX'.
        :raises APIError: If the http request has a status code different from `2XX`. This
            object wraps both the http Response and any parsed data.
        """

        should_validate = (
            MODELS_AVAILABLE and self.api_client.config.client_side_validation
        )

        # path parameters
        path_params: Dict[str, str] = {}

        ## named body parameters
        body_args: Dict[str, Any] = {}

        # query parameters
        if query is not None and should_validate:
            query = TypeAdapter(ListQuery).validate_python(query)

        response_types_map: Dict[str, Any] = (
            {"2XX": response_type}
            if response_type is not None
            else {
                "200": JobsResponse if not select_path else Model,
            }
        )
        non_200_response_types_map: Dict[str, Any] = {}
        response_types_map.update(non_200_response_types_map)

        ## peform request
        return await self.api_client.request(
            method="GET",
            resource_path="/registry/v2/jobs/",
            path_params=path_params,
            params=query,
            **body_args,
            headers=headers,
            **kwargs,
            response_types_map=response_types_map,
            select_path=select_path,
            raw_response=raw_response,
        )