# Scale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**type** | [**ScaleType**](ScaleType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**ScaleArgs**](ScaleArgs.md) |  | [optional] 
**result** | **object** | The result data for a completed scale job. | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.scale import Scale

# TODO update the JSON string below
json = "{}"
# create an instance of Scale from a JSON string
scale_instance = Scale.from_json(json)
# print the JSON string representation of the object
print Scale.to_json()

# convert the object into a dict
scale_dict = scale_instance.to_dict()
# create an instance of Scale from a dict
scale_form_dict = scale.from_dict(scale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


