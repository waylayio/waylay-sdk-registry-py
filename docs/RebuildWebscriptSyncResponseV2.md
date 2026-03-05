# RebuildWebscriptSyncResponseV2

Webscript Rebuild Ignored

**Source:** `waylay.services.registry.models.rebuild_webscript_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.rebuild_webscript_sync_response_v2 import (
    RebuildWebscriptSyncResponseV2,
)

rebuild_webscript_sync_response_v2 = RebuildWebscriptSyncResponseV2(
    message=..., causes=..., entity=...
)

# Create from JSON
rebuild_webscript_sync_response_v2 = RebuildWebscriptSyncResponseV2.from_json(
    '{ "message": ..., "causes": ..., "entity": ... }'
)

# Export to dictionary
rebuild_webscript_sync_response_v2_dict = rebuild_webscript_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


