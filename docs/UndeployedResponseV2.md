# UndeployedResponseV2

Undeployed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**versions** | **List[str]** | The versions that were deprecated, undeployed and/or removed. | 

## Example

```python
from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of UndeployedResponseV2 from a JSON string
undeployed_response_v2_instance = UndeployedResponseV2.from_json(json)
# print the JSON string representation of the object
print UndeployedResponseV2.to_json()

# convert the object into a dict
undeployed_response_v2_dict = undeployed_response_v2_instance.to_dict()
# create an instance of UndeployedResponseV2 from a dict
undeployed_response_v2_form_dict = undeployed_response_v2.from_dict(undeployed_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


