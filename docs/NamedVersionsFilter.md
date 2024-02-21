# NamedVersionsFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name_version** | **List[str]** | Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 

## Example

```python
from waylay.services.registry.models.named_versions_filter import NamedVersionsFilter

# TODO update the JSON string below
json = "{}"
# create an instance of NamedVersionsFilter from a JSON string
named_versions_filter_instance = NamedVersionsFilter.from_json(json)
# print the JSON string representation of the object
print NamedVersionsFilter.to_json()

# convert the object into a dict
named_versions_filter_dict = named_versions_filter_instance.to_dict()
# create an instance of NamedVersionsFilter from a dict
named_versions_filter_form_dict = named_versions_filter.from_dict(named_versions_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


