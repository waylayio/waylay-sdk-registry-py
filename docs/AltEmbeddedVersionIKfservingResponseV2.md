# AltEmbeddedVersionIKfservingResponseV2

Embedded representations of the _latest_ draft/published versions.

**Source:** `waylay.services.registry.models.alt_embedded_version_i_kfserving_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | [optional] 
**published** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.alt_embedded_version_i_kfserving_response_v2 import (
    AltEmbeddedVersionIKfservingResponseV2,
)

alt_embedded_version_i_kfserving_response_v2 = AltEmbeddedVersionIKfservingResponseV2(
    draft=..., published=...
)

# Create from JSON
alt_embedded_version_i_kfserving_response_v2 = (
    AltEmbeddedVersionIKfservingResponseV2.from_json(
        '{ "draft": ..., "published": ... }'
    )
)

# Export to dictionary
alt_embedded_version_i_kfserving_response_v2_dict = (
    alt_embedded_version_i_kfserving_response_v2.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


