# waylay.services.registry.SchemasApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_role**](SchemasApi.md#get_by_role) | **GET** /registry/v2/schemas/{functionType}/{role}/schema | Get Asset Schema
[**get**](SchemasApi.md#get) | **GET** /registry/v2/schemas/{schemaId} | Get Asset Schema


# **get_by_role**
> Dict[str, object] get_by_role(function_type: FunctionType, role: AssetRole, query=GetByRoleQuery)

Get Asset Schema

Get the JSON schema that is used to validate the asset.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.asset_role import AssetRole
from waylay.services.registry.models.function_type import FunctionType

function_type = waylay.services.registry.FunctionType() # FunctionType | Function type,
role = waylay.services.registry.AssetRole() # AssetRole | Asset role,


try:
    # Get Asset Schema
    api_response = await waylay_client.registry.schemas.get_by_role(function_type=function_type, role=role, )
    print("The response of registry.schemas.get_by_role:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.schemas.get_by_role: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_type** | [**FunctionType**](.md)| Function type | 
 **role** | [**AssetRole**](.md)| Asset role | 

### Return type


**Dict[str, object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> Dict[str, object] get(schema_id: str, query=GetQuery)

Get Asset Schema

Get the JSON schema that is used to validate an asset.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()


schema_id = 'schema_id_example' # str | Schema id,


try:
    # Get Asset Schema
    api_response = await waylay_client.registry.schemas.get(schema_id=schema_id, )
    print("The response of registry.schemas.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.schemas.get: %s\n" % e)
```

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema id | 

### Return type


**Dict[str, object]**

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

