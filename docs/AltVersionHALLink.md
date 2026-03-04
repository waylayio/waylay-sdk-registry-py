# AltVersionHALLink


**Source:** `waylay.services.registry.models.alt_version_hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | [**AltVersionHALLinkDraft**](AltVersionHALLinkDraft.md) |  | [optional] 
**published** | [**AltVersionHALLinkPublished**](AltVersionHALLinkPublished.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.alt_version_hal_link import AltVersionHALLink

alt_version_hal_link = AltVersionHALLink(draft=..., published=...)

# Create from JSON
alt_version_hal_link = AltVersionHALLink.from_json('{ "draft": ..., "published": ... }')

# Export to dictionary
alt_version_hal_link_dict = alt_version_hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


