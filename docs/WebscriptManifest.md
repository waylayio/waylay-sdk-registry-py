# WebscriptManifest


**Source:** `waylay.services.registry.models.webscript_manifest`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 
**name** | **str** | The logical name for the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**runtime** | **str** |  | 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | 
**protected** | **bool** | Indicates whether the function&#39;s script and other assets should be protected. | [optional] 
**tags** | [**List[TagOrTagReference]**](TagOrTagReference.md) | Tags associated with this entity. | [optional] 
**private** | **bool** | If &lt;code&gt;true&lt;/code&gt; this webscript will require authentication. | 
**allow_hmac** | **bool** | If &lt;code&gt;true&lt;/code&gt; this webscript will support authentication with a &lt;em&gt;HMAC&lt;/em&gt; key, available as the &lt;code&gt;secret&lt;/code&gt; attribute of the deployed webscript entity. | 


## Example

```python
from waylay.services.registry.models.webscript_manifest import WebscriptManifest

webscript_manifest = WebscriptManifest(
    deploy=...,
    name=...,
    version=...,
    runtime=...,
    runtime_version=...,
    metadata=...,
    protected=...,
    tags=...,
    private=...,
    allow_hmac=...,
)

# Create from JSON
webscript_manifest = WebscriptManifest.from_json(
    '{ "deploy": ..., "name": ..., "version": ..., "runtime": ..., "runtimeVersion": ..., "metadata": ..., "protected": ..., "tags": ..., "private": ..., "allowHmac": ... }'
)

# Export to dictionary
webscript_manifest_dict = webscript_manifest.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


