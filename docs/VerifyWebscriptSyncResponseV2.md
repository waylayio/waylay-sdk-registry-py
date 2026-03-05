# VerifyWebscriptSyncResponseV2

Webscript Health Verified

**Source:** `waylay.services.registry.models.verify_webscript_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 
**result** | [**VerifyResult**](VerifyResult.md) |  | 


## Example

```python
from waylay.services.registry.models.verify_webscript_sync_response_v2 import (
    VerifyWebscriptSyncResponseV2,
)

verify_webscript_sync_response_v2 = VerifyWebscriptSyncResponseV2(
    message=..., entity=..., result=...
)

# Create from JSON
verify_webscript_sync_response_v2 = VerifyWebscriptSyncResponseV2.from_json(
    '{ "message": ..., "entity": ..., "result": ... }'
)

# Export to dictionary
verify_webscript_sync_response_v2_dict = verify_webscript_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


