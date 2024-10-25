# AltVersionHALLinkDraft

Link to the lastest draft version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** |  | 
**href** | [**HALLinkHref**](HALLinkHref.md) |  | 
**version** | **str** |  | 
**deprecated** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.alt_version_hal_link_draft import AltVersionHALLinkDraft

# TODO update the JSON string below
json = "{}"
# create an instance of AltVersionHALLinkDraft from a JSON string
alt_version_hal_link_draft_instance = AltVersionHALLinkDraft.from_json(json)
# print the JSON string representation of the object
print AltVersionHALLinkDraft.to_json()

# convert the object into a dict
alt_version_hal_link_draft_dict = alt_version_hal_link_draft_instance.to_dict()
# create an instance of AltVersionHALLinkDraft from a dict
alt_version_hal_link_draft_form_dict = alt_version_hal_link_draft.from_dict(alt_version_hal_link_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


