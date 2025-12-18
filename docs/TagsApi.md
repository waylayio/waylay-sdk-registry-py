# waylay.services.registry.TagsApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](TagsApi.md#get) | **GET** /registry/v2/tags/{tagName} | Get
[**list**](TagsApi.md#list) | **GET** /registry/v2/tags/ | List
[**remove**](TagsApi.md#remove) | **DELETE** /registry/v2/tags/ | Remove Unused

# **get**
> get(
> tag_name: str,
> headers
> ) -> FunctionTagResponse

Get

Get the metadata of a function Tag by name.

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
    # Get
    # calls `GET /registry/v2/tags/{tagName}`
    api_response = await waylay_client.registry.tags.get(
        'tag_name_example', # tag_name | path param "tagName"
    )
    print("The response of registry.tags.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.tags.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/tags/{tagName}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**tag_name** | **str** | path parameter `"tagName"` | The name of the tag that might be applied to a function. | 
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
**200** | Function Tag Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list**
> list(
> query: ListQuery,
> headers
> ) -> FunctionTagsResponse

List

List tags used on any plug, webscript or model.

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
    # List
    # calls `GET /registry/v2/tags/`
    api_response = await waylay_client.registry.tags.list(
        # query parameters:
        query = {
            'name': '*-demo-??'
            'color': '#4153ea'
        },
    )
    print("The response of registry.tags.list:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.tags.list: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/tags/
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**query** | [QueryParamTypes](Operation.md#req_arg_query) \| **None** | URL query parameter |  | 
**query['name']** (dict) <br> **query.name** (Query) | **str** | query parameter `"name"` | If set, filters on the &lt;code&gt;name&lt;/code&gt; of a tag. Supports &lt;code&gt;*&lt;/code&gt; and &lt;code&gt;?&lt;/code&gt; wildcards and is case-insensitive. | [optional] 
**query['color']** (dict) <br> **query.color** (Query) | **str** | query parameter `"color"` | If set, filters on the &lt;code&gt;color&lt;/code&gt; of a tag. Uses an exact match. | [optional] 
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
**200** | Function Tags Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove**
> remove(
> headers
> ) -> FunctionTagsResponse

Remove Unused

Remove tags that are not referenced by any plug, webscript or model. This is normally executed as background task.

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
    # Remove Unused
    # calls `DELETE /registry/v2/tags/`
    api_response = await waylay_client.registry.tags.remove(
    )
    print("The response of registry.tags.remove:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.tags.remove: %s\n" % e)
```

### Endpoint
```
DELETE /registry/v2/tags/
```
### Parameters

This endpoint does not need any parameter.
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
**200** | Function Tags Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

