# VerifyJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**VerifyType**](VerifyType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**VerifyArgs**](VerifyArgs.md) |  | 
**result** | [**VerifyResult**](VerifyResult.md) |  | [optional] 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from waylay.services.registry.models.verify_job_status import VerifyJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyJobStatus from a JSON string
verify_job_status_instance = VerifyJobStatus.from_json(json)
# print the JSON string representation of the object
print VerifyJobStatus.to_json()

# convert the object into a dict
verify_job_status_dict = verify_job_status_instance.to_dict()
# create an instance of VerifyJobStatus from a dict
verify_job_status_form_dict = verify_job_status.from_dict(verify_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


