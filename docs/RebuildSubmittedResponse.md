# RebuildSubmittedResponse

Rebuild Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 

## Example

```python
from waylay.services.registry.models.rebuild_submitted_response import RebuildSubmittedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildSubmittedResponse from a JSON string
rebuild_submitted_response_instance = RebuildSubmittedResponse.from_json(json)
# print the JSON string representation of the object
print RebuildSubmittedResponse.to_json()

# convert the object into a dict
rebuild_submitted_response_dict = rebuild_submitted_response_instance.to_dict()
# create an instance of RebuildSubmittedResponse from a dict
rebuild_submitted_response_form_dict = rebuild_submitted_response.from_dict(rebuild_submitted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


