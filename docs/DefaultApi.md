# waylay.services.registry.DefaultApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](DefaultApi.md#get) | **GET** /registry/v2/ | Version


# **get**
> RootPageResponse get(query=GetQuery)

Version

Get the version of this function registry deployment.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

from waylay.services.registry.models.root_page_response import RootPageResponse



try:
    # Version
    api_response = await waylay_client.registry.default.get()
    print("The response of registry.default.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.default.get: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type


[**RootPageResponse**](RootPageResponse.md)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Default Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

