# VerifyJobForFunction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**type** | **str** | The type of the background task. | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**VerifyArgs**](VerifyArgs.md) |  | [optional] 
**result** | [**VerifyResult**](VerifyResult.md) |  | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.verify_job_for_function import VerifyJobForFunction

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyJobForFunction from a JSON string
verify_job_for_function_instance = VerifyJobForFunction.from_json(json)
# print the JSON string representation of the object
print VerifyJobForFunction.to_json()

# convert the object into a dict
verify_job_for_function_dict = verify_job_for_function_instance.to_dict()
# create an instance of VerifyJobForFunction from a dict
verify_job_for_function_form_dict = verify_job_for_function.from_dict(verify_job_for_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


