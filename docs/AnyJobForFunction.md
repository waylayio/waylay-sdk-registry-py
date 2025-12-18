# AnyJobForFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**ScaleType**](ScaleType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**ScaleArgs**](ScaleArgs.md) |  | [optional] 
**result** | **object** | The result data for a completed scale job. | [optional] 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.any_job_for_function import AnyJobForFunction

# TODO update the JSON string below
json = "{}"
# create an instance of AnyJobForFunction from a JSON string
any_job_for_function_instance = AnyJobForFunction.from_json(json)
# print the JSON string representation of the object
print AnyJobForFunction.to_json()

# convert the object into a dict
any_job_for_function_dict = any_job_for_function_instance.to_dict()
# create an instance of AnyJobForFunction from a dict
any_job_for_function_form_dict = any_job_for_function.from_dict(any_job_for_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


