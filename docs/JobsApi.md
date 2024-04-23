# waylay.services.registry.JobsApi

All URIs are relative to *https://api-aws-dev.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events**](JobsApi.md#events) | **GET** /registry/v2/jobs/events | Stream Events
[**get**](JobsApi.md#get) | **GET** /registry/v2/jobs/{type}/{id} | Get Job
[**list**](JobsApi.md#list) | **GET** /registry/v2/jobs/ | List Jobs

# **events**
> events(
> query: EventsQuery,
> headers
> ) -> AsyncIterator[EventWithCloseSSE]

Stream Events

Get an SSE stream of all job events for the users tenant.  The stream can be filtered on job type or on a specific job id.   When filtering on job id, the server will send a <code>close</code> event  upon completion of the job. The client should handle this event by closing the stream.  

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.event_with_close_sse import EventWithCloseSSE
from waylay.services.registry.models.job_type import JobType
try:
    # Stream Events
    # calls `GET /registry/v2/jobs/events`
    api_response = await waylay_client.registry.jobs.events(
        # query parameters:
        query = {
            'type': 'build'
            'children': True
        },
    )
    print("The response of registry.jobs.events:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.jobs.events: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/jobs/events
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['type']** (dict) <br> **query.type** (Query) | [**JobType**](.md) | query parameter `"type"` | The type of the job. | [optional] 
**query['id']** (dict) <br> **query.id** (Query) | **str** | query parameter `"id"` | The id of the job. | [optional] 
**query['children']** (dict) <br> **query.children** (Query) | **bool** | query parameter `"children"` | If set to &lt;code&gt;true&lt;/code&gt;, the event stream will include events of the job&#39;s dependants. E.g., when subscribing to a verify job with &#x60;children&#x3D;true&#x60;, you will also receive the events of the underlying build and deploy jobs. Defaults to &lt;code&gt;false&lt;/code&gt;. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`AsyncIterator[EventWithCloseSSE]`** |  | [EventWithCloseSSE](EventWithCloseSSE.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/event-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events Streaming |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> type: JobType,
> id: str,
> headers
> ) -> JobResponse

Get Job

Get a background job by type and id.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.job_response import JobResponse
from waylay.services.registry.models.job_type import JobType
try:
    # Get Job
    # calls `GET /registry/v2/jobs/{type}/{id}`
    api_response = await waylay_client.registry.jobs.get(
        'build', # type | path param "type"
        'id_example', # id | path param "id"
    )
    print("The response of registry.jobs.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.jobs.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/jobs/{type}/{id}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**type** | [**JobType**](.md) | path parameter `"type"` |  | 
**id** | **str** | path parameter `"id"` |  | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`JobResponse`** |  | [JobResponse](JobResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> JobsResponse

List Jobs

List all background jobs for the users tenant.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_type_schema import JobTypeSchema
from waylay.services.registry.models.jobs_response import JobsResponse
try:
    # List Jobs
    # calls `GET /registry/v2/jobs/`
    api_response = await waylay_client.registry.jobs.list(
        # query parameters:
        query = {
        },
    )
    print("The response of registry.jobs.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.jobs.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/jobs/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** (dict) <br> **query.limit** (Query) | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['type']** (dict) <br> **query.type** (Query) | [**List[JobTypeSchema]**](JobTypeSchema.md) | query parameter `"type"` | Filter on job type | [optional] 
**query['state']** (dict) <br> **query.state** (Query) | [**List[JobStateResult]**](JobStateResult.md) | query parameter `"state"` | Filter on job state | [optional] 
**query['functionType']** (dict) <br> **query.function_type** (Query) | [**List[FunctionType]**](FunctionType.md) | query parameter `"functionType"` | Filter on function type | [optional] 
**query['createdBefore']** (dict) <br> **query.created_before** (Query) | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on jobs that created before the given timestamp or age | [optional] 
**query['createdAfter']** (dict) <br> **query.created_after** (Query) | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on jobs that created after the given timestamp or age | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`JobsResponse`** |  | [JobsResponse](JobsResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

