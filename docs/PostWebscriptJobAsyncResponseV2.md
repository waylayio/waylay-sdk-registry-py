# PostWebscriptJobAsyncResponseV2

Webscript Deployment Initiated

**Source:** `waylay.services.registry.models.post_webscript_job_async_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.post_webscript_job_async_response_v2 import (
    PostWebscriptJobAsyncResponseV2,
)

post_webscript_job_async_response_v2 = PostWebscriptJobAsyncResponseV2(
    message=..., links=..., entity=...
)

# Create from JSON
post_webscript_job_async_response_v2 = PostWebscriptJobAsyncResponseV2.from_json(
    '{ "message": ..., "_links": ..., "entity": ... }'
)

# Export to dictionary
post_webscript_job_async_response_v2_dict = (
    post_webscript_job_async_response_v2.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


