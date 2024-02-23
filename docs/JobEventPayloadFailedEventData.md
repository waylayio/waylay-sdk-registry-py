# JobEventPayloadFailedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobReference**](JobReference.md) |  | 
**data** | [**FailedEventData**](FailedEventData.md) |  | 
**timestamp** | **datetime** | Timestamp of the event | 

## Example

```python
from waylay.services.registry.models.job_event_payload_failed_event_data import JobEventPayloadFailedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventPayloadFailedEventData from a JSON string
job_event_payload_failed_event_data_instance = JobEventPayloadFailedEventData.from_json(json)
# print the JSON string representation of the object
print JobEventPayloadFailedEventData.to_json()

# convert the object into a dict
job_event_payload_failed_event_data_dict = job_event_payload_failed_event_data_instance.to_dict()
# create an instance of JobEventPayloadFailedEventData from a dict
job_event_payload_failed_event_data_form_dict = job_event_payload_failed_event_data.from_dict(job_event_payload_failed_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


