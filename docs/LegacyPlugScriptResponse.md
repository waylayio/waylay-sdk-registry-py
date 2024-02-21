# LegacyPlugScriptResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**type** | [**PlugType**](PlugType.md) |  | 
**script** | **str** |  | 
**metadata** | [**LegacyPlugScriptMeta**](LegacyPlugScriptMeta.md) |  | 
**dependencies** | **object** |  | 

## Example

```python
from waylay.services.registry.models.legacy_plug_script_response import LegacyPlugScriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugScriptResponse from a JSON string
legacy_plug_script_response_instance = LegacyPlugScriptResponse.from_json(json)
# print the JSON string representation of the object
print LegacyPlugScriptResponse.to_json()

# convert the object into a dict
legacy_plug_script_response_dict = legacy_plug_script_response_instance.to_dict()
# create an instance of LegacyPlugScriptResponse from a dict
legacy_plug_script_response_form_dict = legacy_plug_script_response.from_dict(legacy_plug_script_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


