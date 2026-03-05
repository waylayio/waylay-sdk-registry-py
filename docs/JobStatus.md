# JobStatus


**Source:** `waylay.services.registry.models.job_status`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**progress** | [**JobStatusProgress**](JobStatusProgress.md) |  | 
**attempts_made** | **float** |  | 
**finished_on** | **datetime** |  | [optional] 
**processed_on** | **datetime** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**parent** | [**ParentKeys**](ParentKeys.md) |  | [optional] 
**delay** | **float** |  | [optional] 


## Example

```python
from waylay.services.registry.models.job_status import JobStatus

job_status = JobStatus(
    id=...,
    name=...,
    progress=...,
    attempts_made=...,
    finished_on=...,
    processed_on=...,
    failed_reason=...,
    parent=...,
    delay=...,
)

# Create from JSON
job_status = JobStatus.from_json(
    '{ "id": ..., "name": ..., "progress": ..., "attemptsMade": ..., "finishedOn": ..., "processedOn": ..., "failedReason": ..., "parent": ..., "delay": ... }'
)

# Export to dictionary
job_status_dict = job_status.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


