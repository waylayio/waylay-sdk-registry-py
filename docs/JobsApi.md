# waylay.services.registry.JobsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events**](JobsApi.md#events) | **GET** /registry/v2/jobs/events | Stream Events
[**get**](JobsApi.md#get) | **GET** /registry/v2/jobs/{type}/{id} | Get Job
[**list**](JobsApi.md#list) | **GET** /registry/v2/jobs/ | List Jobs


# **events**
> EventWithCloseSSE events(type=type, id=id, children=children)

Stream Events

Get an SSE stream of all job events for the users tenant.  The stream can be filtered on job type or on a specific job id.   When filtering on job id, the server will send a <code>close</code> event  upon completion of the job. The client should handle this event by closing the stream.  

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.event_with_close_sse import EventWithCloseSSE
from waylay.services.registry.models.job_type import JobType
from waylay.services.registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.waylay.io
# See configuration.py for a list of all supported configuration parameters.
configuration = waylay.services.registry.Configuration(
    host = "https://api.waylay.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: waylayApiKeySecret
configuration = waylay.services.registry.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with waylay.services.registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waylay.services.registry.JobsApi(api_client)
    type = waylay.services.registry.JobType() # JobType | The type of the job. (optional)
    id = 'id_example' # str | The id of the job. (optional)
    children = True # bool | If set to <code>true</code>, the event stream will include events of the job's dependants. E.g., when subscribing to a verify job with `children=true`, you will also receive the events of the underlying build and deploy jobs. Defaults to <code>false</code>. (optional)

    try:
        # Stream Events
        api_response = await api_instance.events(type=type, id=id, children=children)
        print("The response of JobsApi->events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**JobType**](.md)| The type of the job. | [optional] 
 **id** | **str**| The id of the job. | [optional] 
 **children** | **bool**| If set to &lt;code&gt;true&lt;/code&gt;, the event stream will include events of the job&#39;s dependants. E.g., when subscribing to a verify job with &#x60;children&#x3D;true&#x60;, you will also receive the events of the underlying build and deploy jobs. Defaults to &lt;code&gt;false&lt;/code&gt;. | [optional] 

### Return type

[**EventWithCloseSSE**](EventWithCloseSSE.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/eventstream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Events Streaming |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> JobResponse get(type, id)

Get Job

Get a background job by type and id.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.job_response import JobResponse
from waylay.services.registry.models.job_type import JobType
from waylay.services.registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.waylay.io
# See configuration.py for a list of all supported configuration parameters.
configuration = waylay.services.registry.Configuration(
    host = "https://api.waylay.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: waylayApiKeySecret
configuration = waylay.services.registry.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with waylay.services.registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waylay.services.registry.JobsApi(api_client)
    type = waylay.services.registry.JobType() # JobType | 
    id = 'id_example' # str | 

    try:
        # Get Job
        api_response = await api_instance.get(type, id)
        print("The response of JobsApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**JobType**](.md)|  | 
 **id** | **str**|  | 

### Return type

[**JobResponse**](JobResponse.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> JobsResponse list(limit=limit, type=type, state=state, function_type=function_type, created_before=created_before, created_after=created_after)

List Jobs

List all background jobs for the users tenant.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_type_schema import JobTypeSchema
from waylay.services.registry.models.jobs_response import JobsResponse
from waylay.services.registry.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.waylay.io
# See configuration.py for a list of all supported configuration parameters.
configuration = waylay.services.registry.Configuration(
    host = "https://api.waylay.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: waylayApiKeySecret
configuration = waylay.services.registry.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with waylay.services.registry.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = waylay.services.registry.JobsApi(api_client)
    limit = 3.4 # float | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. (optional)
    type = [waylay.services.registry.JobTypeSchema()] # List[JobTypeSchema] | Filter on job type (optional)
    state = [waylay.services.registry.JobStateResult()] # List[JobStateResult] | Filter on job state (optional)
    function_type = [waylay.services.registry.FunctionType()] # List[FunctionType] | Filter on function type (optional)
    created_before = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on jobs that created before the given timestamp or age (optional)
    created_after = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on jobs that created after the given timestamp or age (optional)

    try:
        # List Jobs
        api_response = await api_instance.list(limit=limit, type=type, state=state, function_type=function_type, created_before=created_before, created_after=created_after)
        print("The response of JobsApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobsApi->list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
 **type** | [**List[JobTypeSchema]**](JobTypeSchema.md)| Filter on job type | [optional] 
 **state** | [**List[JobStateResult]**](JobStateResult.md)| Filter on job state | [optional] 
 **function_type** | [**List[FunctionType]**](FunctionType.md)| Filter on function type | [optional] 
 **created_before** | [**TimestampSpec**](.md)| Filter on jobs that created before the given timestamp or age | [optional] 
 **created_after** | [**TimestampSpec**](.md)| Filter on jobs that created after the given timestamp or age | [optional] 

### Return type

[**JobsResponse**](JobsResponse.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

