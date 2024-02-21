# JobEventResponseCompletedEventData

Event object describing a state change of a background job.

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
from waylay.services.registry.models.job_event_response_completed_event_data import JobEventResponseCompletedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventResponseCompletedEventData from a JSON string
job_event_response_completed_event_data_instance = JobEventResponseCompletedEventData.from_json(json)
# print the JSON string representation of the object
print JobEventResponseCompletedEventData.to_json()

# convert the object into a dict
job_event_response_completed_event_data_dict = job_event_response_completed_event_data_instance.to_dict()
# create an instance of JobEventResponseCompletedEventData from a dict
job_event_response_completed_event_data_form_dict = job_event_response_completed_event_data.from_dict(job_event_response_completed_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


