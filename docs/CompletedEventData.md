# CompletedEventData


**Source:** `waylay.services.registry.models.completed_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 
**returnvalue** | [**AnyJobResult**](AnyJobResult.md) |  | 


## Example

```python
from waylay.services.registry.models.completed_event_data import CompletedEventData

completed_event_data = CompletedEventData(prev=..., returnvalue=...)

# Create from JSON
completed_event_data = CompletedEventData.from_json(
    '{ "prev": ..., "returnvalue": ... }'
)

# Export to dictionary
completed_event_data_dict = completed_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


