# KFServingManifestPatch

Patch attributes to merge into an existing model manifest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.kf_serving_manifest_patch import KFServingManifestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of KFServingManifestPatch from a JSON string
kf_serving_manifest_patch_instance = KFServingManifestPatch.from_json(json)
# print the JSON string representation of the object
print KFServingManifestPatch.to_json()

# convert the object into a dict
kf_serving_manifest_patch_dict = kf_serving_manifest_patch_instance.to_dict()
# create an instance of KFServingManifestPatch from a dict
kf_serving_manifest_patch_form_dict = kf_serving_manifest_patch.from_dict(kf_serving_manifest_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


