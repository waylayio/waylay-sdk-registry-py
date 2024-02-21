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
> bytearray example_archive(name, version, ls=ls, include_deprecated=include_deprecated)

Get Runtime Example Archive

Get an example of the specification archive of the runtime.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
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
    api_instance = waylay.services.registry.RuntimesApi(api_client)
    name = 'name_example' # str | The name of a <em>runtime</em>
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | A version range for a <em>runtime</em>
    ls = False # bool | If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. (optional) (default to False)
    include_deprecated = True # bool | If set to `true`, deprecated runtimes will be included in the query. (optional) (default to True)

    try:
        # Get Runtime Example Archive
        api_response = await api_instance.example_archive(name, version, ls=ls, include_deprecated=include_deprecated)
        print("The response of RuntimesApi->example_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimesApi->example_archive: %s\n" % e)
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

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_example_asset**
> bytearray get_example_asset(name, version, wildcard, ls=ls, include_deprecated=include_deprecated)

Get File From Runtime Example Archive

Get a file from the example specification archive of the runtime.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
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
    api_instance = waylay.services.registry.RuntimesApi(api_client)
    name = 'name_example' # str | The name of a <em>runtime</em>
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | A version range for a <em>runtime</em>
    wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive
    ls = False # bool | If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. (optional) (default to False)
    include_deprecated = True # bool | If set to `true`, deprecated runtimes will be included in the query. (optional) (default to True)

    try:
        # Get File From Runtime Example Archive
        api_response = await api_instance.get_example_asset(name, version, wildcard, ls=ls, include_deprecated=include_deprecated)
        print("The response of RuntimesApi->get_example_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimesApi->get_example_asset: %s\n" % e)
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

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/tar+gzip, application/x-gzip, application/x-tar, application/gzip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest**
> RuntimeVersionResponse get_latest(name, version=version, include_deprecated=include_deprecated, function_type=function_type, archive_format=archive_format)

Get Latest Runtime Version

Get a representation of the default runtime version by name.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse
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
    api_instance = waylay.services.registry.RuntimesApi(api_client)
    name = 'name_example' # str | The name of a <em>runtime</em>
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | If set, filters on the <code>version</code> of a runtime. Supports [version ranges](https://devhints.io/semver). (optional)
    include_deprecated = False # bool | If set to `true`, deprecated runtimes will be included in the query. (optional) (default to False)
    function_type = [waylay.services.registry.FunctionType()] # List[FunctionType] | If set, filters on the <code>functionType</code> of a runtime. Uses an exact match. (optional)
    archive_format = [waylay.services.registry.ArchiveFormat()] # List[ArchiveFormat] | If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match. (optional)

    try:
        # Get Latest Runtime Version
        api_response = await api_instance.get_latest(name, version=version, include_deprecated=include_deprecated, function_type=function_type, archive_format=archive_format)
        print("The response of RuntimesApi->get_latest:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimesApi->get_latest: %s\n" % e)
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

# **get**
> RuntimeVersionResponse get(name, version, include_deprecated=include_deprecated)

Get Runtime Version

Get a representation of the default runtime version by name.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.runtime_version_response import RuntimeVersionResponse
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
    api_instance = waylay.services.registry.RuntimesApi(api_client)
    name = 'name_example' # str | The name of a <em>runtime</em>
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | A version range for a <em>runtime</em>
    include_deprecated = True # bool | If set to `true`, deprecated runtimes will be included in the query. (optional) (default to True)

    try:
        # Get Runtime Version
        api_response = await api_instance.get(name, version, include_deprecated=include_deprecated)
        print("The response of RuntimesApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimesApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a &lt;em&gt;runtime&lt;/em&gt; | 
 **version** | [**SemanticVersionRange**](.md)| A version range for a &lt;em&gt;runtime&lt;/em&gt; | 
 **include_deprecated** | **bool**| If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to True]

### Return type

[**RuntimeVersionResponse**](RuntimeVersionResponse.md)

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
> RuntimeSummaryResponse list(version=version, latest=latest, include_deprecated=include_deprecated, name=name, function_type=function_type, archive_format=archive_format)

List Runtimes

List the runtimes that function registry supports.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse
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
    api_instance = waylay.services.registry.RuntimesApi(api_client)
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | If set, filters on the <code>version</code> of a runtime. Supports [version ranges](https://devhints.io/semver). (optional)
    latest = waylay.services.registry.LatestVersionLevel() # LatestVersionLevel | If set, filters on the level of latest versions that will be included in the query. * `major`: include at most one latest version per name and major release. * `minor`: include at most one latest version per name and minor release. * `patch`: include each matching patch version. * `true`: include the latest matching version. * `false`: include any matching version (same as `patch`).  This filter is applied after all other selection criteria. (optional)
    include_deprecated = False # bool | If set to `true`, deprecated runtimes will be included in the query. (optional) (default to False)
    name = 'node*' # str | If set, filters on the <code>name</code> of a runtime. Supports <code>*</code> and <code>?</code> wildcards and is case-insensitive. (optional)
    function_type = [waylay.services.registry.FunctionType()] # List[FunctionType] | If set, filters on the <code>functionType</code> of a runtime. Uses an exact match. (optional)
    archive_format = [waylay.services.registry.ArchiveFormat()] # List[ArchiveFormat] | If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match. (optional)

    try:
        # List Runtimes
        api_response = await api_instance.list(version=version, latest=latest, include_deprecated=include_deprecated, name=name, function_type=function_type, archive_format=archive_format)
        print("The response of RuntimesApi->list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimesApi->list: %s\n" % e)
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

# **list_versions**
> RuntimeSummaryResponse list_versions(name, version=version, latest=latest, include_deprecated=include_deprecated, function_type=function_type, archive_format=archive_format)

List Runtime Versions

List the supported versions of a specific runtime.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.latest_version_level import LatestVersionLevel
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse
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
    api_instance = waylay.services.registry.RuntimesApi(api_client)
    name = 'name_example' # str | The name of a <em>runtime</em>
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | If set, filters on the <code>version</code> of a runtime. Supports [version ranges](https://devhints.io/semver). (optional)
    latest = waylay.services.registry.LatestVersionLevel() # LatestVersionLevel | If set, filters on the level of latest versions that will be included in the query. * `major`: include at most one latest version per name and major release. * `minor`: include at most one latest version per name and minor release. * `patch`: include each matching patch version. * `true`: include the latest matching version. * `false`: include any matching version (same as `patch`).  This filter is applied after all other selection criteria. (optional)
    include_deprecated = False # bool | If set to `true`, deprecated runtimes will be included in the query. (optional) (default to False)
    function_type = [waylay.services.registry.FunctionType()] # List[FunctionType] | If set, filters on the <code>functionType</code> of a runtime. Uses an exact match. (optional)
    archive_format = [waylay.services.registry.ArchiveFormat()] # List[ArchiveFormat] | If set, filters on the <code>archiveFormat</code> of a runtime. Uses an exact match. (optional)

    try:
        # List Runtime Versions
        api_response = await api_instance.list_versions(name, version=version, latest=latest, include_deprecated=include_deprecated, function_type=function_type, archive_format=archive_format)
        print("The response of RuntimesApi->list_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RuntimesApi->list_versions: %s\n" % e)
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

