# PlugManifestPatch

Patch attributes to merge into an existing plug manifest.

**Source:** `waylay.services.registry.models.plug_manifest_patch`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugType**](PlugType.md) |  | [optional] 
**interface** | [**PlugInterface**](PlugInterface.md) |  | [optional] 
**metadata** | [**PlugMeta**](PlugMeta.md) |  | [optional] 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.plug_manifest_patch import PlugManifestPatch

plug_manifest_patch = PlugManifestPatch(
    type=..., interface=..., metadata=..., runtime_version=..., runtime=..., deploy=...
)

# Create from JSON
plug_manifest_patch = PlugManifestPatch.from_json(
    '{ "type": ..., "interface": ..., "metadata": ..., "runtimeVersion": ..., "runtime": ..., "deploy": ... }'
)

# Export to dictionary
plug_manifest_patch_dict = plug_manifest_patch.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


