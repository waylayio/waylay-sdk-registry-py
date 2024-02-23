# Build1


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
from waylay.services.registry.models.build1 import Build1

# TODO update the JSON string below
json = "{}"
# create an instance of Build1 from a JSON string
build1_instance = Build1.from_json(json)
# print the JSON string representation of the object
print Build1.to_json()

# convert the object into a dict
build1_dict = build1_instance.to_dict()
# create an instance of Build1 from a dict
build1_form_dict = build1.from_dict(build1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


