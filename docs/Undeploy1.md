# Undeploy1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the background task. | 
**operation** | **str** | The operation name for the background task. | 
**id** | **str** | The id of the background job, or the constant &#x60;_unknown_&#x60; | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**created_at** | **datetime** | The creation time of this job | 
**created_by** | **str** | The user that initiated this job | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**links** | [**JobAndFunctionHALLink**](JobAndFunctionHALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.undeploy1 import Undeploy1

# TODO update the JSON string below
json = "{}"
# create an instance of Undeploy1 from a JSON string
undeploy1_instance = Undeploy1.from_json(json)
# print the JSON string representation of the object
print Undeploy1.to_json()

# convert the object into a dict
undeploy1_dict = undeploy1_instance.to_dict()
# create an instance of Undeploy1 from a dict
undeploy1_form_dict = undeploy1.from_dict(undeploy1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


