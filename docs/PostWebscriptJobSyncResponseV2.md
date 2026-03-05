# PostWebscriptJobSyncResponseV2

Webscript Deployed

**Source:** `waylay.services.registry.models.post_webscript_job_sync_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import (
    PostWebscriptJobSyncResponseV2,
)

post_webscript_job_sync_response_v2 = PostWebscriptJobSyncResponseV2(
    message=..., entity=...
)

# Create from JSON
post_webscript_job_sync_response_v2 = PostWebscriptJobSyncResponseV2.from_json(
    '{ "message": ..., "entity": ... }'
)

# Export to dictionary
post_webscript_job_sync_response_v2_dict = post_webscript_job_sync_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


