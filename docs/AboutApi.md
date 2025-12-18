# waylay.services.registry.AboutApi

All URIs are relative to *https://api.waylay.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](AboutApi.md#get) | **GET** /registry/v2/ | Get Service Status

# **get**
> get(
> headers
> ) -> RootPageResponse

Get Service Status

Get the status and version of the function registry service.

### Example

```python
from pprint import pprint

# Import the waylay-client from the waylay-sdk-core package
from waylay.sdk.client import WaylayClient
from waylay.sdk.api.api_exceptions import ApiError

# Intialize a waylay client instance
waylay_client = WaylayClient.from_profile()

# Note that the typed model classes for responses/parameters/... are only available when `waylay-sdk-registry-types` is installed
from waylay.services.registry.models.root_page_response import RootPageResponse
try:
    # Get Service Status
    # calls `GET /registry/v2/`
    api_response = await waylay_client.registry.about.get(
    )
    print("The response of registry.about.get:\n")
    pprint(api_response)
except ApiError as e:
    print("Exception when calling registry.about.get: %s\n" % e)
```

### Endpoint
```
GET /registry/v2/
```
### Parameters

This endpoint does not need any parameter.
**headers** | [HeaderTypes](Operation.md#req_headers) | request headers |  | 

### Return type

Selected path param | Raw response param | Return Type  | Description | Links
------------------- | ------------------ | ------------ | ----------- | -----
Literal[""] _(default)_  | False _(default)_ | **`RootPageResponse`** |  | [RootPageResponse](RootPageResponse.md)
str | False _(default)_ | **`Any`** | If any other string value for the selected path is provided, the exact type of the response will only be known at runtime. | 
/ | True | `Response` | The raw http response object.

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | Status Page |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

