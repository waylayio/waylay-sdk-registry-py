# DelayedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay** | **float** |  | 

## Example

```python
from waylay.services.registry.models.delayed_event_data import DelayedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of DelayedEventData from a JSON string
delayed_event_data_instance = DelayedEventData.from_json(json)
# print the JSON string representation of the object
print DelayedEventData.to_json()

# convert the object into a dict
delayed_event_data_dict = delayed_event_data_instance.to_dict()
# create an instance of DelayedEventData from a dict
delayed_event_data_form_dict = delayed_event_data.from_dict(delayed_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


