# DelayedEventData


**Source:** `waylay.services.registry.models.delayed_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay** | **float** |  | 


## Example

```python
from waylay.services.registry.models.delayed_event_data import DelayedEventData

delayed_event_data = DelayedEventData(delay=...)

# Create from JSON
delayed_event_data = DelayedEventData.from_json('{ "delay": ... }')

# Export to dictionary
delayed_event_data_dict = delayed_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


