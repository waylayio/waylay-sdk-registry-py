# waylay.services.registry.PlugTagsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_all**](PlugTagsApi.md#add_all) | **PATCH** /registry/v2/plugs/{name}/tags | Add Tags On All
[**add**](PlugTagsApi.md#add) | **PATCH** /registry/v2/plugs/{name}/versions/{version}/tags | Add Tags
[**clear_all**](PlugTagsApi.md#clear_all) | **DELETE** /registry/v2/plugs/{name}/tags | Clear Tags On Any/All
[**clear**](PlugTagsApi.md#clear) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/tags | Clear Tags
[**find_all**](PlugTagsApi.md#find_all) | **GET** /registry/v2/plugs/{name}/tags/{tagName} | Find Tags On Any/All
[**find**](PlugTagsApi.md#find) | **GET** /registry/v2/plugs/{name}/versions/{version}/tags/{tagName} | Find Tag
[**list_all**](PlugTagsApi.md#list_all) | **GET** /registry/v2/plugs/{name}/tags | List Tags On Any/All
[**list**](PlugTagsApi.md#list) | **GET** /registry/v2/plugs/{name}/versions/{version}/tags | List Tags
[**put_all**](PlugTagsApi.md#put_all) | **PUT** /registry/v2/plugs/{name}/tags/{tagName} | Put Tag On All
[**put**](PlugTagsApi.md#put) | **PUT** /registry/v2/plugs/{name}/versions/{version}/tags/{tagName} | Put Tag
[**remove_all**](PlugTagsApi.md#remove_all) | **DELETE** /registry/v2/plugs/{name}/tags/{tagName} | Remove Tag On Any/All
[**remove**](PlugTagsApi.md#remove) | **DELETE** /registry/v2/plugs/{name}/versions/{version}/tags/{tagName} | Remove Tag
[**replace_all**](PlugTagsApi.md#replace_all) | **PUT** /registry/v2/plugs/{name}/tags | Replace Tags On Any/All
[**replace**](PlugTagsApi.md#replace) | **PUT** /registry/v2/plugs/{name}/versions/{version}/tags | Replace Tags

# **add_all**
> add_all(
> name: str,
> headers
> ) -> FunctionTagsResponse

Add Tags On All

Add tags to all versions of a named plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
from waylay.services.registry.models.update_tags_request_v2 import UpdateTagsRequestV2
try:
    # Add Tags On All
    # calls `PATCH /registry/v2/plugs/{name}/tags`
    api_response = await waylay_client.registry.plug_tags.add_all(
        'name_example', # name | path param "name"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.UpdateTagsRequestV2() # UpdateTagsRequestV2 |  (optional)
    )
    print("The response of registry.plug_tags.add_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.add_all: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/plugs/{name}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**json** | [**UpdateTagsRequestV2**](UpdateTagsRequestV2.md) | json request body |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add**
> add(
> name: str,
> version: str,
> headers
> ) -> FunctionTagsResponse

Add Tags

Add tags used on a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
from waylay.services.registry.models.update_tags_request_v2 import UpdateTagsRequestV2
try:
    # Add Tags
    # calls `PATCH /registry/v2/plugs/{name}/versions/{version}/tags`
    api_response = await waylay_client.registry.plug_tags.add(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.UpdateTagsRequestV2() # UpdateTagsRequestV2 |  (optional)
    )
    print("The response of registry.plug_tags.add:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.add: %s\n" % e)
```

### Endpoint
```
PATCH /registry/v2/plugs/{name}/versions/{version}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**UpdateTagsRequestV2**](UpdateTagsRequestV2.md) | json request body |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clear_all**
> clear_all(
> name: str,
> query: ClearAllQuery,
> headers
> ) -> FunctionTagsResponse

Clear Tags On Any/All

Remove all tags used on any or all versions of a named plug.         With 'from=all', a tag is only removed when it was set to all versions.         

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
from waylay.services.registry.models.tagging_scope_option import TaggingScopeOption
try:
    # Clear Tags On Any/All
    # calls `DELETE /registry/v2/plugs/{name}/tags`
    api_response = await waylay_client.registry.plug_tags.clear_all(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'scope': 'any'
        },
    )
    print("The response of registry.plug_tags.clear_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.clear_all: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scope']** (dict) <br> **query.scope** (Query) | [**TaggingScopeOption**](.md) | query parameter `"scope"` | Tagging operations on a _named_ function can either operate on - &#x60;any&#x60; versions: operate on tags that are are associated on _any_ version (union) - &#x60;all&#x60; versions: operate on tags that are are associated with _all_ versions (intersection) | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
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

# **clear**
> clear(
> name: str,
> version: str,
> headers
> ) -> FunctionTagsResponse

Clear Tags

Remove all tags used on a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
try:
    # Clear Tags
    # calls `DELETE /registry/v2/plugs/{name}/versions/{version}/tags`
    api_response = await waylay_client.registry.plug_tags.clear(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.plug_tags.clear:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.clear: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}/versions/{version}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
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

# **find_all**
> find_all(
> tag_name: str,
> name: str,
> query: FindAllQuery,
> headers
> ) -> FunctionTagResponse

Find Tags On Any/All

Check the existence of a tag on any or all versions of a named plug.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tag_response import FunctionTagResponse
from waylay.services.registry.models.tagging_scope_option import TaggingScopeOption
try:
    # Find Tags On Any/All
    # calls `GET /registry/v2/plugs/{name}/tags/{tagName}`
    api_response = await waylay_client.registry.plug_tags.find_all(
        'tag_name_example', # tag_name | path param "tagName"
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'scope': 'any'
        },
    )
    print("The response of registry.plug_tags.find_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.find_all: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scope']** (dict) <br> **query.scope** (Query) | [**TaggingScopeOption**](.md) | query parameter `"scope"` | Tagging operations on a _named_ function can either operate on - &#x60;any&#x60; versions: operate on tags that are are associated on _any_ version (union) - &#x60;all&#x60; versions: operate on tags that are are associated with _all_ versions (intersection) | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagResponse`** |  | [FunctionTagResponse](FunctionTagResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**404** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find**
> find(
> tag_name: str,
> name: str,
> version: str,
> headers
> ) -> FunctionTagResponse

Find Tag

Check the existence of a tag on a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tag_response import FunctionTagResponse
try:
    # Find Tag
    # calls `GET /registry/v2/plugs/{name}/versions/{version}/tags/{tagName}`
    api_response = await waylay_client.registry.plug_tags.find(
        'tag_name_example', # tag_name | path param "tagName"
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.plug_tags.find:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.find: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions/{version}/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagResponse`** |  | [FunctionTagResponse](FunctionTagResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**404** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_all**
> list_all(
> name: str,
> query: ListAllQuery,
> headers
> ) -> FunctionTagsResponse

List Tags On Any/All

List tags used on any or all versions of a named plug.         With 'from=all', only the tags that are set to all versions are returned.         

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
from waylay.services.registry.models.tagging_scope_option import TaggingScopeOption
try:
    # List Tags On Any/All
    # calls `GET /registry/v2/plugs/{name}/tags`
    api_response = await waylay_client.registry.plug_tags.list_all(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'scope': 'any'
        },
    )
    print("The response of registry.plug_tags.list_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.list_all: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scope']** (dict) <br> **query.scope** (Query) | [**TaggingScopeOption**](.md) | query parameter `"scope"` | Tagging operations on a _named_ function can either operate on - &#x60;any&#x60; versions: operate on tags that are are associated on _any_ version (union) - &#x60;all&#x60; versions: operate on tags that are are associated with _all_ versions (intersection) | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
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
> name: str,
> version: str,
> headers
> ) -> FunctionTagsResponse

List Tags

List tags used on a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
try:
    # List Tags
    # calls `GET /registry/v2/plugs/{name}/versions/{version}/tags`
    api_response = await waylay_client.registry.plug_tags.list(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.plug_tags.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/plugs/{name}/versions/{version}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
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

# **put_all**
> put_all(
> tag_name: str,
> name: str,
> headers
> ) -> FunctionTagResponse

Put Tag On All

Add a tag on on all versions of a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tag_response import FunctionTagResponse
try:
    # Put Tag On All
    # calls `PUT /registry/v2/plugs/{name}/tags/{tagName}`
    api_response = await waylay_client.registry.plug_tags.put_all(
        'tag_name_example', # tag_name | path param "tagName"
        'name_example', # name | path param "name"
    )
    print("The response of registry.plug_tags.put_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.put_all: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/plugs/{name}/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
**name** | **str** | path parameter `"name"` | The name of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagResponse`** |  | [FunctionTagResponse](FunctionTagResponse.md)
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

# **put**
> put(
> tag_name: str,
> name: str,
> version: str,
> headers
> ) -> FunctionTagResponse

Put Tag

Put a tag on a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tag_response import FunctionTagResponse
try:
    # Put Tag
    # calls `PUT /registry/v2/plugs/{name}/versions/{version}/tags/{tagName}`
    api_response = await waylay_client.registry.plug_tags.put(
        'tag_name_example', # tag_name | path param "tagName"
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.plug_tags.put:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.put: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/plugs/{name}/versions/{version}/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagResponse`** |  | [FunctionTagResponse](FunctionTagResponse.md)
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

# **remove_all**
> remove_all(
> tag_name: str,
> name: str,
> headers
> ) -> FunctionTagResponse

Remove Tag On Any/All

Remove a tag on any or all version from a plug version.         With 'from=all', the tag is only removed when it exists on all versions.         

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tag_response import FunctionTagResponse
try:
    # Remove Tag On Any/All
    # calls `DELETE /registry/v2/plugs/{name}/tags/{tagName}`
    api_response = await waylay_client.registry.plug_tags.remove_all(
        'tag_name_example', # tag_name | path param "tagName"
        'name_example', # name | path param "name"
    )
    print("The response of registry.plug_tags.remove_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.remove_all: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
**name** | **str** | path parameter `"name"` | The name of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagResponse`** |  | [FunctionTagResponse](FunctionTagResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**404** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(
> tag_name: str,
> name: str,
> version: str,
> headers
> ) -> FunctionTagResponse

Remove Tag

Remove a tag from a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tag_response import FunctionTagResponse
try:
    # Remove Tag
    # calls `DELETE /registry/v2/plugs/{name}/versions/{version}/tags/{tagName}`
    api_response = await waylay_client.registry.plug_tags.remove(
        'tag_name_example', # tag_name | path param "tagName"
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
    )
    print("The response of registry.plug_tags.remove:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.remove: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/plugs/{name}/versions/{version}/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagResponse`** |  | [FunctionTagResponse](FunctionTagResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |
**404** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_all**
> replace_all(
> name: str,
> query: ReplaceAllQuery,
> headers
> ) -> FunctionTagsResponse

Replace Tags On Any/All

Replace tags used on any or all versions of a named plug.         With 'from=all', only the tags that were set to all versions are replaced.         

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
from waylay.services.registry.models.tagging_scope_option import TaggingScopeOption
from waylay.services.registry.models.update_tags_request_v2 import UpdateTagsRequestV2
try:
    # Replace Tags On Any/All
    # calls `PUT /registry/v2/plugs/{name}/tags`
    api_response = await waylay_client.registry.plug_tags.replace_all(
        'name_example', # name | path param "name"
        # query parameters:
        query = {
            'scope': 'any'
        },
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.UpdateTagsRequestV2() # UpdateTagsRequestV2 |  (optional)
    )
    print("The response of registry.plug_tags.replace_all:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.replace_all: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/plugs/{name}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**json** | [**UpdateTagsRequestV2**](UpdateTagsRequestV2.md) | json request body |  | [optional] 
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['scope']** (dict) <br> **query.scope** (Query) | [**TaggingScopeOption**](.md) | query parameter `"scope"` | Tagging operations on a _named_ function can either operate on - &#x60;any&#x60; versions: operate on tags that are are associated on _any_ version (union) - &#x60;all&#x60; versions: operate on tags that are are associated with _all_ versions (intersection) | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace**
> replace(
> name: str,
> version: str,
> headers
> ) -> FunctionTagsResponse

Replace Tags

Replace tags used on a plug version.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse
from waylay.services.registry.models.update_tags_request_v2 import UpdateTagsRequestV2
try:
    # Replace Tags
    # calls `PUT /registry/v2/plugs/{name}/versions/{version}/tags`
    api_response = await waylay_client.registry.plug_tags.replace(
        'name_example', # name | path param "name"
        'version_example', # version | path param "version"
        # json data: use a generated model or a json-serializable python data structure (dict, list)
        json = waylay.services.registry.UpdateTagsRequestV2() # UpdateTagsRequestV2 |  (optional)
    )
    print("The response of registry.plug_tags.replace:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.plug_tags.replace: %s\n" % e)
```

### Endpoint
```
PUT /registry/v2/plugs/{name}/versions/{version}/tags
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**name** | **str** | path parameter `"name"` | The name of the function. | 
**version** | **str** | path parameter `"version"` | The version of the function. | 
**json** | [**UpdateTagsRequestV2**](UpdateTagsRequestV2.md) | json request body |  | [optional] 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`FunctionTagsResponse`** |  | [FunctionTagsResponse](FunctionTagsResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

