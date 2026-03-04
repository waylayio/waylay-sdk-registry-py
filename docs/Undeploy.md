# Undeploy


**Source:** `waylay.services.registry.models.undeploy`




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
**type** | [**AnyJobForFunctionUndeploy**](AnyJobForFunctionUndeploy.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**UndeployArgs**](UndeployArgs.md) |  | [optional] 
**result** | [**UndeployResult**](UndeployResult.md) |  | [optional] 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.undeploy import Undeploy

undeploy = Undeploy(
    links=...,
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
    failure_reason=...,
)

# Create from JSON
undeploy = Undeploy.from_json(
    '{ "_links": ..., "operation": ..., "createdBy": ..., "createdAt": ..., "processedAt": ..., "finishedAt": ..., "attemptsMade": ..., "type": ..., "state": ..., "request": ..., "result": ..., "function": ..., "job": ..., "failureReason": ... }'
)

# Export to dictionary
undeploy_dict = undeploy.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


