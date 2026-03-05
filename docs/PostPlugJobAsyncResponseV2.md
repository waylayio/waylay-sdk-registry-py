# PostPlugJobAsyncResponseV2

Plug Deployment Initiated

**Source:** `waylay.services.registry.models.post_plug_job_async_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**entity** | [**PlugResponseV2**](PlugResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.post_plug_job_async_response_v2 import (
    PostPlugJobAsyncResponseV2,
)

post_plug_job_async_response_v2 = PostPlugJobAsyncResponseV2(
    message=..., links=..., entity=...
)

# Create from JSON
post_plug_job_async_response_v2 = PostPlugJobAsyncResponseV2.from_json(
    '{ "message": ..., "_links": ..., "entity": ... }'
)

# Export to dictionary
post_plug_job_async_response_v2_dict = post_plug_job_async_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


