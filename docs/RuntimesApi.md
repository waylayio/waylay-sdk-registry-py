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
> bytearray example_archive(name: str, version: SemanticVersionRange, query=ExampleArchiveQuery)

Get Runtime Example Archive

Get an example of the specification archive of the runtime.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()


name = 'name_example' # str | The name of a <em>runtime</em>,
version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | A version range for a <em>runtime</em>,


try:
    # Get Runtime Example Archive
    api_response = await waylay_client.registry.runtimes.example_archive(name=name, version=version, )
    print("The response of registry.runtimes.example_archive:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.example_archive: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a &lt;em&gt;runtime&lt;/em&gt; | 
 **version** | [**SemanticVersionRange**](.md)| A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
 **ls** | **bool**| If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to True]

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

# **get_example_asset**
> bytearray get_example_asset(name: str, version: SemanticVersionRange, wildcard: str, query=GetExampleAssetQuery)

Get File From Runtime Example Archive

Get a file from the example specification archive of the runtime.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()


name = 'name_example' # str | The name of a <em>runtime</em>,
version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | A version range for a <em>runtime</em>,
wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive,


try:
    # Get File From Runtime Example Archive
    api_response = await waylay_client.registry.runtimes.get_example_asset(name=name, version=version, wildcard=wildcard, )
    print("The response of registry.runtimes.get_example_asset:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.get_example_asset: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a &lt;em&gt;runtime&lt;/em&gt; | 
 **version** | [**SemanticVersionRange**](.md)| A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
 **wildcard** | **str**| Full path or path prefix of the asset within the archive | 
 **ls** | **bool**| If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to True]

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
> RuntimeVersionResponse get_latest(name: str, query=GetLatestQuery)

Get Latest Runtime Version

Get a representation of the default runtime version by name.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse

name = 'name_example' # str | The name of a <em>runtime</em>,


try:
    # Get Latest Runtime Version
    api_response = await waylay_client.registry.runtimes.get_latest(name=name, )
    print("The response of registry.runtimes.get_latest:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.get_latest: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a &lt;em&gt;runtime&lt;/em&gt; | 
 **version** | [**SemanticVersionRange**](.md)| If set, filters on the &lt;code&gt;version&lt;/code&gt; of a runtime. Supports [version ranges](https://devhints.io/semver). | [optional] 
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to False]
 **function_type** | [**List[FunctionType]**](FunctionType.md)| If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
 **archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md)| If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 

### Return type


[**RuntimeVersionResponse**](RuntimeVersionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> RuntimeVersionResponse get(name: str, version: SemanticVersionRange, query=GetQuery)

Get Runtime Version

Get a representation of the default runtime version by name.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse

name = 'name_example' # str | The name of a <em>runtime</em>,
version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | A version range for a <em>runtime</em>,


try:
    # Get Runtime Version
    api_response = await waylay_client.registry.runtimes.get(name=name, version=version, )
    print("The response of registry.runtimes.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a &lt;em&gt;runtime&lt;/em&gt; | 
 **version** | [**SemanticVersionRange**](.md)| A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to True]

### Return type


[**RuntimeVersionResponse**](RuntimeVersionResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> RuntimeSummaryResponse list(query=ListQuery)

List Runtimes

List the runtimes that function registry supports.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse



try:
    # List Runtimes
    api_response = await waylay_client.registry.runtimes.list()
    print("The response of registry.runtimes.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.list: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | [**SemanticVersionRange**](.md)| If set, filters on the &lt;code&gt;version&lt;/code&gt; of a runtime. Supports [version ranges](https://devhints.io/semver). | [optional] 
 **latest** | [**LatestVersionLevel**](.md)| If set, filters on the level of latest versions that will be included in the query. * &#x60;major&#x60;: include at most one latest version per name and major release. * &#x60;minor&#x60;: include at most one latest version per name and minor release. * &#x60;patch&#x60;: include each matching patch version. * &#x60;true&#x60;: include the latest matching version. * &#x60;false&#x60;: include any matching version (same as &#x60;patch&#x60;).  This filter is applied after all other selection criteria. | [optional] 
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to False]
 **name** | **str**| If set, filters on the &lt;code&gt;name&lt;/code&gt; of a runtime. Supports &lt;code&gt;*&lt;/code&gt; and &lt;code&gt;?&lt;/code&gt; wildcards and is case-insensitive. | [optional] 
 **function_type** | [**List[FunctionType]**](FunctionType.md)| If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
 **archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md)| If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 

### Return type


[**RuntimeSummaryResponse**](RuntimeSummaryResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_versions**
> RuntimeSummaryResponse list_versions(name: str, query=ListVersionsQuery)

List Runtime Versions

List the supported versions of a specific runtime.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse

name = 'name_example' # str | The name of a <em>runtime</em>,


try:
    # List Runtime Versions
    api_response = await waylay_client.registry.runtimes.list_versions(name=name, )
    print("The response of registry.runtimes.list_versions:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.runtimes.list_versions: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a &lt;em&gt;runtime&lt;/em&gt; | 
 **version** | [**SemanticVersionRange**](.md)| If set, filters on the &lt;code&gt;version&lt;/code&gt; of a runtime. Supports [version ranges](https://devhints.io/semver). | [optional] 
 **latest** | [**LatestVersionLevel**](.md)| If set, filters on the level of latest versions that will be included in the query. * &#x60;major&#x60;: include at most one latest version per name and major release. * &#x60;minor&#x60;: include at most one latest version per name and minor release. * &#x60;patch&#x60;: include each matching patch version. * &#x60;true&#x60;: include the latest matching version. * &#x60;false&#x60;: include any matching version (same as &#x60;patch&#x60;).  This filter is applied after all other selection criteria. | [optional] 
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to False]
 **function_type** | [**List[FunctionType]**](FunctionType.md)| If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
 **archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md)| If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 

### Return type


[**RuntimeSummaryResponse**](RuntimeSummaryResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

