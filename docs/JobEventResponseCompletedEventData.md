# JobEventResponseCompletedEventData

Event object describing a state change of a background job.

**Source:** `waylay.services.registry.models.job_event_response_completed_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobStatusAndEntityHALLinks**](JobStatusAndEntityHALLinks.md) |  | 
**job** | [**JobReference**](JobReference.md) |  | 
**data** | [**CompletedEventData**](CompletedEventData.md) |  | 
**timestamp** | **datetime** | Timestamp of the event | 
**function** | [**FunctionRef**](FunctionRef.md) |  | 


## Example

```python
from waylay.services.registry.models.job_event_response_completed_event_data import (
    JobEventResponseCompletedEventData,
)

job_event_response_completed_event_data = JobEventResponseCompletedEventData(
    links=..., job=..., data=..., timestamp=..., function=...
)

# Create from JSON
job_event_response_completed_event_data = JobEventResponseCompletedEventData.from_json(
    '{ "_links": ..., "job": ..., "data": ..., "timestamp": ..., "function": ... }'
)

# Export to dictionary
job_event_response_completed_event_data_dict = (
    job_event_response_completed_event_data.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


