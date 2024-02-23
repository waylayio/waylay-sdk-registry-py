# WebscriptManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 
**name** | **str** | The logical name for the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**runtime** | **str** |  | 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | 
**private** | **bool** | If &lt;code&gt;true&lt;/code&gt; this webscript will require authentication. | 
**allow_hmac** | **bool** | If &lt;code&gt;true&lt;/code&gt; this webscript will support authentication with a &lt;em&gt;HMAC&lt;/em&gt; key, available as the &lt;code&gt;secret&lt;/code&gt; attribute of the deployed webscript entity. | 

## Example

```python
from waylay.services.registry.models.webscript_manifest import WebscriptManifest

# TODO update the JSON string below
json = "{}"
# create an instance of WebscriptManifest from a JSON string
webscript_manifest_instance = WebscriptManifest.from_json(json)
# print the JSON string representation of the object
print WebscriptManifest.to_json()

# convert the object into a dict
webscript_manifest_dict = webscript_manifest_instance.to_dict()
# create an instance of WebscriptManifest from a dict
webscript_manifest_form_dict = webscript_manifest.from_dict(webscript_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


