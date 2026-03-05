# BuildJobStatus


**Source:** `waylay.services.registry.models.build_job_status`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**BuildJobStatusType**](BuildJobStatusType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**BuildArgs**](BuildArgs.md) |  | 
**result** | [**BuildResult**](BuildResult.md) |  | [optional] 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 


## Example

```python
from waylay.services.registry.models.build_job_status import BuildJobStatus

build_job_status = BuildJobStatus(
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
build_job_status = BuildJobStatus.from_json(
    '{ "operation": ..., "createdBy": ..., "createdAt": ..., "processedAt": ..., "finishedAt": ..., "attemptsMade": ..., "type": ..., "state": ..., "request": ..., "result": ..., "function": ..., "job": ... }'
)

# Export to dictionary
build_job_status_dict = build_job_status.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


