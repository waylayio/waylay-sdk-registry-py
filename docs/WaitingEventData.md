# WaitingEventData


**Source:** `waylay.services.registry.models.waiting_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.waiting_event_data import WaitingEventData

waiting_event_data = WaitingEventData(prev=...)

# Create from JSON
waiting_event_data = WaitingEventData.from_json('{ "prev": ... }')

# Export to dictionary
waiting_event_data_dict = waiting_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


