# RebuildComputedResponse

Rebuild Ignored

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 

## Example

```python
from waylay.services.registry.models.rebuild_computed_response import RebuildComputedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildComputedResponse from a JSON string
rebuild_computed_response_instance = RebuildComputedResponse.from_json(json)
# print the JSON string representation of the object
print RebuildComputedResponse.to_json()

# convert the object into a dict
rebuild_computed_response_dict = rebuild_computed_response_instance.to_dict()
# create an instance of RebuildComputedResponse from a dict
rebuild_computed_response_form_dict = rebuild_computed_response.from_dict(rebuild_computed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


