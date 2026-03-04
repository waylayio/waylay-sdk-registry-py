# FailedEventData


**Source:** `waylay.services.registry.models.failed_event_data`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prev** | [**QueueEvents**](QueueEvents.md) |  | [optional] 
**failed_reason** | **str** | The failure reason of the job | 


## Example

```python
from waylay.services.registry.models.failed_event_data import FailedEventData

failed_event_data = FailedEventData(prev=..., failed_reason=...)

# Create from JSON
failed_event_data = FailedEventData.from_json('{ "prev": ..., "failedReason": ... }')

# Export to dictionary
failed_event_data_dict = failed_event_data.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


