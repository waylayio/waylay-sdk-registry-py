# waylay.services.registry.ModelFunctionsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ModelFunctionsApi.md#create) | **POST** /registry/v2/models/ | Create Model
[**delete_asset**](ModelFunctionsApi.md#delete_asset) | **DELETE** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Delete Model Asset
[**get_archive**](ModelFunctionsApi.md#get_archive) | **GET** /registry/v2/models/{name}/versions/{version}/content | Get Model Archive
[**get_asset**](ModelFunctionsApi.md#get_asset) | **GET** /registry/v2/models/{name}/versions/{version}/content/{wildcard} | Get File From Model Archive
[**get_latest_version**](ModelFunctionsApi.md#get_latest_version) | **GET** /registry/v2/models/{name} | Get Latest Model Version
[**get_version**](ModelFunctionsApi.md#get_version) | **GET** /registry/v2/models/{name}/versions/{version} | Get Model Version
[**jobs**](ModelFunctionsApi.md#jobs) | **GET** /registry/v2/models/{name}/versions/{version}/jobs | List Model Jobs
[**list_all**](ModelFunctionsApi.md#list_all) | **GET** /registry/v2/models/ | List Models
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
> PostModelJobSyncResponseV2 create(deprecate_previous=deprecate_previous, dry_run=dry_run, var_async=var_async, scale_to_zero=scale_to_zero, version=version, name=name, draft=draft, multipart_file_upload=multipart_file_upload)

Create Model

Creates a new <em>model</em> function by uploading its assets.      The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>model.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=kfserving</code>).    For each <em>runtime</em> other files will be required or supported.    

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    deprecate_previous = waylay.services.registry.DeprecatePreviousPolicy() # DeprecatePreviousPolicy | Set the cleanup policy used to automatically deprecate/delete previous versions. (optional)
    dry_run = True # bool | If set to <code>true</code>, validates the deployment conditions, but does not change anything. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)
    scale_to_zero = False # bool | If set to <code>true</code>, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately. (optional) (default to False)
    version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | If set, the function version will be an increment of the latest existing version that satisfies the `version` range. Note that this increment always takes precedence over an explicit `version` in the function manifest. (optional)
    name = 'name_example' # str | If set, the value will be used as the function name instead of the one specified in the manifest. (optional)
    draft = False # bool | If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid. (optional) (default to False)
    multipart_file_upload = waylay.services.registry.MultipartFileUpload() # MultipartFileUpload | The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>      The required <code>model.json</code> json file contains the function metadata,   and must have a <code>runtime</code> attribute that is one of the supported <em>runtime</em>s    (see <code>GET /registry/v2/runtimes?functionType=kfserving</code>).    For each <em>runtime</em> other files will be required or supported.  (optional)

    try:
        # Create Model
        api_response = await api_instance.create(deprecate_previous=deprecate_previous, dry_run=dry_run, var_async=var_async, scale_to_zero=scale_to_zero, version=version, name=name, draft=draft, multipart_file_upload=multipart_file_upload)
        print("The response of ModelFunctionsApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->create: %s\n" % e)
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
 **multipart_file_upload** | [**MultipartFileUpload**](MultipartFileUpload.md)| The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;      The required &lt;code&gt;model.json&lt;/code&gt; json file contains the function metadata,   and must have a &lt;code&gt;runtime&lt;/code&gt; attribute that is one of the supported &lt;em&gt;runtime&lt;/em&gt;s    (see &lt;code&gt;GET /registry/v2/runtimes?functionType&#x3D;kfserving&lt;/code&gt;).    For each &lt;em&gt;runtime&lt;/em&gt; other files will be required or supported.  | [optional] 

### Return type

[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> PostModelJobSyncResponseV2 delete_asset(chown, name, version, wildcard, comment=comment, var_async=var_async)

Delete Model Asset

Delete an asset from the model's collection of existing assets.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    chown = False # bool | If set, ownership of the draft function is transferred to the current user. (default to False)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)

    try:
        # Delete Model Asset
        api_response = await api_instance.delete_asset(chown, name, version, wildcard, comment=comment, var_async=var_async)
        print("The response of ModelFunctionsApi->delete_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->delete_asset: %s\n" % e)
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

[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> bytearray get_archive(name, version, ls=ls)

Get Model Archive

Get the specification archive of a model.

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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    ls = False # bool | If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. (optional) (default to False)

    try:
        # Get Model Archive
        api_response = await api_instance.get_archive(name, version, ls=ls)
        print("The response of ModelFunctionsApi->get_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->get_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **ls** | **bool**| If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]

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

# **get_asset**
> bytearray get_asset(name, version, wildcard, ls=ls)

Get File From Model Archive

Get a file from the specification archive of a model.

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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive
    ls = False # bool | If set to `true`, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. (optional) (default to False)

    try:
        # Get File From Model Archive
        api_response = await api_instance.get_asset(name, version, wildcard, ls=ls)
        print("The response of ModelFunctionsApi->get_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->get_asset: %s\n" % e)
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

# **get_latest_version**
> GetModelResponseV2 get_latest_version(name, include_draft=include_draft, include_deprecated=include_deprecated)

Get Latest Model Version

Fetch the latest version of a <em>model</em>.    By default, the result shows the latest non-deprecated, non-draft version.   If there is no such version, the latest deprecated or the latest draft version is returned, with the former taking precedence.       Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>     The returned <em>model version</em> will contain a link to its   latest _draft_ or latest _published_ version (if existing and different).   

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    include_draft = True # bool | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**. (optional)
    include_deprecated = True # bool | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**. (optional)

    try:
        # Get Latest Model Version
        api_response = await api_instance.get_latest_version(name, include_draft=include_draft, include_deprecated=include_deprecated)
        print("The response of ModelFunctionsApi->get_latest_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->get_latest_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **include_draft** | **bool**| Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
 **include_deprecated** | **bool**| Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 

### Return type

[**GetModelResponseV2**](GetModelResponseV2.md)

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

# **get_version**
> GetModelResponseV2 get_version(name, version)

Get Model Version

Get a model by name and version.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.

    try:
        # Get Model Version
        api_response = await api_instance.get_version(name, version)
        print("The response of ModelFunctionsApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->get_version: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 

### Return type

[**GetModelResponseV2**](GetModelResponseV2.md)

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

# **jobs**
> JobsForModelResponseV2 jobs(name, version, limit=limit, type=type, state=state, function_type=function_type, created_before=created_before, created_after=created_after)

List Model Jobs

List the ongoing and completed operations on a model.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.function_type import FunctionType
from waylay.services.registry.models.job_state_result import JobStateResult
from waylay.services.registry.models.job_type_schema import JobTypeSchema
from waylay.services.registry.models.jobs_for_model_response_v2 import JobsForModelResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    limit = 3.4 # float | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. (optional)
    type = [waylay.services.registry.JobTypeSchema()] # List[JobTypeSchema] | Filter on job type (optional)
    state = [waylay.services.registry.JobStateResult()] # List[JobStateResult] | Filter on job state (optional)
    function_type = [waylay.services.registry.FunctionType()] # List[FunctionType] | Filter on function type (optional)
    created_before = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on jobs that created before the given timestamp or age (optional)
    created_after = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on jobs that created after the given timestamp or age (optional)

    try:
        # List Model Jobs
        api_response = await api_instance.jobs(name, version, limit=limit, type=type, state=state, function_type=function_type, created_before=created_before, created_after=created_after)
        print("The response of ModelFunctionsApi->jobs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->jobs: %s\n" % e)
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

[**JobsForModelResponseV2**](JobsForModelResponseV2.md)

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

# **list_all**
> LatestModelsResponseV2 list_all(limit=limit, page=page, include_draft=include_draft, include_deprecated=include_deprecated, deprecated=deprecated, draft=draft, name_version=name_version, version=version, status=status, runtime_version=runtime_version, created_by=created_by, updated_by=updated_by, created_before=created_before, created_after=created_after, updated_before=updated_before, updated_after=updated_after, name=name, archive_format=archive_format, runtime=runtime, latest=latest)

List Models

List the (latest) versions of available <em>models</em>.  ### List Latest Model Versions By default, the result includes the latest non-deprecated, non-draft version for each <em>model</em> name. If there is no such version, the latest _deprecated_ or the latest _draft_ version is included, with the former taking precedence.     Use the boolean query parameters <code>includeDeprecated</code> or <code>includeDraft</code> to change this behaviour:   <ul>   <li><code>includeDeprecated=true</code>: do not prefer non-deprecated versions as a latest version: if the latest version is a deprecated one, it will be shown, even if there are older non-deprecated versions.</li>   <li><code>includeDraft=true</code>: do not prefer non-draft versions as a latest version: if the latest version is a draft, it will be shown, even if there are older non-draft versions.</li>   </ul>   As long as no _version filters_ are used, each listed <em>model version</em> item will contain a HAL **link to the  latest** _draft_ (`entities[]._links.draft`) or latest _published_ (`entities[]._links.publisned`) version (if existing and different).  ### List Latest Model Versions (with filter) When any of the _version filter_ query parameters are used, the response contains the _latest_ version per named <em>model</em> that satisfy the filters, but **without links**.  ### List All Model Versions When using `latest=false` (default when using the `namedVersion` filter), the listing contains _all_  <em>models</em> versions that satisfy the query, possibly multiple versions per named <em>models</em>. No HAL links are provided.  #### Filter on _status_ By default <em>model versions</em> with status  `undeployed` are **excluded** in all cases. Use the _version filter_ `status` to include/exclude a status from the results. By example,  > `?status=any&includeDeprecated=true&includeDraft=true&latest=false`  will list _ALL_ versions known to the function registry.  #### Version filter parameters The following query parameters are _version filters_ for the <em>model</em> listing: > `version`, `status`, `runtimeVersion`, `createdBy`, `createdBefore`, `createdAfter`, `updatedBy`, `updatedBefore`, `updatedAfter`, `nameVersion`, `deprecated`, `draft` 

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.latest_models_response_v2 import LatestModelsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    limit = 3.4 # float | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. (optional)
    page = 3.4 # float | The number of pages to skip when returning result to this query. (optional)
    include_draft = True # bool | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to `true`, draft versions are **included**. If set to `false`, draft versions are **excluded**. (optional)
    include_deprecated = True # bool | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to `true`, deprecated versions are **included**. If set to `false`, deprecated versions are **excluded**. (optional)
    deprecated = True # bool | Filter on the deprecation status of the function. (optional)
    draft = True # bool | Filter on the draft status of the function. (optional)
    name_version = ['name_version_example'] # List[str] | Filter on exact `{name}@{version}` functions. Using this filter implies a `latest=false` default, returning multiple versions of the same named versions if they are filtered. (optional)
    version = 'version_example' # str | Filter on the version of the function (case-sensitive, supports wildcards). (optional)
    status = [waylay.services.registry.StatusFilter()] # List[StatusFilter] | Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions. (optional)
    runtime_version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | Filter on the runtime version. (optional)
    created_by = '@me' # str | Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs. (optional)
    updated_by = '@me' # str | Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs. (optional)
    created_before = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were created before the given timestamp or age. (optional)
    created_after = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were created after the given timestamp or age. (optional)
    updated_before = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were updated before the given timestamp or age. (optional)
    updated_after = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were updated after the given timestamp or age. (optional)
    name = 'name_example' # str | Filter on the name of the function. This is case-insensitive and supports wild-cards `?` (any one character) and `*` (any sequence of characters). (optional)
    archive_format = [waylay.services.registry.ArchiveFormat()] # List[ArchiveFormat] | Filter on the archive format of the function. (optional)
    runtime = ['runtime_example'] # List[str] | Filter on the runtime of the function. (optional)
    latest = True # bool | When `true`, only the latest version per function name is returned. If set to `false`, multiple versions per named function can be returned. Defaults to `true`, except when specific versions are selected with the `nameVersion` filter. (optional)

    try:
        # List Models
        api_response = await api_instance.list_all(limit=limit, page=page, include_draft=include_draft, include_deprecated=include_deprecated, deprecated=deprecated, draft=draft, name_version=name_version, version=version, status=status, runtime_version=runtime_version, created_by=created_by, updated_by=updated_by, created_before=created_before, created_after=created_after, updated_before=updated_before, updated_after=updated_after, name=name, archive_format=archive_format, runtime=runtime, latest=latest)
        print("The response of ModelFunctionsApi->list_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->list_all: %s\n" % e)
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

[**LatestModelsResponseV2**](LatestModelsResponseV2.md)

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
> ModelVersionsResponseV2 list_versions(name, limit=limit, page=page, deprecated=deprecated, draft=draft, version=version, status=status, runtime_version=runtime_version, created_by=created_by, updated_by=updated_by, created_before=created_before, created_after=created_after, updated_before=updated_before, updated_after=updated_after, archive_format=archive_format, runtime=runtime)

List Model Versions

List all deployed versions of a model.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.archive_format import ArchiveFormat
from waylay.services.registry.models.model_versions_response_v2 import ModelVersionsResponseV2
from waylay.services.registry.models.status_filter import StatusFilter
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    limit = 3.4 # float | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. (optional)
    page = 3.4 # float | The number of pages to skip when returning result to this query. (optional)
    deprecated = True # bool | Filter on the deprecation status of the function. (optional)
    draft = True # bool | Filter on the draft status of the function. (optional)
    version = 'version_example' # str | Filter on the version of the function (case-sensitive, supports wildcards). (optional)
    status = [waylay.services.registry.StatusFilter()] # List[StatusFilter] | Filter on the status of the plug. Filter values with a `-` postfix exclude the status. Use the `any` filter value to include all states. When not specified, a default `undeployed-` filter excludes _undeployed_ functions. (optional)
    runtime_version = waylay.services.registry.SemanticVersionRange() # SemanticVersionRange | Filter on the runtime version. (optional)
    created_by = '@me' # str | Filter on the user that create the plug. You can use the `@me` token to indicate your own plugs. (optional)
    updated_by = '@me' # str | Filter on the user that last updated the plug. You can use the `@me` token to indicate your own plugs. (optional)
    created_before = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were created before the given timestamp or age. (optional)
    created_after = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were created after the given timestamp or age. (optional)
    updated_before = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were updated before the given timestamp or age. (optional)
    updated_after = waylay.services.registry.TimestampSpec() # TimestampSpec | Filter on funtions that were updated after the given timestamp or age. (optional)
    archive_format = [waylay.services.registry.ArchiveFormat()] # List[ArchiveFormat] | Filter on the archive format of the function. (optional)
    runtime = ['runtime_example'] # List[str] | Filter on the runtime of the function. (optional)

    try:
        # List Model Versions
        api_response = await api_instance.list_versions(name, limit=limit, page=page, deprecated=deprecated, draft=draft, version=version, status=status, runtime_version=runtime_version, created_by=created_by, updated_by=updated_by, created_before=created_before, created_after=created_after, updated_before=updated_before, updated_after=updated_after, archive_format=archive_format, runtime=runtime)
        print("The response of ModelFunctionsApi->list_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->list_versions: %s\n" % e)
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

[**ModelVersionsResponseV2**](ModelVersionsResponseV2.md)

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

# **patch_metadata**
> GetModelResponseV2 patch_metadata(name, version, comment=comment, function_meta=function_meta)

Patch Model Metadata

Patch the metadata of a model version.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.function_meta import FunctionMeta
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    function_meta = waylay.services.registry.FunctionMeta() # FunctionMeta |  (optional)

    try:
        # Patch Model Metadata
        api_response = await api_instance.patch_metadata(name, version, comment=comment, function_meta=function_meta)
        print("The response of ModelFunctionsApi->patch_metadata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->patch_metadata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **function_meta** | [**FunctionMeta**](FunctionMeta.md)|  | [optional] 

### Return type

[**GetModelResponseV2**](GetModelResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **publish**
> PostModelJobSyncResponseV2 publish(name, version, comment=comment, deprecate_previous=deprecate_previous, var_async=var_async)

Publish Draft Model

Mark the <em>model</em> to be ready and stable, taking it out of draft mode.,    Typically, the <em>model</em> should be in the <code>running</code> status,    such that publishing becomes a simple operation where the existing deployment can be re-used.   In other statuses, plug-registry may need to initiate a new build and deployment procedure.   

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.deprecate_previous_policy import DeprecatePreviousPolicy
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    deprecate_previous = waylay.services.registry.DeprecatePreviousPolicy() # DeprecatePreviousPolicy | Set the cleanup policy used to automatically deprecate/delete previous versions. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)

    try:
        # Publish Draft Model
        api_response = await api_instance.publish(name, version, comment=comment, deprecate_previous=deprecate_previous, var_async=var_async)
        print("The response of ModelFunctionsApi->publish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->publish: %s\n" % e)
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

[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> RebuildModelSyncResponseV2 rebuild(name, version, comment=comment, dry_run=dry_run, var_async=var_async, upgrade=upgrade, force_version=force_version, ignore_checks=ignore_checks, scale_to_zero=scale_to_zero, skip_rebuild=skip_rebuild)

Rebuild Model

Rebuild and deploy a model with the original or updated base image.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.rebuild_model_sync_response_v2 import RebuildModelSyncResponseV2
from waylay.services.registry.models.rebuild_policy import RebuildPolicy
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    dry_run = True # bool | If set to <code>true</code>, checks whether rebuild jobs are needed, but do not start any jobs. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)
    upgrade = waylay.services.registry.RebuildPolicy() # RebuildPolicy | If set, force a rebuild with the given <em>runtime</em> version selection policy. <ul>  <li><code>same</code> <b>patch</b> version.   This should only include backward compatible upgrades.  </li>  <li><code>minor</code> <b>major</b> version.   This might include an upgrade of e.g. the language runtime and/or provided   dependencies that could break compatiblity with the function. .</li> </ul> (optional)
    force_version = 'force_version_example' # str | If set, force a rebuild with the given runtime version (including downgrades). This parameter is mutually exclusive to the `upgrade` parameter. (optional)
    ignore_checks = True # bool | If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in `pending`, `running`, `failed` or `undeployed` * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the `dryRun` option (optional)
    scale_to_zero = True # bool | Indicates whether the function needs to be scaled down after successful (re-)deployment. If not set, the function is scaled to zero only if it was not active before this command. (optional)
    skip_rebuild = True # bool | If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. (optional)

    try:
        # Rebuild Model
        api_response = await api_instance.rebuild(name, version, comment=comment, dry_run=dry_run, var_async=var_async, upgrade=upgrade, force_version=force_version, ignore_checks=ignore_checks, scale_to_zero=scale_to_zero, skip_rebuild=skip_rebuild)
        print("The response of ModelFunctionsApi->rebuild:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->rebuild: %s\n" % e)
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

[**RebuildModelSyncResponseV2**](RebuildModelSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> UndeployedResponseV2 remove_version(name, version, comment=comment, var_async=var_async, force=force, undeploy=undeploy)

Remove Model Version

Deprecate, undeploy and/or remove a <em>model</em> version.    By default, a `DELETE`    * _deprecates_ the model version(s): they are no longer included in listings by default.   * _undeploys_ the model version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the model version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)
    force = True # bool | If <code>true</code>, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. (optional)
    undeploy = True # bool | If `true`, the `DELETE` operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. (optional)

    try:
        # Remove Model Version
        api_response = await api_instance.remove_version(name, version, comment=comment, var_async=var_async, force=force, undeploy=undeploy)
        print("The response of ModelFunctionsApi->remove_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->remove_version: %s\n" % e)
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

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> UndeployedResponseV2 remove_versions(name, comment=comment, force=force, undeploy=undeploy, var_async=var_async)

Remove Model

Deprecate, undeploy and/or remove all versions of this named <em>model</em>.    By default, a `DELETE`    * _deprecates_ the model version(s): they are no longer included in listings by default.   * _undeploys_ the model version(s) with delay: the function can no longer be invoked, the small delay allows     other services to discover the removal.   * _removes_ the version(s) from the plug registry.    Use `?force=true` to immediately _undeploy_ and _remove_ without delay.    Use `?undeploy=true` to undeploy, but keep the model version registered in a `undeployed` state.   An `undeployed` version can later be restored by a _rebuild_ action. 

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    force = True # bool | If <code>true</code>, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. (optional)
    undeploy = True # bool | If `true`, the `DELETE` operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an `undeployed` status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If `false`, the `DELETE` operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with `force=true`.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)

    try:
        # Remove Model
        api_response = await api_instance.remove_versions(name, comment=comment, force=force, undeploy=undeploy, var_async=var_async)
        print("The response of ModelFunctionsApi->remove_versions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->remove_versions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **force** | **bool**| If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
 **undeploy** | **bool**| If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

### Return type

[**UndeployedResponseV2**](UndeployedResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> PostModelJobSyncResponseV2 update_asset(chown, name, version, wildcard, comment=comment, var_async=var_async, file_upload=file_upload)

Update Model Asset

The provided asset will be added to the <em>model</em> function's collection of existing assets,   replacing any existing asset with the same name.    Please note that it is not allowed to update the model.json json file with a changed value for any of the     <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.   

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.file_upload import FileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    chown = False # bool | If set, ownership of the draft function is transferred to the current user. (default to False)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    wildcard = 'wildcard_example' # str | Full path or path prefix of the asset within the archive
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)
    file_upload = waylay.services.registry.FileUpload() # FileUpload | A single asset file. (optional)

    try:
        # Update Model Asset
        api_response = await api_instance.update_asset(chown, name, version, wildcard, comment=comment, var_async=var_async, file_upload=file_upload)
        print("The response of ModelFunctionsApi->update_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->update_asset: %s\n" % e)
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

[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> PostModelJobSyncResponseV2 update_assets(chown, name, version, comment=comment, var_async=var_async, multipart_file_upload=multipart_file_upload)

Update Model Assets

Update a draft <em>model</em> function by updating its assets.      The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>model</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.    

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    chown = False # bool | If set, ownership of the draft function is transferred to the current user. (default to False)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)
    multipart_file_upload = waylay.services.registry.MultipartFileUpload() # MultipartFileUpload | The assets for a <em>model</em> function can be provided as either   <ul>     <li>a single <em>tar</em> archive (optionally compressed), with one of the content types      <code>application/octet-stream</code>, <code>application/tar+gzip</code>, <code>application/x-gzip</code>, <code>application/x-tar</code>, <code>application/gzip</code></li>     <li>separate files in a <code>multipart/form-data</code> request</li>   </ul>    The provided assets will be added to the <em>model</em> function's collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json</code> json file with a changed value for any of the    <code>name</code>, <code>version</code> and/or <code>runtime</code> attributes.    For each <em>runtime</em> other files are supported.  (optional)

    try:
        # Update Model Assets
        api_response = await api_instance.update_assets(chown, name, version, comment=comment, var_async=var_async, multipart_file_upload=multipart_file_upload)
        print("The response of ModelFunctionsApi->update_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->update_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chown** | **bool**| If set, ownership of the draft function is transferred to the current user. | [default to False]
 **name** | **str**| The name of the function. | 
 **version** | **str**| The version of the function. | 
 **comment** | **str**| An optional user-specified comment corresponding to the operation. | [optional] 
 **var_async** | **bool**| Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
 **multipart_file_upload** | [**MultipartFileUpload**](MultipartFileUpload.md)| The assets for a &lt;em&gt;model&lt;/em&gt; function can be provided as either   &lt;ul&gt;     &lt;li&gt;a single &lt;em&gt;tar&lt;/em&gt; archive (optionally compressed), with one of the content types      &lt;code&gt;application/octet-stream&lt;/code&gt;, &lt;code&gt;application/tar+gzip&lt;/code&gt;, &lt;code&gt;application/x-gzip&lt;/code&gt;, &lt;code&gt;application/x-tar&lt;/code&gt;, &lt;code&gt;application/gzip&lt;/code&gt;&lt;/li&gt;     &lt;li&gt;separate files in a &lt;code&gt;multipart/form-data&lt;/code&gt; request&lt;/li&gt;   &lt;/ul&gt;    The provided assets will be added to the &lt;em&gt;model&lt;/em&gt; function&#39;s collection of existing assets,   replacing any existing assets with the same name.    Please note that it is not allowed to update the model.json&lt;/code&gt; json file with a changed value for any of the    &lt;code&gt;name&lt;/code&gt;, &lt;code&gt;version&lt;/code&gt; and/or &lt;code&gt;runtime&lt;/code&gt; attributes.    For each &lt;em&gt;runtime&lt;/em&gt; other files are supported.  | [optional] 

### Return type

[**PostModelJobSyncResponseV2**](PostModelJobSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

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
> VerifyModelSyncResponseV2 verify(name, version, comment=comment, var_async=var_async, scale_to_zero=scale_to_zero)

Verify Health Of Model

Verify health of model deployed on openfaas.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.verify_model_sync_response_v2 import VerifyModelSyncResponseV2
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
    api_instance = waylay.services.registry.ModelFunctionsApi(api_client)
    name = 'name_example' # str | The name of the function.
    version = 'version_example' # str | The version of the function.
    comment = 'comment_example' # str | An optional user-specified comment corresponding to the operation. (optional)
    var_async = True # bool | Unless this is set to <code>false</code>, the server will start the required job actions asynchronously and return a <code>202</code> <em>Accepted</em> response. If <code>false</code> the request will block until the job actions are completed, or a timeout occurs. (optional) (default to True)
    scale_to_zero = True # bool | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. (optional)

    try:
        # Verify Health Of Model
        api_response = await api_instance.verify(name, version, comment=comment, var_async=var_async, scale_to_zero=scale_to_zero)
        print("The response of ModelFunctionsApi->verify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ModelFunctionsApi->verify: %s\n" % e)
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

[**VerifyModelSyncResponseV2**](VerifyModelSyncResponseV2.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**202** | Model Verification Initiated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

