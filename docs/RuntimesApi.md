# waylay.services.registry.RuntimesApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**example_archive**](RuntimesApi.md#example_archive) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example | Get Runtime Example Archive
[**get_example_asset**](RuntimesApi.md#get_example_asset) | **GET** /registry/v2/runtimes/{name}/versions/{version}/example/{wildcard} | Get File From Runtime Example Archive
[**get_latest**](RuntimesApi.md#get_latest) | **GET** /registry/v2/runtimes/{name} | Get Latest Runtime Version
[**get**](RuntimesApi.md#get) | **GET** /registry/v2/runtimes/{name}/versions/{version} | Get Runtime Version
[**list**](RuntimesApi.md#list) | **GET** /registry/v2/runtimes/ | List Runtimes
[**list_versions**](RuntimesApi.md#list_versions) | **GET** /registry/v2/runtimes/{name}/versions | List Runtime Versions

# **example_archive**
> example_archive(
> name: str,
> version: SemanticVersionRange,
> query: ExampleArchiveQuery,
> headers
> ) -> bytearray

Get Runtime Example Archive

Get an example of the specification archive of the runtime.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
try:
    # Get Runtime Example Archive
    # calls `GET /registry/v2/runtimes/{name}/versions/{version}/example`
    api_response = await waylay_client.registry.runtimes.example_archive(
        'name_example', # name | path param "name"
        waylay.services.registry.SemanticVersionRange(), # version | path param "version"
        # query parameters:
        query = {
            'ls': False
            'includeDeprecated': True
        },
    )
    print("The response of registry.runtimes.example_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.example_archive: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/runtimes/{name}/versions/{version}/example
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of a &lt;em&gt;runtime&lt;/em&gt; | 
**version** | [**SemanticVersionRange**](.md) | path parameter `"version"` | A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ls']** (dict) <br> **query.ls** (Query) | **bool** | query parameter `"ls"` | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default False]
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`bytearray`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_asset**
> get_example_asset(
> name: str,
> version: SemanticVersionRange,
> wildcard: str,
> query: GetExampleAssetQuery,
> headers
> ) -> bytearray

Get File From Runtime Example Archive

Get a file from the example specification archive of the runtime.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
try:
    # Get File From Runtime Example Archive
    # calls `GET /registry/v2/runtimes/{name}/versions/{version}/example/{wildcard}`
    api_response = await waylay_client.registry.runtimes.get_example_asset(
        'name_example', # name | path param "name"
        waylay.services.registry.SemanticVersionRange(), # version | path param "version"
        'wildcard_example', # wildcard | path param "wildcard"
        # query parameters:
        query = {
            'ls': False
            'includeDeprecated': True
        },
    )
    print("The response of registry.runtimes.get_example_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.get_example_asset: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/runtimes/{name}/versions/{version}/example/{wildcard}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of a &lt;em&gt;runtime&lt;/em&gt; | 
**version** | [**SemanticVersionRange**](.md) | path parameter `"version"` | A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
**wildcard** | **str** | path parameter `"wildcard"` | Full path or path prefix of the asset within the archive | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['ls']** (dict) <br> **query.ls** (Query) | **bool** | query parameter `"ls"` | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default False]
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`bytearray`** |  | 
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

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
> ) -> RuntimeVersionResponse

Get Latest Runtime Version

Get a representation of the default runtime version by name.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse
try:
    # Get Latest Runtime Version
    # calls `GET /registry/v2/runtimes/{name}`
    api_response = await waylay_client.registry.runtimes.get_latest(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'version': waylay.services.registry.SemanticVersionRange()
            'includeDeprecated': False
            'functionType': []
            'archiveFormat': []
        },
    )
    print("The response of registry.runtimes.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.get_latest: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/runtimes/{name}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of a &lt;em&gt;runtime&lt;/em&gt; | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['version']** (dict) <br> **query.version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"version"` | If set, filters on the &lt;code&gt;version&lt;/code&gt; of a runtime. Supports [version ranges](https://devhints.io/semver). | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default False]
**query['functionType']** (dict) <br> **query.function_type** (Query) | [**List[FunctionType]**](FunctionType.md) | query parameter `"functionType"` | If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RuntimeVersionResponse`** |  | [RuntimeVersionResponse](RuntimeVersionResponse.md)
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

# **get**
> get(
> name: str,
> version: SemanticVersionRange,
> query: GetQuery,
> headers
> ) -> RuntimeVersionResponse

Get Runtime Version

Get a representation of the default runtime version by name.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse
try:
    # Get Runtime Version
    # calls `GET /registry/v2/runtimes/{name}/versions/{version}`
    api_response = await waylay_client.registry.runtimes.get(
        'name_example', # name | path param "name"
        waylay.services.registry.SemanticVersionRange(), # version | path param "version"
        # query parameters:
        query = {
            'includeDeprecated': True
        },
    )
    print("The response of registry.runtimes.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/runtimes/{name}/versions/{version}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of a &lt;em&gt;runtime&lt;/em&gt; | 
**version** | [**SemanticVersionRange**](.md) | path parameter `"version"` | A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default True]
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RuntimeVersionResponse`** |  | [RuntimeVersionResponse](RuntimeVersionResponse.md)
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
> ) -> RuntimeSummaryResponse

List Runtimes

List the runtimes that function registry supports.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse
try:
    # List Runtimes
    # calls `GET /registry/v2/runtimes/`
    api_response = await waylay_client.registry.runtimes.list(
        # query parameters:
        query = {
            'version': waylay.services.registry.SemanticVersionRange()
            'latest': 'major'
            'includeDeprecated': False
            'name': 'node*'
            'functionType': []
            'archiveFormat': []
        },
    )
    print("The response of registry.runtimes.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/runtimes/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['version']** (dict) <br> **query.version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"version"` | If set, filters on the &lt;code&gt;version&lt;/code&gt; of a runtime. Supports [version ranges](https://devhints.io/semver). | [optional] 
**query['latest']** (dict) <br> **query.latest** (Query) | [**LatestVersionLevel**](.md) | query parameter `"latest"` | If set, filters on the level of latest versions that will be included in the query. * &#x60;major&#x60;: include at most one latest version per name and major release. * &#x60;minor&#x60;: include at most one latest version per name and minor release. * &#x60;patch&#x60;: include each matching patch version. * &#x60;true&#x60;: include the latest matching version. * &#x60;false&#x60;: include any matching version (same as &#x60;patch&#x60;).  This filter is applied after all other selection criteria. | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default False]
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` | If set, filters on the &lt;code&gt;name&lt;/code&gt; of a runtime. Supports &lt;code&gt;*&lt;/code&gt; and &lt;code&gt;?&lt;/code&gt; wildcards and is case-insensitive. | [optional] 
**query['functionType']** (dict) <br> **query.function_type** (Query) | [**List[FunctionType]**](FunctionType.md) | query parameter `"functionType"` | If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RuntimeSummaryResponse`** |  | [RuntimeSummaryResponse](RuntimeSummaryResponse.md)
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

# **list_versions**
> list_versions(
> name: str,
> query: ListVersionsQuery,
> headers
> ) -> RuntimeSummaryResponse

List Runtime Versions

List the supported versions of a specific runtime.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse
try:
    # List Runtime Versions
    # calls `GET /registry/v2/runtimes/{name}/versions`
    api_response = await waylay_client.registry.runtimes.list_versions(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'version': waylay.services.registry.SemanticVersionRange()
            'latest': 'major'
            'includeDeprecated': False
            'functionType': []
            'archiveFormat': []
        },
    )
    print("The response of registry.runtimes.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.list_versions: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/runtimes/{name}/versions
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of a &lt;em&gt;runtime&lt;/em&gt; | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['version']** (dict) <br> **query.version** (Query) | [**SemanticVersionRange**](.md) | query parameter `"version"` | If set, filters on the &lt;code&gt;version&lt;/code&gt; of a runtime. Supports [version ranges](https://devhints.io/semver). | [optional] 
**query['latest']** (dict) <br> **query.latest** (Query) | [**LatestVersionLevel**](.md) | query parameter `"latest"` | If set, filters on the level of latest versions that will be included in the query. * &#x60;major&#x60;: include at most one latest version per name and major release. * &#x60;minor&#x60;: include at most one latest version per name and minor release. * &#x60;patch&#x60;: include each matching patch version. * &#x60;true&#x60;: include the latest matching version. * &#x60;false&#x60;: include any matching version (same as &#x60;patch&#x60;).  This filter is applied after all other selection criteria. | [optional] 
**query['includeDeprecated']** (dict) <br> **query.include_deprecated** (Query) | **bool** | query parameter `"includeDeprecated"` | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default False]
**query['functionType']** (dict) <br> **query.function_type** (Query) | [**List[FunctionType]**](FunctionType.md) | query parameter `"functionType"` | If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**query['archiveFormat']** (dict) <br> **query.archive_format** (Query) | [**List[ArchiveFormat]**](ArchiveFormat.md) | query parameter `"archiveFormat"` | If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RuntimeSummaryResponse`** |  | [RuntimeSummaryResponse](RuntimeSummaryResponse.md)
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

