# waylay.services.registry.DefaultApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](DefaultApi.md#get) | **GET** /registry/v2/ | Version


# **get**
> RootPageResponse get()

Version

Get the version of this function registry deployment.

### Example

* Basic Authentication (waylayApiKeySecret):

```python
import time
import os
import waylay.services.registry
from waylay.services.registry.models.root_page_response import RootPageResponse
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
    api_instance = waylay.services.registry.DefaultApi(api_client)

    try:
        # Version
        api_response = await api_instance.get()
        print("The response of DefaultApi->get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**RootPageResponse**](RootPageResponse.md)

### Authorization

[waylayApiKeySecret](../README.md#waylayApiKeySecret)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

