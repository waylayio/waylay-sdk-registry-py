# waylay.services.registry.WebscriptFunctionsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](WebscriptFunctionsApi.md#create) | **POST** /registry/v2/webscripts/ | Create Webscript Version
[**delete_asset**](WebscriptFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Delete Webscript Asset
[**get_archive**](WebscriptFunctionsApi.md#get_archive) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content | Get Webscript Archive
[**get_asset**](WebscriptFunctionsApi.md#get_asset) | **GET** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Get File From Webscript Archive
[**get_latest**](WebscriptFunctionsApi.md#get_latest) | **GET** /registry/v2/webscripts/{name} | Get Latest Webscript Version
[**get**](WebscriptFunctionsApi.md#get) | **GET** /registry/v2/webscripts/{name}/versions/{version} | Get Webscript Version
[**jobs**](WebscriptFunctionsApi.md#jobs) | **GET** /registry/v2/webscripts/{name}/versions/{version}/jobs | List Webscript Jobs
[**list_versions**](WebscriptFunctionsApi.md#list_versions) | **GET** /registry/v2/webscripts/{name}/versions | List Webscript Versions
[**list**](WebscriptFunctionsApi.md#list) | **GET** /registry/v2/webscripts/ | List Webscripts
[**patch_metadata**](WebscriptFunctionsApi.md#patch_metadata) | **PATCH** /registry/v2/webscripts/{name}/versions/{version}/metadata | Patch Webscript Metadata
[**publish**](WebscriptFunctionsApi.md#publish) | **POST** /registry/v2/webscripts/{name}/versions/{version}/publish | Publish Draft Webscript
[**rebuild**](WebscriptFunctionsApi.md#rebuild) | **POST** /registry/v2/webscripts/{name}/versions/{version}/rebuild | Rebuild Webscript
[**remove_version**](WebscriptFunctionsApi.md#remove_version) | **DELETE** /registry/v2/webscripts/{name}/versions/{version} | Remove Webscript Version
[**remove_versions**](WebscriptFunctionsApi.md#remove_versions) | **DELETE** /registry/v2/webscripts/{name} | Remove Webscript
[**update_asset**](WebscriptFunctionsApi.md#update_asset) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content/{wildcard} | Update Webscript Asset
[**update_assets**](WebscriptFunctionsApi.md#update_assets) | **PUT** /registry/v2/webscripts/{name}/versions/{version}/content | Update Webscript Assets
[**verify**](WebscriptFunctionsApi.md#verify) | **POST** /registry/v2/webscripts/{name}/versions/{version}/verify | Verify Health Of Webscript


# **create**
> PostWebscriptJobSyncResponseV2 create(query=CreateQuery, body: MultipartFileUpload)

Create Webscript Version

Creates a new <em>webscript</em> function by uploading its assets.      The assets for a <em>webscript</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>webscript.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=webscripts</code>).    For each <em>runtime</em> other files will be required or supported.    

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
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2


body = waylay.services.registry.MultipartFileUpload() # MultipartFileUpload | The assets for a <em>webscript</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>webscript.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=webscripts</code>).    For each <em>runtime</em> other files will be required or supported.  (optional),

try:
    # Create Webscript Version
    api_response = await waylay_client.registry.webscript_functions.create(body = body)
    print("The response of registry.webscript_functions.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.create: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deprecate_previous** | [**DeprecatePreviousPolicy**](.md)| Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
 **dry_run** | **bool**| If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **scale_to_zero** | **bool**| If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately. | [optional] [default to False]
 **version** | [**SemanticVersionRange**](.md)| If set, the function version will be an increment of the latest existing version that satisfies the &#x60;version&#x60; range. Note that this increment always takes precedence over an explicit &#x60;version&#x60; in the function manifest. | [optional] 
 **name** | **str**| If set, the value will be used as the function name instead of the one specified in the manifest. | [optional] 
 **draft** | **bool**| If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid. | [optional] [default to False]
 **multipart_file_upload** | [**MultipartFileUpload**](MultipartFileUpload.md)| The assets for a &lt;em&gt;webscript&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;      The required &lt;code&gt;webscript.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;webscripts&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 

### Return type

[**PostWebscriptJobSyncResponseV2**](PostWebscriptJobSyncResponseV2.md)

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
> PostWebscriptJobSyncResponseV2 delete_asset(name: str, version: str, wildcard: str, query=DeleteAssetQuery)

Delete Webscript Asset

Delete an asset from the webscript's collection of existing assets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,
wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive,


try:
    # Delete Webscript Asset
    api_response = await waylay_client.registry.webscript_functions.delete_asset(name=name, version=version, wildcard=wildcard, )
    print("The response of registry.webscript_functions.delete_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.delete_asset: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chown** | **bool**| If set, ownership of the draft function is transferred to the current user. | [default to False]
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **wildcard** | **str**| Full path or path prefix of the asset within the archive | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

### Return type

[**PostWebscriptJobSyncResponseV2**](PostWebscriptJobSyncResponseV2.md)

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
> bytearray get_archive(name: str, version: str, query=GetArchiveQuery)

Get Webscript Archive

Get the specification archive of a webscript.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()


name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Get Webscript Archive
    api_response = await waylay_client.registry.webscript_functions.get_archive(name=name, version=version, )
    print("The response of registry.webscript_functions.get_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.get_archive: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **ls** | **bool**| If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]

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
> bytearray get_asset(name: str, version: str, wildcard: str, query=GetAssetQuery)

Get File From Webscript Archive

Get a file from the specification archive of a webscript.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()


name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,
wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive,


try:
    # Get File From Webscript Archive
    api_response = await waylay_client.registry.webscript_functions.get_asset(name=name, version=version, wildcard=wildcard, )
    print("The response of registry.webscript_functions.get_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.get_asset: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **wildcard** | **str**| Full path or path prefix of the asset within the archive | 
 **ls** | **bool**| If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]

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
> GetWebscriptResponseV2 get_latest(name: str, query=GetLatestQuery)

Get Latest Webscript Version

Fetch the latest version of a <em>webscript</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>webscript version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2

name = 'name_example' # str | The name of the function.,


try:
    # Get Latest Webscript Version
    api_response = await waylay_client.registry.webscript_functions.get_latest(name=name, )
    print("The response of registry.webscript_functions.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.get_latest: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **include_draft** | **bool**| Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
 **include_deprecated** | **bool**| Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 

### Return type

[**GetWebscriptResponseV2**](GetWebscriptResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> GetWebscriptResponseV2 get(name: str, version: str, query=GetQuery)

Get Webscript Version

Get the webscript version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Get Webscript Version
    api_response = await waylay_client.registry.webscript_functions.get(name=name, version=version, )
    print("The response of registry.webscript_functions.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 

### Return type

[**GetWebscriptResponseV2**](GetWebscriptResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> JobsForWebscriptResponseV2 jobs(name: str, version: str, query=JobsQuery)

List Webscript Jobs

List the ongoing and completed operations on a specific webscript.

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
from waylay.services.registry.models.jobs_for_webscript_response_v2 import JobsForWebscriptResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # List Webscript Jobs
    api_response = await waylay_client.registry.webscript_functions.jobs(name=name, version=version, )
    print("The response of registry.webscript_functions.jobs:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.jobs: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **limit** | **float**| The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
 **type** | [**List[JobTypeSchema]**](JobTypeSchema.md)| Filter on job type | [optional] 
 **state** | [**List[JobStateResult]**](JobStateResult.md)| Filter on job state | [optional] 
 **function_type** | [**List[FunctionType]**](FunctionType.md)| Filter on function type | [optional] 
 **created_before** | [**TimestampSpec**](.md)| Filter on jobs that created before the given timestamp or age | [optional] 
 **created_after** | [**TimestampSpec**](.md)| Filter on jobs that created after the given timestamp or age | [optional] 

### Return type

[**JobsForWebscriptResponseV2**](JobsForWebscriptResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> WebscriptVersionsResponseV2 list_versions(name: str, query=ListVersionsQuery)

List Webscript Versions

List all deployed versions of a webscript.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.status_filter import StatusFilter
from waylay.services.registry.models.webscript_versions_response_v2 import WebscriptVersionsResponseV2

name = 'name_example' # str | The name of the function.,


try:
    # List Webscript Versions
    api_response = await waylay_client.registry.webscript_functions.list_versions(name=name, )
    print("The response of registry.webscript_functions.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.list_versions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **limit** | **float**| The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
 **page** | **float**| The number of pages to skip when returning result to this query. | [optional] 
 **deprecated** | **bool**| Filter on the deprecation status of the function. | [optional] 
 **draft** | **bool**| Filter on the draft status of the function. | [optional] 
 **version** | **str**| Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
 **status** | [**List[StatusFilter]**](StatusFilter.md)| Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
 **runtime_version** | [**SemanticVersionRange**](.md)| Filter on the runtime version. | [optional] 
 **created_by** | **str**| Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
 **updated_by** | **str**| Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
 **created_before** | [**TimestampSpec**](.md)| Filter on funtions that were created before the given timestamp or age. | [optional] 
 **created_after** | [**TimestampSpec**](.md)| Filter on funtions that were created after the given timestamp or age. | [optional] 
 **updated_before** | [**TimestampSpec**](.md)| Filter on funtions that were updated before the given timestamp or age. | [optional] 
 **updated_after** | [**TimestampSpec**](.md)| Filter on funtions that were updated after the given timestamp or age. | [optional] 
 **archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md)| Filter on the archive format of the function. | [optional] 
 **runtime** | [**List[str]**](str.md)| Filter on the runtime of the function. | [optional] 

### Return type

[**WebscriptVersionsResponseV2**](WebscriptVersionsResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> LatestWebscriptsResponseV2 list(query=ListQuery)

List Webscripts

List the (latest) versions of available <em>webscripts</em>.  ### List Latest Webscript Versions By default, the result includes the latest non-deprecated, non-draft version for each <em>webscript</em> name. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   As long as no _version filters_ are used, each listed <em>webscript version</em> item will contain a HAL **link to the  latest** _draft_ (`entities[]._links.draft`) or latest _published_ (`entities[]._links.publisned`) version (if existing and different).  ### List Latest Webscript Versions (with filter) When any of the _version filter_ query parameters are used, the response contains the _latest_ version per named <em>webscript</em> that satisfy the filters, but **without links**.  ### List All Webscript Versions When using `latest=false` (default when using the `namedVersion` filter), the listing contains _all_  <em>webscripts</em> versions that satisfy the query, possibly multiple versions per named <em>webscripts</em>. No HAL links are provided.  #### Filter on _status_ By default <em>webscript versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list _ALL_ versions known to the function registry.  #### Version filter parameters The following query parameters are _version filters_ for the <em>webscript</em> listing: > `version`, `status`, `runtimeVersion`, `createdBy`, `createdBefore`, `createdAfter`, `updatedBy`, `updatedBefore`, `updatedAfter`, `nameVersion`, `deprecated`, `draft` 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.latest_webscripts_response_v2 import LatestWebscriptsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter



try:
    # List Webscripts
    api_response = await waylay_client.registry.webscript_functions.list()
    print("The response of registry.webscript_functions.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.list: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
 **page** | **float**| The number of pages to skip when returning result to this query. | [optional] 
 **include_draft** | **bool**| Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
 **include_deprecated** | **bool**| Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
 **deprecated** | **bool**| Filter on the deprecation status of the function. | [optional] 
 **draft** | **bool**| Filter on the draft status of the function. | [optional] 
 **name_version** | [**List[str]**](str.md)| Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 
 **version** | **str**| Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
 **status** | [**List[StatusFilter]**](StatusFilter.md)| Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
 **runtime_version** | [**SemanticVersionRange**](.md)| Filter on the runtime version. | [optional] 
 **created_by** | **str**| Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
 **updated_by** | **str**| Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
 **created_before** | [**TimestampSpec**](.md)| Filter on funtions that were created before the given timestamp or age. | [optional] 
 **created_after** | [**TimestampSpec**](.md)| Filter on funtions that were created after the given timestamp or age. | [optional] 
 **updated_before** | [**TimestampSpec**](.md)| Filter on funtions that were updated before the given timestamp or age. | [optional] 
 **updated_after** | [**TimestampSpec**](.md)| Filter on funtions that were updated after the given timestamp or age. | [optional] 
 **name** | **str**| Filter on the name of the function. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
 **archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md)| Filter on the archive format of the function. | [optional] 
 **runtime** | [**List[str]**](str.md)| Filter on the runtime of the function. | [optional] 
 **latest** | **bool**| When &#x60;true&#x60;, only the latest version per function name is returned. If set to &#x60;false&#x60;, multiple versions per named function can be returned. Defaults to &#x60;true&#x60;, except when specific versions are selected with the &#x60;nameVersion&#x60; filter. | [optional] 

### Return type

[**LatestWebscriptsResponseV2**](LatestWebscriptsResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_metadata**
> GetWebscriptResponseV2 patch_metadata(name: str, version: str, query=PatchMetadataQuery, body: FunctionMeta)

Patch Webscript Metadata

Patch the metadata of a webscript version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.function_meta import FunctionMeta
from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,

body = waylay.services.registry.FunctionMeta() # FunctionMeta |  (optional),

try:
    # Patch Webscript Metadata
    api_response = await waylay_client.registry.webscript_functions.patch_metadata(name=name, version=version, body = body)
    print("The response of registry.webscript_functions.patch_metadata:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.patch_metadata: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **function_meta** | [**FunctionMeta**](FunctionMeta.md)|  | [optional] 

### Return type

[**GetWebscriptResponseV2**](GetWebscriptResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> PostWebscriptJobSyncResponseV2 publish(name: str, version: str, query=PublishQuery)

Publish Draft Webscript

Mark the <em>webscript</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>webscript</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Publish Draft Webscript
    api_response = await waylay_client.registry.webscript_functions.publish(name=name, version=version, )
    print("The response of registry.webscript_functions.publish:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.publish: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **deprecate_previous** | [**DeprecatePreviousPolicy**](.md)| Set the cleanup policy used to automatically deprecate/delete previous versions. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

### Return type

[**PostWebscriptJobSyncResponseV2**](PostWebscriptJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Webscript Published |  -  |
**202** | Webscript Published And Deploy Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> RebuildWebscriptSyncResponseV2 rebuild(name: str, version: str, query=RebuildQuery)

Rebuild Webscript

Rebuild and deploy a webscript with the original or updated base image.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.rebuild_policy import RebuildPolicy
from waylay.services.registry.models.rebuild_webscript_sync_response_v2 import RebuildWebscriptSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Rebuild Webscript
    api_response = await waylay_client.registry.webscript_functions.rebuild(name=name, version=version, )
    print("The response of registry.webscript_functions.rebuild:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.rebuild: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **dry_run** | **bool**| If set to &lt;code&gt;true&lt;/code&gt;, checks whether rebuild jobs are needed, but do not start any jobs. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **upgrade** | [**RebuildPolicy**](.md)| If set, force a rebuild with the given &lt;em&gt;runtime&lt;/em&gt; version selection policy. &lt;ul&gt;  &lt;li&gt;&lt;code&gt;same&lt;/code&gt; &lt;b&gt;patch&lt;/b&gt; version.   This should only include backward compatible upgrades.  &lt;/li&gt;  &lt;li&gt;&lt;code&gt;minor&lt;/code&gt; &lt;b&gt;major&lt;/b&gt; version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .&lt;/li&gt; &lt;/ul&gt; | [optional] 
 **force_version** | **str**| If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the &#x60;upgrade&#x60; parameter. | [optional] 
 **ignore_checks** | **bool**| If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;failed&#x60; or &#x60;undeployed&#x60; * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the &#x60;dryRun&#x60; option | [optional] 
 **scale_to_zero** | **bool**| Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
 **skip_rebuild** | **bool**| If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. | [optional] 

### Return type

[**RebuildWebscriptSyncResponseV2**](RebuildWebscriptSyncResponseV2.md)

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
> UndeployedResponseV2 remove_version(name: str, version: str, query=RemoveVersionQuery)

Remove Webscript Version

Deprecate, undeploy and/or remove a <em>webscript</em> version.    By default, a `DELETE`    * _deprecates_ the webscript version(s): they are no longer included in listings by default.   * _undeploys_ the webscript version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the webscript version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Remove Webscript Version
    api_response = await waylay_client.registry.webscript_functions.remove_version(name=name, version=version, )
    print("The response of registry.webscript_functions.remove_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.remove_version: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **force** | **bool**| If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
 **undeploy** | **bool**| If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 

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
> UndeployedResponseV2 remove_versions(name: str, query=RemoveVersionsQuery)

Remove Webscript

Deprecate, undeploy and/or remove all versions of this named <em>webscript</em>.    By default, a `DELETE`    * _deprecates_ the webscript version(s): they are no longer included in listings by default.   * _undeploys_ the webscript version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the webscript version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2

name = 'name_example' # str | The name of the function.,


try:
    # Remove Webscript
    api_response = await waylay_client.registry.webscript_functions.remove_versions(name=name, )
    print("The response of registry.webscript_functions.remove_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.remove_versions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **force** | **bool**| If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
 **undeploy** | **bool**| If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 

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
> PostWebscriptJobSyncResponseV2 update_asset(name: str, version: str, wildcard: str, query=UpdateAssetQuery, body: FileUpload)

Update Webscript Asset

The provided asset will be added to the <em>webscript</em> function's collection of existing assets,   replacing any existing asset with the same name.    Please note that it is not allowed to update the webscript.json json file with a changed value for any of the     <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.file_upload import FileUpload
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,
wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive,

body = waylay.services.registry.FileUpload() # FileUpload | A single asset file. (optional),

try:
    # Update Webscript Asset
    api_response = await waylay_client.registry.webscript_functions.update_asset(name=name, version=version, wildcard=wildcard, body = body)
    print("The response of registry.webscript_functions.update_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.update_asset: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chown** | **bool**| If set, ownership of the draft function is transferred to the current user. | [default to False]
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **wildcard** | **str**| Full path or path prefix of the asset within the archive | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **file_upload** | [**FileUpload**](FileUpload.md)| A single asset file. | [optional] 

### Return type

[**PostWebscriptJobSyncResponseV2**](PostWebscriptJobSyncResponseV2.md)

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
> PostWebscriptJobSyncResponseV2 update_assets(name: str, version: str, query=UpdateAssetsQuery, body: MultipartFileUpload)

Update Webscript Assets

Update a draft <em>webscript</em> function by updating its assets.      The assets for a <em>webscript</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>webscript</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the webscript.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,

body = waylay.services.registry.MultipartFileUpload() # MultipartFileUpload | The assets for a <em>webscript</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>webscript</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the webscript.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.  (optional),

try:
    # Update Webscript Assets
    api_response = await waylay_client.registry.webscript_functions.update_assets(name=name, version=version, body = body)
    print("The response of registry.webscript_functions.update_assets:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.update_assets: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chown** | **bool**| If set, ownership of the draft function is transferred to the current user. | [default to False]
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **multipart_file_upload** | [**MultipartFileUpload**](MultipartFileUpload.md)| The assets for a &lt;em&gt;webscript&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;webscript&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the webscript.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 

### Return type

[**PostWebscriptJobSyncResponseV2**](PostWebscriptJobSyncResponseV2.md)

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
> VerifyWebscriptSyncResponseV2 verify(name: str, version: str, query=VerifyQuery)

Verify Health Of Webscript

Verify health of webscript deployed on openfaas.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.verify_webscript_sync_response_v2 import VerifyWebscriptSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Verify Health Of Webscript
    api_response = await waylay_client.registry.webscript_functions.verify(name=name, version=version, )
    print("The response of registry.webscript_functions.verify:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.webscript_functions.verify: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **scale_to_zero** | **bool**| Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 

### Return type

[**VerifyWebscriptSyncResponseV2**](VerifyWebscriptSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Webscript Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

