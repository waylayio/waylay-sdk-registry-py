# RebuildModelAsyncResponseV2

Model Rebuild Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 

## Example

```python
from waylay.services.registry.models.rebuild_model_async_response_v2 import RebuildModelAsyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildModelAsyncResponseV2 from a JSON string
rebuild_model_async_response_v2_instance = RebuildModelAsyncResponseV2.from_json(json)
# print the JSON string representation of the object
print RebuildModelAsyncResponseV2.to_json()

# convert the object into a dict
rebuild_model_async_response_v2_dict = rebuild_model_async_response_v2_instance.to_dict()
# create an instance of RebuildModelAsyncResponseV2 from a dict
rebuild_model_async_response_v2_form_dict = rebuild_model_async_response_v2.from_dict(rebuild_model_async_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


