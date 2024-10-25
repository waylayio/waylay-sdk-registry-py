# PlugManifest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 
**name** | **str** | The logical name for the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**runtime** | **str** |  | 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**PlugMeta**](PlugMeta.md) |  | 
**protected** | **bool** | Indicates whether the function&#39;s script and other assets should be protected. | [optional] 
**tags** | [**List[TagOrTagReference]**](TagOrTagReference.md) | Tags associated with this entity. | [optional] 
**type** | [**PlugType**](PlugType.md) |  | 
**interface** | [**PlugInterface**](PlugInterface.md) |  | 

## Example

```python
from waylay.services.registry.models.plug_manifest import PlugManifest

# TODO update the JSON string below
json = "{}"
# create an instance of PlugManifest from a JSON string
plug_manifest_instance = PlugManifest.from_json(json)
# print the JSON string representation of the object
print PlugManifest.to_json()

# convert the object into a dict
plug_manifest_dict = plug_manifest_instance.to_dict()
# create an instance of PlugManifest from a dict
plug_manifest_form_dict = plug_manifest.from_dict(plug_manifest_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


