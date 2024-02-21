# CreateKFServingAsyncResponse

Model Deployment Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**entity** | [**KFServingManifest**](KFServingManifest.md) |  | 

## Example

```python
from waylay.services.registry.models.create_kf_serving_async_response import CreateKFServingAsyncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKFServingAsyncResponse from a JSON string
create_kf_serving_async_response_instance = CreateKFServingAsyncResponse.from_json(json)
# print the JSON string representation of the object
print CreateKFServingAsyncResponse.to_json()

# convert the object into a dict
create_kf_serving_async_response_dict = create_kf_serving_async_response_instance.to_dict()
# create an instance of CreateKFServingAsyncResponse from a dict
create_kf_serving_async_response_form_dict = create_kf_serving_async_response.from_dict(create_kf_serving_async_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


