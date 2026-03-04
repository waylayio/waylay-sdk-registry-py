# VerifyJobStatus


**Source:** `waylay.services.registry.models.verify_job_status`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**VerifyJobStatusType**](VerifyJobStatusType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**VerifyArgs**](VerifyArgs.md) |  | 
**result** | [**VerifyResult**](VerifyResult.md) |  | [optional] 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 


## Example

```python
from waylay.services.registry.models.verify_job_status import VerifyJobStatus

verify_job_status = VerifyJobStatus(
    operation=...,
    created_by=...,
    created_at=...,
    processed_at=...,
    finished_at=...,
    attempts_made=...,
    type=...,
    state=...,
    request=...,
    result=...,
    function=...,
    job=...,
)

# Create from JSON
verify_job_status = VerifyJobStatus.from_json(
    '{ "operation": ..., "createdBy": ..., "createdAt": ..., "processedAt": ..., "finishedAt": ..., "attemptsMade": ..., "type": ..., "state": ..., "request": ..., "result": ..., "function": ..., "job": ... }'
)

# Export to dictionary
verify_job_status_dict = verify_job_status.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


