# RebuildPlugSyncResponseV2

Plug Rebuild Ignored

**Source:** `waylay.services.registry.models.rebuild_plug_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 
**entity** | [**PlugResponseV2**](PlugResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.rebuild_plug_sync_response_v2 import (
    RebuildPlugSyncResponseV2,
)

rebuild_plug_sync_response_v2 = RebuildPlugSyncResponseV2(
    message=..., causes=..., entity=...
)

# Create from JSON
rebuild_plug_sync_response_v2 = RebuildPlugSyncResponseV2.from_json(
    '{ "message": ..., "causes": ..., "entity": ... }'
)

# Export to dictionary
rebuild_plug_sync_response_v2_dict = rebuild_plug_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


