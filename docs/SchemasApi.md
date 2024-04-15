# waylay.services.registry.SchemasApi

All URIs are relative to *https://api-aws-dev.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_role**](SchemasApi.md#get_by_role) | **GET** /registry/v2/schemas/{functionType}/{role}/schema | Get Asset Schema
[**get**](SchemasApi.md#get) | **GET** /registry/v2/schemas/{schemaId} | Get Asset Schema

# **get_by_role**
> get_by_role(
> function_type: FunctionType,
> role: AssetRole,
> headers
> ) -> Dict[str, object]

Get Asset Schema

Get the JSON schema that is used to validate the asset.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.asset_role import AssetRole
from waylay.services.registry.models.function_type import FunctionType
try:
    # Get Asset Schema
    # calls `GET /registry/v2/schemas/{functionType}/{role}/schema`
    api_response = await waylay_client.registry.schemas.get_by_role(
        'plugs', # function_type | path param "functionType"
        'manifest', # role | path param "role"
    )
    print("The response of registry.schemas.get_by_role:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.schemas.get_by_role: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/schemas/{functionType}/{role}/schema
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**function_type** | [**FunctionType**](.md) | path parameter `"functionType"` | Function type | 
**role** | [**AssetRole**](.md) | path parameter `"role"` | Asset role | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`Dict[str, object]`** |  | 
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
> schema_id: str,
> headers
> ) -> Dict[str, object]

Get Asset Schema

Get the JSON schema that is used to validate an asset.

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
    # Get Asset Schema
    # calls `GET /registry/v2/schemas/{schemaId}`
    api_response = await waylay_client.registry.schemas.get(
        'schema_id_example', # schema_id | path param "schemaId"
    )
    print("The response of registry.schemas.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.schemas.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/schemas/{schemaId}
```
### Parameters

Name     | Type  | API binding   | Description   | Notes
-------- | ----- | ------------- | ------------- | -------------
**schema_id** | **str** | path parameter `"schemaId"` | Schema id | 
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`Dict[str, object]`** |  | 
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

