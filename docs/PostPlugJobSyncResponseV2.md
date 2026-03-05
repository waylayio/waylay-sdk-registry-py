# PostPlugJobSyncResponseV2

Plug Deployed

**Source:** `waylay.services.registry.models.post_plug_job_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**PlugResponseV2**](PlugResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.post_plug_job_sync_response_v2 import (
    PostPlugJobSyncResponseV2,
)

post_plug_job_sync_response_v2 = PostPlugJobSyncResponseV2(message=..., entity=...)

# Create from JSON
post_plug_job_sync_response_v2 = PostPlugJobSyncResponseV2.from_json(
    '{ "message": ..., "entity": ... }'
)

# Export to dictionary
post_plug_job_sync_response_v2_dict = post_plug_job_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


