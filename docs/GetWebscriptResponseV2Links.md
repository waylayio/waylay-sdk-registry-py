# GetWebscriptResponseV2Links

HAL links to related actions.

**Source:** `waylay.services.registry.models.get_webscript_response_v2_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**content** | [**IHALLink**](IHALLink.md) |  | [optional] 
**draft** | [**AltVersionHALLinkDraft**](AltVersionHALLinkDraft.md) |  | [optional] 
**published** | [**AltVersionHALLinkPublished**](AltVersionHALLinkPublished.md) |  | [optional] 
**jobs** | [**IHALLink**](IHALLink.md) |  | [optional] 
**invoke** | [**IHALLink**](IHALLink.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.get_webscript_response_v2_links import (
    GetWebscriptResponseV2Links,
)

get_webscript_response_v2_links = GetWebscriptResponseV2Links(
    job=..., content=..., draft=..., published=..., jobs=..., invoke=...
)

# Create from JSON
get_webscript_response_v2_links = GetWebscriptResponseV2Links.from_json(
    '{ "job": ..., "content": ..., "draft": ..., "published": ..., "jobs": ..., "invoke": ... }'
)

# Export to dictionary
get_webscript_response_v2_links_dict = get_webscript_response_v2_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


