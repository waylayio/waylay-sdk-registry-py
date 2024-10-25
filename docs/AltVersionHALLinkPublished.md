# AltVersionHALLinkPublished

Link to the lastest published version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** |  | 
**href** | [**HALLinkHref**](HALLinkHref.md) |  | 
**version** | **str** |  | 
**deprecated** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.alt_version_hal_link_published import AltVersionHALLinkPublished

# TODO update the JSON string below
json = "{}"
# create an instance of AltVersionHALLinkPublished from a JSON string
alt_version_hal_link_published_instance = AltVersionHALLinkPublished.from_json(json)
# print the JSON string representation of the object
print AltVersionHALLinkPublished.to_json()

# convert the object into a dict
alt_version_hal_link_published_dict = alt_version_hal_link_published_instance.to_dict()
# create an instance of AltVersionHALLinkPublished from a dict
alt_version_hal_link_published_form_dict = alt_version_hal_link_published.from_dict(alt_version_hal_link_published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


