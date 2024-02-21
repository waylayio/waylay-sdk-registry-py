# Deploy1


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
from waylay.services.registry.models.deploy1 import Deploy1

# TODO update the JSON string below
json = "{}"
# create an instance of Deploy1 from a JSON string
deploy1_instance = Deploy1.from_json(json)
# print the JSON string representation of the object
print Deploy1.to_json()

# convert the object into a dict
deploy1_dict = deploy1_instance.to_dict()
# create an instance of Deploy1 from a dict
deploy1_form_dict = deploy1.from_dict(deploy1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


