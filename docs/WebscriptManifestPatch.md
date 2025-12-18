# WebscriptManifestPatch

Patch attributes to merge into an existing webscript manifest.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**private** | **bool** | If &lt;code&gt;true&lt;/code&gt; this webscript will require authentication. | [optional] 
**allow_hmac** | **bool** | If &lt;code&gt;true&lt;/code&gt; this webscript will support authentication with a &lt;em&gt;HMAC&lt;/em&gt; key, available as the &lt;code&gt;secret&lt;/code&gt; attribute of the deployed webscript entity. | [optional] 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | [optional] 
**runtime** | **str** |  | [optional] 
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.webscript_manifest_patch import WebscriptManifestPatch

# TODO update the JSON string below
json = "{}"
# create an instance of WebscriptManifestPatch from a JSON string
webscript_manifest_patch_instance = WebscriptManifestPatch.from_json(json)
# print the JSON string representation of the object
print WebscriptManifestPatch.to_json()

# convert the object into a dict
webscript_manifest_patch_dict = webscript_manifest_patch_instance.to_dict()
# create an instance of WebscriptManifestPatch from a dict
webscript_manifest_patch_form_dict = webscript_manifest_patch.from_dict(webscript_manifest_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


