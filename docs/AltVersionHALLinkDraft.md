# AltVersionHALLinkDraft

Link to the lastest draft version.

**Source:** `waylay.services.registry.models.alt_version_hal_link_draft`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** |  | 
**href** | [**IHALLinkHref**](IHALLinkHref.md) |  | 
**version** | **str** |  | 
**deprecated** | **bool** |  | 


## Example

```python
from waylay.services.registry.models.alt_version_hal_link_draft import (
    AltVersionHALLinkDraft,
)

alt_version_hal_link_draft = AltVersionHALLinkDraft(
    draft=..., href=..., version=..., deprecated=...
)

# Create from JSON
alt_version_hal_link_draft = AltVersionHALLinkDraft.from_json(
    '{ "draft": ..., "href": ..., "version": ..., "deprecated": ... }'
)

# Export to dictionary
alt_version_hal_link_draft_dict = alt_version_hal_link_draft.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


