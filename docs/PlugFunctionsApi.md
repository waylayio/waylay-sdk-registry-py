# waylay.services.registry.PlugFunctionsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](PlugFunctionsApi.md#create) | **POST** /registry/v2/plugs/ | Create Plug
[**delete_asset**](PlugFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Delete Plug Asset
[**get_archive**](PlugFunctionsApi.md#get_archive) | **GET** /registry/v2/plugs/{name}/versions/{version}/content | Get Plug Archive
[**get_asset**](PlugFunctionsApi.md#get_asset) | **GET** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Get File From Plug Archive
[**get_latest**](PlugFunctionsApi.md#get_latest) | **GET** /registry/v2/plugs/{name} | Get Latest Plug Version
[**get**](PlugFunctionsApi.md#get) | **GET** /registry/v2/plugs/{name}/versions/{version} | Get Plug Version
[**jobs**](PlugFunctionsApi.md#jobs) | **GET** /registry/v2/plugs/{name}/versions/{version}/jobs | List Plug Jobs
[**list**](PlugFunctionsApi.md#list) | **GET** /registry/v2/plugs/ | List Plugs
[**list_versions**](PlugFunctionsApi.md#list_versions) | **GET** /registry/v2/plugs/{name}/versions | List Plug Versions
[**patch_interface**](PlugFunctionsApi.md#patch_interface) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/interface | Patch Plug Interface
[**patch_metadata**](PlugFunctionsApi.md#patch_metadata) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/metadata | Patch Plug Metadata
[**publish**](PlugFunctionsApi.md#publish) | **POST** /registry/v2/plugs/{name}/versions/{version}/publish | Publish Draft Plug
[**rebuild**](PlugFunctionsApi.md#rebuild) | **POST** /registry/v2/plugs/{name}/versions/{version}/rebuild | Rebuild Plug
[**remove_version**](PlugFunctionsApi.md#remove_version) | **DELETE** /registry/v2/plugs/{name}/versions/{version} | Remove Plug Version
[**remove_versions**](PlugFunctionsApi.md#remove_versions) | **DELETE** /registry/v2/plugs/{name} | Remove Plug
[**update_asset**](PlugFunctionsApi.md#update_asset) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content/{wildcard} | Update Plug Asset
[**update_assets**](PlugFunctionsApi.md#update_assets) | **PUT** /registry/v2/plugs/{name}/versions/{version}/content | Update Plug Assets
[**verify**](PlugFunctionsApi.md#verify) | **POST** /registry/v2/plugs/{name}/versions/{version}/verify | Verify Health Of Plug


# **create**
> PostPlugJobSyncResponseV2 create(query=CreateQuery, body: MultipartFileUpload)

Create Plug

Creates a new <em>plug</em> function by uploading its assets.      The assets for a <em>plug</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>plug.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=plugs</code>).    For each <em>runtime</em> other files will be required or supported.    

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
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2


body = waylay.services.registry.MultipartFileUpload() # MultipartFileUpload | The assets for a <em>plug</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>plug.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=plugs</code>).    For each <em>runtime</em> other files will be required or supported.  (optional),

try:
    # Create Plug
    api_response = await waylay_client.registry.plug_functions.create(body = body)
    print("The response of registry.plug_functions.create:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.create: %s\n" % e)
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
 **multipart_file_upload** | [**MultipartFileUpload**](MultipartFileUpload.md)| The assets for a &lt;em&gt;plug&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;      The required &lt;code&gt;plug.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;plugs&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 

### Return type

[**PostPlugJobSyncResponseV2**](PostPlugJobSyncResponseV2.md)

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
> PostPlugJobSyncResponseV2 delete_asset(name: str, version: str, wildcard: str, query=DeleteAssetQuery)

Delete Plug Asset

Delete an asset from the plug's collection of existing assets.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,
wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive,


try:
    # Delete Plug Asset
    api_response = await waylay_client.registry.plug_functions.delete_asset(name=name, version=version, wildcard=wildcard, )
    print("The response of registry.plug_functions.delete_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.delete_asset: %s\n" % e)
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

[**PostPlugJobSyncResponseV2**](PostPlugJobSyncResponseV2.md)

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

Get Plug Archive

Get the specification archive of a plug.

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
    # Get Plug Archive
    api_response = await waylay_client.registry.plug_functions.get_archive(name=name, version=version, )
    print("The response of registry.plug_functions.get_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.get_archive: %s\n" % e)
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

Get File From Plug Archive

Get a file from the specification archive of a plug.

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
    # Get File From Plug Archive
    api_response = await waylay_client.registry.plug_functions.get_asset(name=name, version=version, wildcard=wildcard, )
    print("The response of registry.plug_functions.get_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.get_asset: %s\n" % e)
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
> GetPlugResponseV2 get_latest(name: str, query=GetLatestQuery)

Get Latest Plug Version

Fetch the latest version of a <em>plug</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>plug version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
from waylay.services.registry.models.plug_type import PlugType

name = 'name_example' # str | The name of the function.,


try:
    # Get Latest Plug Version
    api_response = await waylay_client.registry.plug_functions.get_latest(name=name, )
    print("The response of registry.plug_functions.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.get_latest: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **type** | [**PlugType**](.md)| If set, filters on the type of plug. | [optional] 
 **include_draft** | **bool**| Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
 **include_deprecated** | **bool**| Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 

### Return type

[**GetPlugResponseV2**](GetPlugResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plug Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> GetPlugResponseV2 get(name: str, version: str, query=GetQuery)

Get Plug Version

Get a specific version of a plug.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Get Plug Version
    api_response = await waylay_client.registry.plug_functions.get(name=name, version=version, )
    print("The response of registry.plug_functions.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 

### Return type

[**GetPlugResponseV2**](GetPlugResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/html

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plug Version Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **jobs**
> JobsForPlugResponseV2 jobs(name: str, version: str, query=JobsQuery)

List Plug Jobs

List the ongoing and completed operations on a specific plug.

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
from waylay.services.registry.models.jobs_for_plug_response_v2 import JobsForPlugResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # List Plug Jobs
    api_response = await waylay_client.registry.plug_functions.jobs(name=name, version=version, )
    print("The response of registry.plug_functions.jobs:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.jobs: %s\n" % e)
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

[**JobsForPlugResponseV2**](JobsForPlugResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> LatestPlugsResponseV2 list(query=ListQuery)

List Plugs

List the (latest) versions of available <em>plugs</em>.  ### List Latest Plug Versions By default, the result includes the latest non-deprecated, non-draft version for each <em>plug</em> name. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   As long as no _version filters_ are used, each listed <em>plug version</em> item will contain a HAL **link to the  latest** _draft_ (`entities[]._links.draft`) or latest _published_ (`entities[]._links.publisned`) version (if existing and different).  ### List Latest Plug Versions (with filter) When any of the _version filter_ query parameters are used, the response contains the _latest_ version per named <em>plug</em> that satisfy the filters, but **without links**.  ### List All Plug Versions When using `latest=false` (default when using the `namedVersion` filter), the listing contains _all_  <em>plugs</em> versions that satisfy the query, possibly multiple versions per named <em>plugs</em>. No HAL links are provided.  #### Filter on _status_ By default <em>plug versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list _ALL_ versions known to the function registry.  #### Version filter parameters The following query parameters are _version filters_ for the <em>plug</em> listing: > `version`, `status`, `runtimeVersion`, `createdBy`, `createdBefore`, `createdAfter`, `updatedBy`, `updatedBefore`, `updatedAfter`, `nameVersion`, `deprecated`, `draft`, `tags` 

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.latest_plugs_response_v2 import LatestPlugsResponseV2
from waylay.services.registry.models.plug_type import PlugType
from waylay.services.registry.models.status_filter import StatusFilter



try:
    # List Plugs
    api_response = await waylay_client.registry.plug_functions.list()
    print("The response of registry.plug_functions.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.list: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tags** | [**TagsFilter**](.md)| Filter on the tags of the item. Can be a single tag, or a list of tags. When multiple tags are specified, an item must have all of the tags to be selected. | [optional] 
 **type** | [**PlugType**](.md)| If set, filters on the type of plug. | [optional] 
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

[**LatestPlugsResponseV2**](LatestPlugsResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> PlugVersionsResponseV2 list_versions(name: str, query=ListVersionsQuery)

List Plug Versions

List all versions of a plug, including deprecated versions or not.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.plug_versions_response_v2 import PlugVersionsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter

name = 'name_example' # str | The name of the function.,


try:
    # List Plug Versions
    api_response = await waylay_client.registry.plug_functions.list_versions(name=name, )
    print("The response of registry.plug_functions.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.list_versions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **tags** | [**TagsFilter**](.md)| Filter on the tags of the item. Can be a single tag, or a list of tags. When multiple tags are specified, an item must have all of the tags to be selected. | [optional] 
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

[**PlugVersionsResponseV2**](PlugVersionsResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_interface**
> GetPlugResponseV2 patch_interface(name: str, version: str, query=PatchInterfaceQuery, body: Documentation)

Patch Plug Interface

Patch the interface documentation of a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.documentation import Documentation
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,

body = waylay.services.registry.Documentation() # Documentation |  (optional),

try:
    # Patch Plug Interface
    api_response = await waylay_client.registry.plug_functions.patch_interface(name=name, version=version, body = body)
    print("The response of registry.plug_functions.patch_interface:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.patch_interface: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **documentation** | [**Documentation**](Documentation.md)|  | [optional] 

### Return type

[**GetPlugResponseV2**](GetPlugResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_metadata**
> GetPlugResponseV2 patch_metadata(name: str, version: str, query=PatchMetadataQuery, body: UpdateMetadataRequestV2)

Patch Plug Metadata

Patch the metadata of a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2
from waylay.services.registry.models.update_metadata_request_v2 import UpdateMetadataRequestV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,

body = waylay.services.registry.UpdateMetadataRequestV2() # UpdateMetadataRequestV2 |  (optional),

try:
    # Patch Plug Metadata
    api_response = await waylay_client.registry.plug_functions.patch_metadata(name=name, version=version, body = body)
    print("The response of registry.plug_functions.patch_metadata:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.patch_metadata: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **update_metadata_request_v2** | [**UpdateMetadataRequestV2**](UpdateMetadataRequestV2.md)|  | [optional] 

### Return type

[**GetPlugResponseV2**](GetPlugResponseV2.md)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> PostPlugJobSyncResponseV2 publish(name: str, version: str, query=PublishQuery)

Publish Draft Plug

Mark the <em>plug</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>plug</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Publish Draft Plug
    api_response = await waylay_client.registry.plug_functions.publish(name=name, version=version, )
    print("The response of registry.plug_functions.publish:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.publish: %s\n" % e)
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

[**PostPlugJobSyncResponseV2**](PostPlugJobSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Plug Published |  -  |
**202** | Plug Published And Deploy Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rebuild**
> RebuildPlugSyncResponseV2 rebuild(name: str, version: str, query=RebuildQuery)

Rebuild Plug

Rebuild and deploy a plug with the original or updated base image.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.rebuild_plug_sync_response_v2 import RebuildPlugSyncResponseV2
from waylay.services.registry.models.rebuild_policy import RebuildPolicy

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Rebuild Plug
    api_response = await waylay_client.registry.plug_functions.rebuild(name=name, version=version, )
    print("The response of registry.plug_functions.rebuild:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.rebuild: %s\n" % e)
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

[**RebuildPlugSyncResponseV2**](RebuildPlugSyncResponseV2.md)

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

Remove Plug Version

Deprecate, undeploy and/or remove a <em>plug</em> version.  By default, a `DELETE`  * marks _published_ version(s) _deprecated_: they remain active, but are no longer included in listings by default. * completely removes any _draft_ version(s) (_deprecate_, _undeploy_ and _remove_)  A _deprecated_ plug version will eventually be _undeployed_ (but not _removed_) by an external background task,  once proven that no waylay rule template or task references it.  Use `?force=true` to skip the deprecation and immediately remove the version(s).  Use `?undeploy=true` to undeploy the plug version(s), but keep it registered in a `undeployed` state. An `undeployed` version can later be restored by a _rebuild_ action. 

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
    # Remove Plug Version
    api_response = await waylay_client.registry.plug_functions.remove_version(name=name, version=version, )
    print("The response of registry.plug_functions.remove_version:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.remove_version: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **force** | **bool**| If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 
 **undeploy** | **bool**| If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 

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

Remove Plug

Deprecate, undeploy and/or remove all versions of this named <em>plug</em>.  By default, a `DELETE`  * marks _published_ version(s) _deprecated_: they remain active, but are no longer included in listings by default. * completely removes any _draft_ version(s) (_deprecate_, _undeploy_ and _remove_)  A _deprecated_ plug version will eventually be _undeployed_ (but not _removed_) by an external background task,  once proven that no waylay rule template or task references it.  Use `?force=true` to skip the deprecation and immediately remove the version(s).  Use `?undeploy=true` to undeploy the plug version(s), but keep it registered in a `undeployed` state. An `undeployed` version can later be restored by a _rebuild_ action. 

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
    # Remove Plug
    api_response = await waylay_client.registry.plug_functions.remove_versions(name=name, )
    print("The response of registry.plug_functions.remove_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.remove_versions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **force** | **bool**| If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 
 **undeploy** | **bool**| If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 

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
> PostPlugJobSyncResponseV2 update_asset(name: str, version: str, wildcard: str, query=UpdateAssetQuery, body: FileUpload)

Update Plug Asset

The provided asset will be added to the <em>plug</em> function's collection of existing assets,   replacing any existing asset with the same name.    Please note that it is not allowed to update the plug.json json file with a changed value for any of the     <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.   

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.file_upload import FileUpload
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,
wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive,

body = waylay.services.registry.FileUpload() # FileUpload | A single asset file. (optional),

try:
    # Update Plug Asset
    api_response = await waylay_client.registry.plug_functions.update_asset(name=name, version=version, wildcard=wildcard, body = body)
    print("The response of registry.plug_functions.update_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.update_asset: %s\n" % e)
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

[**PostPlugJobSyncResponseV2**](PostPlugJobSyncResponseV2.md)

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
> PostPlugJobSyncResponseV2 update_assets(name: str, version: str, query=UpdateAssetsQuery, body: MultipartFileUpload)

Update Plug Assets

Update a draft <em>plug</em> function by updating its assets.      The assets for a <em>plug</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>plug</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the plug.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,

body = waylay.services.registry.MultipartFileUpload() # MultipartFileUpload | The assets for a <em>plug</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>plug</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the plug.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.  (optional),

try:
    # Update Plug Assets
    api_response = await waylay_client.registry.plug_functions.update_assets(name=name, version=version, body = body)
    print("The response of registry.plug_functions.update_assets:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.update_assets: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chown** | **bool**| If set, ownership of the draft function is transferred to the current user. | [default to False]
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **multipart_file_upload** | [**MultipartFileUpload**](MultipartFileUpload.md)| The assets for a &lt;em&gt;plug&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;plug&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the plug.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 

### Return type

[**PostPlugJobSyncResponseV2**](PostPlugJobSyncResponseV2.md)

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
> VerifyPlugSyncResponseV2 verify(name: str, version: str, query=VerifyQuery)

Verify Health Of Plug

Verify health of plug deployed on openfaas.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.verify_plug_sync_response_v2 import VerifyPlugSyncResponseV2

name = 'name_example' # str | The name of the function.,
version = 'version_example' # str | The version of the function.,


try:
    # Verify Health Of Plug
    api_response = await waylay_client.registry.plug_functions.verify(name=name, version=version, )
    print("The response of registry.plug_functions.verify:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_functions.verify: %s\n" % e)
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

[**VerifyPlugSyncResponseV2**](VerifyPlugSyncResponseV2.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Plug Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

