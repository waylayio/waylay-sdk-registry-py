# PostModelJobSyncResponseV2

Model Deployed

**Source:** `waylay.services.registry.models.post_model_job_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.post_model_job_sync_response_v2 import (
    PostModelJobSyncResponseV2,
)

post_model_job_sync_response_v2 = PostModelJobSyncResponseV2(message=..., entity=...)

# Create from JSON
post_model_job_sync_response_v2 = PostModelJobSyncResponseV2.from_json(
    '{ "message": ..., "entity": ... }'
)

# Export to dictionary
post_model_job_sync_response_v2_dict = post_model_job_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


