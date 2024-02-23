# JobEventPayloadWaitingEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobReference**](JobReference.md) |  | 
**data** | [**WaitingEventData**](WaitingEventData.md) |  | 
**timestamp** | **datetime** | Timestamp of the event | 

## Example

```python
from waylay.services.registry.models.job_event_payload_waiting_event_data import JobEventPayloadWaitingEventData

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventPayloadWaitingEventData from a JSON string
job_event_payload_waiting_event_data_instance = JobEventPayloadWaitingEventData.from_json(json)
# print the JSON string representation of the object
print JobEventPayloadWaitingEventData.to_json()

# convert the object into a dict
job_event_payload_waiting_event_data_dict = job_event_payload_waiting_event_data_instance.to_dict()
# create an instance of JobEventPayloadWaitingEventData from a dict
job_event_payload_waiting_event_data_form_dict = job_event_payload_waiting_event_data.from_dict(job_event_payload_waiting_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


