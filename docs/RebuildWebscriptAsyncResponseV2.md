# RebuildWebscriptAsyncResponseV2

Webscript Rebuild Initiated

**Source:** `waylay.services.registry.models.rebuild_webscript_async_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.rebuild_webscript_async_response_v2 import (
    RebuildWebscriptAsyncResponseV2,
)

rebuild_webscript_async_response_v2 = RebuildWebscriptAsyncResponseV2(
    message=..., links=..., causes=..., entity=...
)

# Create from JSON
rebuild_webscript_async_response_v2 = RebuildWebscriptAsyncResponseV2.from_json(
    '{ "message": ..., "_links": ..., "causes": ..., "entity": ... }'
)

# Export to dictionary
rebuild_webscript_async_response_v2_dict = rebuild_webscript_async_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


