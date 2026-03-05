# IKFServingManifestPatch

Patch attributes to merge into an existing model manifest.

**Source:** `waylay.services.registry.models.ikf_serving_manifest_patch`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.ikf_serving_manifest_patch import (
    IKFServingManifestPatch,
)

ikf_serving_manifest_patch = IKFServingManifestPatch(
    runtime_version=..., metadata=..., runtime=..., deploy=...
)

# Create from JSON
ikf_serving_manifest_patch = IKFServingManifestPatch.from_json(
    '{ "runtimeVersion": ..., "metadata": ..., "runtime": ..., "deploy": ... }'
)

# Export to dictionary
ikf_serving_manifest_patch_dict = ikf_serving_manifest_patch.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


