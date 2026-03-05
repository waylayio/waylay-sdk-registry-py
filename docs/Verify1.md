# Verify1


**Source:** `waylay.services.registry.models.verify1`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**AnyJobStatusSummaryVerify**](AnyJobStatusSummaryVerify.md) |  | 
**id** | **str** | The id of the background job, or the constant &#x60;_unknown_&#x60; | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**links** | [**JobAndFunctionHALLink**](JobAndFunctionHALLink.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.verify1 import Verify1

verify1 = Verify1(
    operation=...,
    created_by=...,
    created_at=...,
    processed_at=...,
    finished_at=...,
    attempts_made=...,
    type=...,
    id=...,
    state=...,
    function=...,
    links=...,
)

# Create from JSON
verify1 = Verify1.from_json(
    '{ "operation": ..., "createdBy": ..., "createdAt": ..., "processedAt": ..., "finishedAt": ..., "attemptsMade": ..., "type": ..., "id": ..., "state": ..., "function": ..., "_links": ... }'
)

# Export to dictionary
verify1_dict = verify1.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


