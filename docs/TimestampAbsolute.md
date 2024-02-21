# TimestampAbsolute

An absolute timestamp as an ISO8601 string

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.timestamp_absolute import TimestampAbsolute

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampAbsolute from a JSON string
timestamp_absolute_instance = TimestampAbsolute.from_json(json)
# print the JSON string representation of the object
print TimestampAbsolute.to_json()

# convert the object into a dict
timestamp_absolute_dict = timestamp_absolute_instance.to_dict()
# create an instance of TimestampAbsolute from a dict
timestamp_absolute_form_dict = timestamp_absolute.from_dict(timestamp_absolute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


