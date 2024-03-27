# Scale1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScaleType**](ScaleType.md) |  | 
**operation** | **str** | The operation name for the background task. | 
**id** | **str** | The id of the background job, or the constant &#x60;_unknown_&#x60; | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**created_at** | **datetime** | The creation time of this job | 
**created_by** | **str** | The user that initiated this job | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**links** | [**JobAndFunctionHALLink**](JobAndFunctionHALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.scale1 import Scale1

# TODO update the JSON string below
json = "{}"
# create an instance of Scale1 from a JSON string
scale1_instance = Scale1.from_json(json)
# print the JSON string representation of the object
print Scale1.to_json()

# convert the object into a dict
scale1_dict = scale1_instance.to_dict()
# create an instance of Scale1 from a dict
scale1_form_dict = scale1.from_dict(scale1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


