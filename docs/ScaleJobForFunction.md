# ScaleJobForFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**type** | **str** | The type of the background task. | 
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
from waylay.services.registry.models.scale_job_for_function import ScaleJobForFunction

# TODO update the JSON string below
json = "{}"
# create an instance of ScaleJobForFunction from a JSON string
scale_job_for_function_instance = ScaleJobForFunction.from_json(json)
# print the JSON string representation of the object
print ScaleJobForFunction.to_json()

# convert the object into a dict
scale_job_for_function_dict = scale_job_for_function_instance.to_dict()
# create an instance of ScaleJobForFunction from a dict
scale_job_for_function_form_dict = scale_job_for_function.from_dict(scale_job_for_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


