# WebscriptManifestPatch

Patch attributes to merge into an existing webscript manifest.

**Source:** `waylay.services.registry.models.webscript_manifest_patch`




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
from waylay.services.registry.models.webscript_manifest_patch import (
    WebscriptManifestPatch,
)

webscript_manifest_patch = WebscriptManifestPatch(
    private=...,
    allow_hmac=...,
    runtime_version=...,
    metadata=...,
    runtime=...,
    deploy=...,
)

# Create from JSON
webscript_manifest_patch = WebscriptManifestPatch.from_json(
    '{ "private": ..., "allowHmac": ..., "runtimeVersion": ..., "metadata": ..., "runtime": ..., "deploy": ... }'
)

# Export to dictionary
webscript_manifest_patch_dict = webscript_manifest_patch.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


