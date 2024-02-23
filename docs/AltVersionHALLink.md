# AltVersionHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | [**GetPlugResponseV2LinksDraft**](GetPlugResponseV2LinksDraft.md) |  | [optional] 
**published** | [**GetPlugResponseV2LinksPublished**](GetPlugResponseV2LinksPublished.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.alt_version_hal_link import AltVersionHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of AltVersionHALLink from a JSON string
alt_version_hal_link_instance = AltVersionHALLink.from_json(json)
# print the JSON string representation of the object
print AltVersionHALLink.to_json()

# convert the object into a dict
alt_version_hal_link_dict = alt_version_hal_link_instance.to_dict()
# create an instance of AltVersionHALLink from a dict
alt_version_hal_link_form_dict = alt_version_hal_link.from_dict(alt_version_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


