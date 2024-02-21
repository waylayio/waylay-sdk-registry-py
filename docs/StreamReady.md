# StreamReady

A message that acknowledges that the server will sent job state changes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventAck**](EventAck.md) |  | 
**data** | **str** | A text message acknowledging what events will be forwarded. | 

## Example

```python
from waylay.services.registry.models.stream_ready import StreamReady

# TODO update the JSON string below
json = "{}"
# create an instance of StreamReady from a JSON string
stream_ready_instance = StreamReady.from_json(json)
# print the JSON string representation of the object
print StreamReady.to_json()

# convert the object into a dict
stream_ready_dict = stream_ready_instance.to_dict()
# create an instance of StreamReady from a dict
stream_ready_form_dict = stream_ready.from_dict(stream_ready_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


