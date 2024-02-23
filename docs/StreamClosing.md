# StreamClosing

A message that notifies that the server will not send more events, and that the client should close.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**EventClose**](EventClose.md) |  | 
**data** | **str** | A text message describing the cause for closing the stream. | 

## Example

```python
from waylay.services.registry.models.stream_closing import StreamClosing

# TODO update the JSON string below
json = "{}"
# create an instance of StreamClosing from a JSON string
stream_closing_instance = StreamClosing.from_json(json)
# print the JSON string representation of the object
print StreamClosing.to_json()

# convert the object into a dict
stream_closing_dict = stream_closing_instance.to_dict()
# create an instance of StreamClosing from a dict
stream_closing_form_dict = stream_closing.from_dict(stream_closing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


