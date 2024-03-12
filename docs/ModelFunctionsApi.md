# waylay.services.registry.ModelFunctionsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ModelFunctionsApi.md#create) | **POST** /registry/v2/models/ | Create Model
[**delete_asset**](ModelFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Delete Model Asset
[**get_archive**](ModelFunctionsApi.md#get_archive) | **GET** /registry/v2/models/{name}/versions/{version}/content | Get Model Archive
[**get_asset**](ModelFunctionsApi.md#get_asset) | **GET** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Get File From Model Archive
[**get_latest**](ModelFunctionsApi.md#get_latest) | **GET** /registry/v2/models/{name} | Get Latest Model Version
[**get**](ModelFunctionsApi.md#get) | **GET** /registry/v2/models/{name}/versions/{version} | Get Model Version
[**jobs**](ModelFunctionsApi.md#jobs) | **GET** /registry/v2/models/{name}/versions/{version}/jobs | List Model Jobs
[**list**](ModelFunctionsApi.md#list) | **GET** /registry/v2/models/ | List Models
[**list_versions**](ModelFunctionsApi.md#list_versions) | **GET** /registry/v2/models/{name}/versions | List Model Versions
[**patch_metadata**](ModelFunctionsApi.md#patch_metadata) | **PATCH** /registry/v2/models/{name}/versions/{version}/metadata | Patch Model Metadata
[**publish**](ModelFunctionsApi.md#publish) | **POST** /registry/v2/models/{name}/versions/{version}/publish | Publish Draft Model
[**rebuild**](ModelFunctionsApi.md#rebuild) | **POST** /registry/v2/models/{name}/versions/{version}/rebuild | Rebuild Model
[**remove_version**](ModelFunctionsApi.md#remove_version) | **DELETE** /registry/v2/models/{name}/versions/{version} | Remove Model Version
[**remove_versions**](ModelFunctionsApi.md#remove_versions) | **DELETE** /registry/v2/models/{name} | Remove Model
[**update_asset**](ModelFunctionsApi.md#update_asset) | **PUT** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Update Model Asset
[**update_assets**](ModelFunctionsApi.md#update_assets) | **PUT** /registry/v2/models/{name}/versions/{version}/content | Update Model Assets
[**verify**](ModelFunctionsApi.md#verify) | **POST** /registry/v2/models/{name}/versions/{version}/verify | Verify Health Of Model

# **create**
> create(
> query: CreateQuery,
> files,
> headers
> ) -> PostModelJobSyncResponseV2 

Create Model

Creates a new <em>model</em> function by uploading its assets.      The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>model.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=kfserving</code>).    For each <em>runtime</em> other files will be required or supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Create Model
    # calls `POST /registry/v2/models/`
    api_response = await waylay_client.registry.model_functions.create(
        # query parameters:
        query = {
            'deprecatePrevious': waylay.services.registry.DeprecatePreviousPolicy()
            'dryRun': True
            'async': True
            'scaleToZero': False
            'version': waylay.services.registry.SemanticVersionRange()
            'name': 'name_example'
            'draft': False
        },
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'application/gzip', 'multipart/form-data', 
        headers = {
            'content-type': 'application/octet-stream',
        },
    )
    print("The response of registry.model_functions.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.create: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;      The required &lt;code&gt;model.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;kfserving&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['deprecatePrevious']** | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
**query['dryRun']** | **bool** | query parameter `"dryRun"` | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['scaleToZero']** | **bool** | query parameter `"scaleToZero"` | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately. | [optional] [default False]
**query['version']** | [**SemanticVersionRange**](.md) | query parameter `"version"` | If set, the function version will be an increment of the latest existing version that satisfies the &#x60;version&#x60; range. Note that this increment always takes precedence over an explicit &#x60;version&#x60; in the function manifest. | [optional] 
**query['name']** | **str** | query parameter `"name"` | If set, the value will be used as the function name instead of the one specified in the manifest. | [optional] 
**query['draft']** | **bool** | query parameter `"draft"` | If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/octet-stream`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `application/gzip`, `multipart/form-data`

### Return type


[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_asset**
> delete_asset(
> name: str,
> version: str,
> wildcard: str,
> query: DeleteAssetQuery,
> headers
> ) -> PostModelJobSyncResponseV2 

Delete Model Asset

Delete an asset from the model's collection of existing assets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Delete Model Asset
    # calls `DELETE /registry/v2/models/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.model_functions.delete_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'async': True
            'chown': False
        },
    )
    print("The response of registry.model_functions.delete_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.delete_asset: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/models/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['chown']** | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_archive**
> get_archive(
> name: str,
> version: str,
> query: GetArchiveQuery,
> headers
> ) -> bytearray 

Get Model Archive

Get the specification archive of a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

try:
    # Get Model Archive
    # calls `GET /registry/v2/models/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.model_functions.get_archive(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.model_functions.get_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.get_archive: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}/content
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ls']** | **bool** | query parameter `"ls"` | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


**bytearray**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> get_asset(
> name: str,
> version: str,
> wildcard: str,
> query: GetAssetQuery,
> headers
> ) -> bytearray 

Get File From Model Archive

Get a file from the specification archive of a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

try:
    # Get File From Model Archive
    # calls `GET /registry/v2/models/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.model_functions.get_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'ls': False
        },
    )
    print("The response of registry.model_functions.get_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.get_asset: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ls']** | **bool** | query parameter `"ls"` | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


**bytearray**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest**
> get_latest(
> name: str,
> query: GetLatestQuery,
> headers
> ) -> GetModelResponseV2 

Get Latest Model Version

Fetch the latest version of a <em>model</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>model version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
try:
    # Get Latest Model Version
    # calls `GET /registry/v2/models/{name}`
    api_response = await waylay_client.registry.model_functions.get_latest(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'includeDraft': True
            'includeDeprecated': True
        },
    )
    print("The response of registry.model_functions.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.get_latest: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['includeDraft']** | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**query['includeDeprecated']** | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**GetModelResponseV2**](GetModelResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> get(
> name: str,
> version: str,
> headers
> ) -> GetModelResponseV2 

Get Model Version

Get a model by name and version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
try:
    # Get Model Version
    # calls `GET /registry/v2/models/{name}/versions/{version}`
    api_response = await waylay_client.registry.model_functions.get(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.model_functions.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**GetModelResponseV2**](GetModelResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> jobs(
> name: str,
> version: str,
> query: JobsQuery,
> headers
> ) -> JobsForModelResponseV2 

List Model Jobs

List the ongoing and completed operations on a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_type_schema import JobTypeSchema
from waylay.services.registry.models.jobs_for_model_response_v2 import JobsForModelResponseV2
try:
    # List Model Jobs
    # calls `GET /registry/v2/models/{name}/versions/{version}/jobs`
    api_response = await waylay_client.registry.model_functions.jobs(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'limit': 3.4
            'type': [waylay.services.registry.JobTypeSchema()]
            'state': [waylay.services.registry.JobStateResult()]
            'functionType': [waylay.services.registry.FunctionType()]
            'createdBefore': waylay.services.registry.TimestampSpec()
            'createdAfter': waylay.services.registry.TimestampSpec()
        },
    )
    print("The response of registry.model_functions.jobs:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.jobs: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions/{version}/jobs
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['type']** | [**List[JobTypeSchema]**](JobTypeSchema.md) | query parameter `"type"` | Filter on job type | [optional] 
**query['state']** | [**List[JobStateResult]**](JobStateResult.md) | query parameter `"state"` | Filter on job state | [optional] 
**query['functionType']** | [**List[FunctionType]**](FunctionType.md) | query parameter `"functionType"` | Filter on function type | [optional] 
**query['createdBefore']** | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on jobs that created before the given timestamp or age | [optional] 
**query['createdAfter']** | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on jobs that created after the given timestamp or age | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**JobsForModelResponseV2**](JobsForModelResponseV2.md)

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
> ) -> LatestModelsResponseV2 

List Models

List the (latest) versions of available <em>models</em>.  ### List Latest Model Versions By default, the result includes the latest non-deprecated, non-draft version for each <em>model</em> name. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   As long as no _version filters_ are used, each listed <em>model version</em> item will contain a HAL **link to the  latest** _draft_ (`entities[]._links.draft`) or latest _published_ (`entities[]._links.publisned`) version (if existing and different).  ### List Latest Model Versions (with filter) When any of the _version filter_ query parameters are used, the response contains the _latest_ version per named <em>model</em> that satisfy the filters, but **without links**.  ### List All Model Versions When using `latest=false` (default when using the `namedVersion` filter), the listing contains _all_  <em>models</em> versions that satisfy the query, possibly multiple versions per named <em>models</em>. No HAL links are provided.  #### Filter on _status_ By default <em>model versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list _ALL_ versions known to the function registry.  #### Version filter parameters The following query parameters are _version filters_ for the <em>model</em> listing: > `version`, `status`, `runtimeVersion`, `createdBy`, `createdBefore`, `createdAfter`, `updatedBy`, `updatedBefore`, `updatedAfter`, `nameVersion`, `deprecated`, `draft` 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.latest_models_response_v2 import LatestModelsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List Models
    # calls `GET /registry/v2/models/`
    api_response = await waylay_client.registry.model_functions.list(
        # query parameters:
        query = {
            'limit': 3.4
            'page': 3.4
            'includeDraft': True
            'includeDeprecated': True
            'deprecated': True
            'draft': True
            'nameVersion': ['name_version_example']
            'version': 'version_example'
            'status': [waylay.services.registry.StatusFilter()]
            'runtimeVersion': waylay.services.registry.SemanticVersionRange()
            'createdBy': '@me'
            'updatedBy': '@me'
            'createdBefore': waylay.services.registry.TimestampSpec()
            'createdAfter': waylay.services.registry.TimestampSpec()
            'updatedBefore': waylay.services.registry.TimestampSpec()
            'updatedAfter': waylay.services.registry.TimestampSpec()
            'name': 'name_example'
            'archiveFormat': [waylay.services.registry.ArchiveFormat()]
            'runtime': ['runtime_example']
            'latest': True
        },
    )
    print("The response of registry.model_functions.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['page']** | **float** | query parameter `"page"` | The number of pages to skip when returning result to this query. | [optional] 
**query['includeDraft']** | **bool** | query parameter `"includeDraft"` | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**query['includeDeprecated']** | **bool** | query parameter `"includeDeprecated"` | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**query['deprecated']** | **bool** | query parameter `"deprecated"` | Filter on the deprecation status of the function. | [optional] 
**query['draft']** | **bool** | query parameter `"draft"` | Filter on the draft status of the function. | [optional] 
**query['nameVersion']** | [**List[str]**](str.md) | query parameter `"nameVersion"` | Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 
**query['version']** | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**query['status']** | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['runtimeVersion']** | [**SemanticVersionRange**](.md) | query parameter `"runtimeVersion"` | Filter on the runtime version. | [optional] 
**query['createdBy']** | **str** | query parameter `"createdBy"` | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['updatedBy']** | **str** | query parameter `"updatedBy"` | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['createdBefore']** | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on funtions that were created before the given timestamp or age. | [optional] 
**query['createdAfter']** | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on funtions that were created after the given timestamp or age. | [optional] 
**query['updatedBefore']** | [**TimestampSpec**](.md) | query parameter `"updatedBefore"` | Filter on funtions that were updated before the given timestamp or age. | [optional] 
**query['updatedAfter']** | [**TimestampSpec**](.md) | query parameter `"updatedAfter"` | Filter on funtions that were updated after the given timestamp or age. | [optional] 
**query['name']** | **str** | query parameter `"name"` | Filter on the name of the function. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**query['archiveFormat']** | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | Filter on the archive format of the function. | [optional] 
**query['runtime']** | [**List[str]**](str.md) | query parameter `"runtime"` | Filter on the runtime of the function. | [optional] 
**query['latest']** | **bool** | query parameter `"latest"` | When &#x60;true&#x60;, only the latest version per function name is returned. If set to &#x60;false&#x60;, multiple versions per named function can be returned. Defaults to &#x60;true&#x60;, except when specific versions are selected with the &#x60;nameVersion&#x60; filter. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**LatestModelsResponseV2**](LatestModelsResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> list_versions(
> name: str,
> query: ListVersionsQuery,
> headers
> ) -> ModelVersionsResponseV2 

List Model Versions

List all deployed versions of a model.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.model_versions_response_v2 import ModelVersionsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
try:
    # List Model Versions
    # calls `GET /registry/v2/models/{name}/versions`
    api_response = await waylay_client.registry.model_functions.list_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'limit': 3.4
            'page': 3.4
            'deprecated': True
            'draft': True
            'version': 'version_example'
            'status': [waylay.services.registry.StatusFilter()]
            'runtimeVersion': waylay.services.registry.SemanticVersionRange()
            'createdBy': '@me'
            'updatedBy': '@me'
            'createdBefore': waylay.services.registry.TimestampSpec()
            'createdAfter': waylay.services.registry.TimestampSpec()
            'updatedBefore': waylay.services.registry.TimestampSpec()
            'updatedAfter': waylay.services.registry.TimestampSpec()
            'archiveFormat': [waylay.services.registry.ArchiveFormat()]
            'runtime': ['runtime_example']
        },
    )
    print("The response of registry.model_functions.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.list_versions: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/models/{name}/versions
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['limit']** | **float** | query parameter `"limit"` | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**query['page']** | **float** | query parameter `"page"` | The number of pages to skip when returning result to this query. | [optional] 
**query['deprecated']** | **bool** | query parameter `"deprecated"` | Filter on the deprecation status of the function. | [optional] 
**query['draft']** | **bool** | query parameter `"draft"` | Filter on the draft status of the function. | [optional] 
**query['version']** | **str** | query parameter `"version"` | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**query['status']** | [**List[StatusFilter]**](StatusFilter.md) | query parameter `"status"` | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**query['runtimeVersion']** | [**SemanticVersionRange**](.md) | query parameter `"runtimeVersion"` | Filter on the runtime version. | [optional] 
**query['createdBy']** | **str** | query parameter `"createdBy"` | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['updatedBy']** | **str** | query parameter `"updatedBy"` | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**query['createdBefore']** | [**TimestampSpec**](.md) | query parameter `"createdBefore"` | Filter on funtions that were created before the given timestamp or age. | [optional] 
**query['createdAfter']** | [**TimestampSpec**](.md) | query parameter `"createdAfter"` | Filter on funtions that were created after the given timestamp or age. | [optional] 
**query['updatedBefore']** | [**TimestampSpec**](.md) | query parameter `"updatedBefore"` | Filter on funtions that were updated before the given timestamp or age. | [optional] 
**query['updatedAfter']** | [**TimestampSpec**](.md) | query parameter `"updatedAfter"` | Filter on funtions that were updated after the given timestamp or age. | [optional] 
**query['archiveFormat']** | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | Filter on the archive format of the function. | [optional] 
**query['runtime']** | [**List[str]**](str.md) | query parameter `"runtime"` | Filter on the runtime of the function. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**ModelVersionsResponseV2**](ModelVersionsResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_metadata**
> patch_metadata(
> name: str,
> version: str,
> query: PatchMetadataQuery,
> headers
> ) -> GetModelResponseV2 

Patch Model Metadata

Patch the metadata of a model version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.function_meta import FunctionMeta
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
try:
    # Patch Model Metadata
    # calls `PATCH /registry/v2/models/{name}/versions/{version}/metadata`
    api_response = await waylay_client.registry.model_functions.patch_metadata(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'comment': 'comment_example'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.FunctionMeta() # FunctionMeta |  (optional)
    )
    print("The response of registry.model_functions.patch_metadata:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.patch_metadata: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/models/{name}/versions/{version}/metadata
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**FunctionMeta**](FunctionMeta.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**GetModelResponseV2**](GetModelResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> publish(
> name: str,
> version: str,
> query: PublishQuery,
> headers
> ) -> PostModelJobSyncResponseV2 

Publish Draft Model

Mark the <em>model</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>model</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Publish Draft Model
    # calls `POST /registry/v2/models/{name}/versions/{version}/publish`
    api_response = await waylay_client.registry.model_functions.publish(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'deprecatePrevious': waylay.services.registry.DeprecatePreviousPolicy()
            'async': True
        },
    )
    print("The response of registry.model_functions.publish:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.publish: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/{name}/versions/{version}/publish
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['deprecatePrevious']** | [**DeprecatePreviousPolicy**](.md) | query parameter `"deprecatePrevious"` | Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Model Published |  -  |
**202** | Model Published And Deploy Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> rebuild(
> name: str,
> version: str,
> query: RebuildQuery,
> headers
> ) -> RebuildModelSyncResponseV2 

Rebuild Model

Rebuild and deploy a model with the original or updated base image.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.rebuild_model_sync_response_v2 import RebuildModelSyncResponseV2
from waylay.services.registry.models.rebuild_policy import RebuildPolicy
try:
    # Rebuild Model
    # calls `POST /registry/v2/models/{name}/versions/{version}/rebuild`
    api_response = await waylay_client.registry.model_functions.rebuild(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'dryRun': True
            'async': True
            'upgrade': waylay.services.registry.RebuildPolicy()
            'forceVersion': 'force_version_example'
            'ignoreChecks': True
            'scaleToZero': True
            'skipRebuild': True
        },
    )
    print("The response of registry.model_functions.rebuild:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.rebuild: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/{name}/versions/{version}/rebuild
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['dryRun']** | **bool** | query parameter `"dryRun"` | If set to &lt;code&gt;true&lt;/code&gt;, checks whether rebuild jobs are needed, but do not start any jobs. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['upgrade']** | [**RebuildPolicy**](.md) | query parameter `"upgrade"` | If set, force a rebuild with the given &lt;em&gt;runtime&lt;/em&gt; version selection policy. &lt;ul&gt;  &lt;li&gt;&lt;code&gt;same&lt;/code&gt; &lt;b&gt;patch&lt;/b&gt; version.   This should only include backward compatible upgrades.  &lt;/li&gt;  &lt;li&gt;&lt;code&gt;minor&lt;/code&gt; &lt;b&gt;major&lt;/b&gt; version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .&lt;/li&gt; &lt;/ul&gt; | [optional] 
**query['forceVersion']** | **str** | query parameter `"forceVersion"` | If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the &#x60;upgrade&#x60; parameter. | [optional] 
**query['ignoreChecks']** | **bool** | query parameter `"ignoreChecks"` | If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;failed&#x60; or &#x60;undeployed&#x60; * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the &#x60;dryRun&#x60; option | [optional] 
**query['scaleToZero']** | **bool** | query parameter `"scaleToZero"` | Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**query['skipRebuild']** | **bool** | query parameter `"skipRebuild"` | If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**RebuildModelSyncResponseV2**](RebuildModelSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_version**
> remove_version(
> name: str,
> version: str,
> query: RemoveVersionQuery,
> headers
> ) -> UndeployedResponseV2 

Remove Model Version

Deprecate, undeploy and/or remove a <em>model</em> version.    By default, a `DELETE`    * _deprecates_ the model version(s): they are no longer included in listings by default.   * _undeploys_ the model version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the model version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2
try:
    # Remove Model Version
    # calls `DELETE /registry/v2/models/{name}/versions/{version}`
    api_response = await waylay_client.registry.model_functions.remove_version(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'async': True
            'force': True
            'undeploy': True
        },
    )
    print("The response of registry.model_functions.remove_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.remove_version: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/models/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['force']** | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
**query['undeploy']** | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**UndeployedResponseV2**](UndeployedResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_versions**
> remove_versions(
> name: str,
> query: RemoveVersionsQuery,
> headers
> ) -> UndeployedResponseV2 

Remove Model

Deprecate, undeploy and/or remove all versions of this named <em>model</em>.    By default, a `DELETE`    * _deprecates_ the model version(s): they are no longer included in listings by default.   * _undeploys_ the model version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the model version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2
try:
    # Remove Model
    # calls `DELETE /registry/v2/models/{name}`
    api_response = await waylay_client.registry.model_functions.remove_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'force': True
            'undeploy': True
            'async': True
        },
    )
    print("The response of registry.model_functions.remove_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.remove_versions: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/models/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['force']** | **bool** | query parameter `"force"` | If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
**query['undeploy']** | **bool** | query parameter `"undeploy"` | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**UndeployedResponseV2**](UndeployedResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> update_asset(
> name: str,
> version: str,
> wildcard: str,
> query: UpdateAssetQuery,
> headers
> ) -> PostModelJobSyncResponseV2 

Update Model Asset

The provided asset will be added to the <em>model</em> function's collection of existing assets,   replacing any existing asset with the same name.    Please note that it is not allowed to update the model.json json file with a changed value for any of the     <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.file_upload import FileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Update Model Asset
    # calls `PUT /registry/v2/models/{name}/versions/{version}/content/{wildcard}`
    api_response = await waylay_client.registry.model_functions.update_asset(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'async': True
            'chown': False
        },
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 
        headers = {
            'content-type': 'application/octet-stream',
        },
    )
    print("The response of registry.model_functions.update_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.update_asset: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/models/{name}/versions/{version}/content/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | A single asset file. | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['chown']** | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/octet-stream`

### Return type


[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assets**
> update_assets(
> name: str,
> version: str,
> query: UpdateAssetsQuery,
> files,
> headers
> ) -> PostModelJobSyncResponseV2 

Update Model Assets

Update a draft <em>model</em> function by updating its assets.      The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>model</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
try:
    # Update Model Assets
    # calls `PUT /registry/v2/models/{name}/versions/{version}/content`
    api_response = await waylay_client.registry.model_functions.update_assets(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'async': True
            'chown': False
        },
        # non-json binary data: use a byte array or a generator of bytearray chuncks
        content=b'my-binary-data',
        # this operation supports multiple request content types: use `headers` to specify the one used
        # alternatives: 'application/tar+gzip', 'application/x-gzip', 'application/x-tar', 'application/gzip', 'multipart/form-data', 
        headers = {
            'content-type': 'application/octet-stream',
        },
    )
    print("The response of registry.model_functions.update_assets:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.update_assets: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/models/{name}/versions/{version}/content
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**content** | **[ContentRequest](Operation.md#req_arg_content)** | binary request body | The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;model&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 
**files** | **[FileTypes](Operation.md#req_arg_files)** | request body files |   |
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['chown']** | **bool** | query parameter `"chown"` | If set, ownership of the draft function is transferred to the current user. | [default False]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 
**headers['content-type']** | **str** | content type | request header `"content-type"` | should match mediaType `application/octet-stream`, `application/tar+gzip`, `application/x-gzip`, `application/x-tar`, `application/gzip`, `multipart/form-data`

### Return type


[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Default Response |  -  |
**202** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify**
> verify(
> name: str,
> version: str,
> query: VerifyQuery,
> headers
> ) -> VerifyModelSyncResponseV2 

Verify Health Of Model

Verify health of model deployed on openfaas.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.verify_model_sync_response_v2 import VerifyModelSyncResponseV2
try:
    # Verify Health Of Model
    # calls `POST /registry/v2/models/{name}/versions/{version}/verify`
    api_response = await waylay_client.registry.model_functions.verify(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # query parameters:
        query = {
            'comment': 'comment_example'
            'async': True
            'scaleToZero': True
        },
    )
    print("The response of registry.model_functions.verify:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.model_functions.verify: %s\n" % e)
```

### Endpoint
```
POST /registry/v2/models/{name}/versions/{version}/verify
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['comment']** | **str** | query parameter `"comment"` | An optional user-specified comment corresponding to the operation. | [optional] 
**query['async']** | **bool** | query parameter `"async"` | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default True]
**query['scaleToZero']** | **bool** | query parameter `"scaleToZero"` | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type


[**VerifyModelSyncResponseV2**](VerifyModelSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Model Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

