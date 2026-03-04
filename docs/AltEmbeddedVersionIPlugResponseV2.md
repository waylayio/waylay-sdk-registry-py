# AltEmbeddedVersionIPlugResponseV2

Embedded representations of the _latest_ draft/published versions.

**Source:** `waylay.services.registry.models.alt_embedded_version_i_plug_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | [**PlugResponseV2**](PlugResponseV2.md) |  | [optional] 
**published** | [**PlugResponseV2**](PlugResponseV2.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.alt_embedded_version_i_plug_response_v2 import (
    AltEmbeddedVersionIPlugResponseV2,
)

alt_embedded_version_i_plug_response_v2 = AltEmbeddedVersionIPlugResponseV2(
    draft=..., published=...
)

# Create from JSON
alt_embedded_version_i_plug_response_v2 = AltEmbeddedVersionIPlugResponseV2.from_json(
    '{ "draft": ..., "published": ... }'
)

# Export to dictionary
alt_embedded_version_i_plug_response_v2_dict = (
    alt_embedded_version_i_plug_response_v2.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


