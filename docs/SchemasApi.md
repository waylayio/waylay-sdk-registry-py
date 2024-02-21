# waylay.services.registry.SchemasApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_role**](SchemasApi.md#get_by_role) | **GET** /registry/v2/schemas/{functionType}/{role}/schema | Get Asset Schema
[**get**](SchemasApi.md#get) | **GET** /registry/v2/schemas/{schemaId} | Get Asset Schema


# **get_by_role**
> Dict[str, object] get_by_role(function_type, role)

Get Asset Schema

Get the JSON schema that is used to validate the asset.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.asset_role import AssetRole
from waylay.services.registry.models.function_type import FunctionType
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
    api_instance = waylay.services.registry.SchemasApi(api_client)
    function_type = waylay.services.registry.FunctionType() # FunctionType | Function type
    role = waylay.services.registry.AssetRole() # AssetRole | Asset role

    try:
        # Get Asset Schema
        api_response = await api_instance.get_by_role(function_type, role)
        print("The response of SchemasApi->get_by_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get_by_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function_type** | [**FunctionType**](.md)| Function type | 
 **role** | [**AssetRole**](.md)| Asset role | 

### Return type

**Dict[str, object]**

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
> Dict[str, object] get(schema_id)

Get Asset Schema

Get the JSON schema that is used to validate an asset.

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
    api_instance = waylay.services.registry.SchemasApi(api_client)
    schema_id = 'schema_id_example' # str | Schema id

    try:
        # Get Asset Schema
        api_response = await api_instance.get(schema_id)
        print("The response of SchemasApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SchemasApi->get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_id** | **str**| Schema id | 

### Return type

**Dict[str, object]**

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

