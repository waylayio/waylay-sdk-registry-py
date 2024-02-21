# DeprecatedDraftFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | Filter on the deprecation status of the function. | [optional] 
**draft** | **bool** | Filter on the draft status of the function. | [optional] 

## Example

```python
from waylay.services.registry.models.deprecated_draft_filter import DeprecatedDraftFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DeprecatedDraftFilter from a JSON string
deprecated_draft_filter_instance = DeprecatedDraftFilter.from_json(json)
# print the JSON string representation of the object
print DeprecatedDraftFilter.to_json()

# convert the object into a dict
deprecated_draft_filter_dict = deprecated_draft_filter_instance.to_dict()
# create an instance of DeprecatedDraftFilter from a dict
deprecated_draft_filter_form_dict = deprecated_draft_filter.from_dict(deprecated_draft_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


