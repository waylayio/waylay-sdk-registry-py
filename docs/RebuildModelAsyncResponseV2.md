# RebuildModelAsyncResponseV2

Model Rebuild Initiated

**Source:** `waylay.services.registry.models.rebuild_model_async_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 


## Example

```python
from waylay.services.registry.models.rebuild_model_async_response_v2 import (
    RebuildModelAsyncResponseV2,
)

rebuild_model_async_response_v2 = RebuildModelAsyncResponseV2(
    message=..., links=..., causes=..., entity=...
)

# Create from JSON
rebuild_model_async_response_v2 = RebuildModelAsyncResponseV2.from_json(
    '{ "message": ..., "_links": ..., "causes": ..., "entity": ... }'
)

# Export to dictionary
rebuild_model_async_response_v2_dict = rebuild_model_async_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


