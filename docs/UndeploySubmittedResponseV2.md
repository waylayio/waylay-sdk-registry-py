# UndeploySubmittedResponseV2

Undeployment Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**versions** | **List[str]** | The versions for which undeployment and/or removal is initiated. | 

## Example

```python
from waylay.services.registry.models.undeploy_submitted_response_v2 import UndeploySubmittedResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of UndeploySubmittedResponseV2 from a JSON string
undeploy_submitted_response_v2_instance = UndeploySubmittedResponseV2.from_json(json)
# print the JSON string representation of the object
print UndeploySubmittedResponseV2.to_json()

# convert the object into a dict
undeploy_submitted_response_v2_dict = undeploy_submitted_response_v2_instance.to_dict()
# create an instance of UndeploySubmittedResponseV2 from a dict
undeploy_submitted_response_v2_form_dict = undeploy_submitted_response_v2.from_dict(undeploy_submitted_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


