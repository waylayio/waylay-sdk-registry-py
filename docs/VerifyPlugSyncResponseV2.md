# VerifyPlugSyncResponseV2

Plug Health Verified

**Source:** `waylay.services.registry.models.verify_plug_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**PlugResponseV2**](PlugResponseV2.md) |  | 
**result** | [**VerifyResult**](VerifyResult.md) |  | 


## Example

```python
from waylay.services.registry.models.verify_plug_sync_response_v2 import (
    VerifyPlugSyncResponseV2,
)

verify_plug_sync_response_v2 = VerifyPlugSyncResponseV2(
    message=..., entity=..., result=...
)

# Create from JSON
verify_plug_sync_response_v2 = VerifyPlugSyncResponseV2.from_json(
    '{ "message": ..., "entity": ..., "result": ... }'
)

# Export to dictionary
verify_plug_sync_response_v2_dict = verify_plug_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


