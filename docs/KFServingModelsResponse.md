# KFServingModelsResponse

Successful Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | [**List[KFServingResponse]**](KFServingResponse.md) |  | 
**paging** | [**PagingResponse**](PagingResponse.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.kf_serving_models_response import KFServingModelsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KFServingModelsResponse from a JSON string
kf_serving_models_response_instance = KFServingModelsResponse.from_json(json)
# print the JSON string representation of the object
print KFServingModelsResponse.to_json()

# convert the object into a dict
kf_serving_models_response_dict = kf_serving_models_response_instance.to_dict()
# create an instance of KFServingModelsResponse from a dict
kf_serving_models_response_form_dict = kf_serving_models_response.from_dict(kf_serving_models_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


