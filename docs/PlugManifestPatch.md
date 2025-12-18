# PlugManifestPatch

Patch attributes to merge into an existing plug manifest.

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

# TODO update the JSON string below
json = "{}"
# create an instance of PlugManifestPatch from a JSON string
plug_manifest_patch_instance = PlugManifestPatch.from_json(json)
# print the JSON string representation of the object
print PlugManifestPatch.to_json()

# convert the object into a dict
plug_manifest_patch_dict = plug_manifest_patch_instance.to_dict()
# create an instance of PlugManifestPatch from a dict
plug_manifest_patch_form_dict = plug_manifest_patch.from_dict(plug_manifest_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


