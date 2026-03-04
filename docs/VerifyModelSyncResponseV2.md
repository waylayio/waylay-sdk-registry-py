# VerifyModelSyncResponseV2

Model Health Verified

**Source:** `waylay.services.registry.models.verify_model_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 
**result** | [**VerifyResult**](VerifyResult.md) |  | 


## Example

```python
from waylay.services.registry.models.verify_model_sync_response_v2 import (
    VerifyModelSyncResponseV2,
)

verify_model_sync_response_v2 = VerifyModelSyncResponseV2(
    message=..., entity=..., result=...
)

# Create from JSON
verify_model_sync_response_v2 = VerifyModelSyncResponseV2.from_json(
    '{ "message": ..., "entity": ..., "result": ... }'
)

# Export to dictionary
verify_model_sync_response_v2_dict = verify_model_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


