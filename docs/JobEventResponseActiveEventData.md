# JobEventResponseActiveEventData

Event object describing a state change of a background job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobStatusAndEntityHALLinks**](JobStatusAndEntityHALLinks.md) |  | 
**job** | [**JobReference**](JobReference.md) |  | 
**data** | [**ActiveEventData**](ActiveEventData.md) |  | 
**timestamp** | **datetime** | Timestamp of the event | 
**function** | [**FunctionRef**](FunctionRef.md) |  | 

## Example

```python
from waylay.services.registry.models.job_event_response_active_event_data import JobEventResponseActiveEventData

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventResponseActiveEventData from a JSON string
job_event_response_active_event_data_instance = JobEventResponseActiveEventData.from_json(json)
# print the JSON string representation of the object
print JobEventResponseActiveEventData.to_json()

# convert the object into a dict
job_event_response_active_event_data_dict = job_event_response_active_event_data_instance.to_dict()
# create an instance of JobEventResponseActiveEventData from a dict
job_event_response_active_event_data_form_dict = job_event_response_active_event_data.from_dict(job_event_response_active_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


