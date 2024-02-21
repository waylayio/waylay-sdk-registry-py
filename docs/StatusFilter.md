# StatusFilter

Inclusion or exclusion filter on the `status` property.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.status_filter import StatusFilter

# TODO update the JSON string below
json = "{}"
# create an instance of StatusFilter from a JSON string
status_filter_instance = StatusFilter.from_json(json)
# print the JSON string representation of the object
print StatusFilter.to_json()

# convert the object into a dict
status_filter_dict = status_filter_instance.to_dict()
# create an instance of StatusFilter from a dict
status_filter_form_dict = status_filter.from_dict(status_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


