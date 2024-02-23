# ModelVersionsResponseV2

Model Versions Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The page size used for this query result. | [optional] 
**count** | **float** | The total count of matching items, from which this result is one page. | 
**page** | **float** | The page number of a paged query result. | [optional] 
**entities** | [**List[KfservingResponseV2]**](KfservingResponseV2.md) | The specification and deployment status of the queried functions | 

## Example

```python
from waylay.services.registry.models.model_versions_response_v2 import ModelVersionsResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of ModelVersionsResponseV2 from a JSON string
model_versions_response_v2_instance = ModelVersionsResponseV2.from_json(json)
# print the JSON string representation of the object
print ModelVersionsResponseV2.to_json()

# convert the object into a dict
model_versions_response_v2_dict = model_versions_response_v2_instance.to_dict()
# create an instance of ModelVersionsResponseV2 from a dict
model_versions_response_v2_form_dict = model_versions_response_v2.from_dict(model_versions_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


