# GetPlugResponseV2Links

HAL links to related jobs and plugs

**Source:** `waylay.services.registry.models.get_plug_response_v2_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**content** | [**IHALLink**](IHALLink.md) |  | [optional] 
**draft** | [**AltVersionHALLinkDraft**](AltVersionHALLinkDraft.md) |  | [optional] 
**published** | [**AltVersionHALLinkPublished**](AltVersionHALLinkPublished.md) |  | [optional] 
**jobs** | [**IHALLink**](IHALLink.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.get_plug_response_v2_links import (
    GetPlugResponseV2Links,
)

get_plug_response_v2_links = GetPlugResponseV2Links(
    job=..., content=..., draft=..., published=..., jobs=...
)

# Create from JSON
get_plug_response_v2_links = GetPlugResponseV2Links.from_json(
    '{ "job": ..., "content": ..., "draft": ..., "published": ..., "jobs": ... }'
)

# Export to dictionary
get_plug_response_v2_links_dict = get_plug_response_v2_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


