# ActiveEventData


**Source:** `waylay.services.registry.models.active_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.active_event_data import ActiveEventData

active_event_data = ActiveEventData(prev=...)

# Create from JSON
active_event_data = ActiveEventData.from_json('{ "prev": ... }')

# Export to dictionary
active_event_data_dict = active_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


