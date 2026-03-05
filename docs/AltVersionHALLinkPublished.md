# AltVersionHALLinkPublished

Link to the lastest published version.

**Source:** `waylay.services.registry.models.alt_version_hal_link_published`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** |  | 
**href** | [**IHALLinkHref**](IHALLinkHref.md) |  | 
**version** | **str** |  | 
**deprecated** | **bool** |  | 


## Example

```python
from waylay.services.registry.models.alt_version_hal_link_published import (
    AltVersionHALLinkPublished,
)

alt_version_hal_link_published = AltVersionHALLinkPublished(
    draft=..., href=..., version=..., deprecated=...
)

# Create from JSON
alt_version_hal_link_published = AltVersionHALLinkPublished.from_json(
    '{ "draft": ..., "href": ..., "version": ..., "deprecated": ... }'
)

# Export to dictionary
alt_version_hal_link_published_dict = alt_version_hal_link_published.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


