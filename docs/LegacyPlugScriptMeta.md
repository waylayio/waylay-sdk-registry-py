# LegacyPlugScriptMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**supported_states** | **List[str]** |  | 
**raw_data** | [**List[LegacyPlugScriptMetaRawDataInner]**](LegacyPlugScriptMetaRawDataInner.md) |  | 
**required_properties** | [**List[LegacyRequiredPropertiesInner]**](LegacyRequiredPropertiesInner.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_plug_script_meta import LegacyPlugScriptMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugScriptMeta from a JSON string
legacy_plug_script_meta_instance = LegacyPlugScriptMeta.from_json(json)
# print the JSON string representation of the object
print LegacyPlugScriptMeta.to_json()

# convert the object into a dict
legacy_plug_script_meta_dict = legacy_plug_script_meta_instance.to_dict()
# create an instance of LegacyPlugScriptMeta from a dict
legacy_plug_script_meta_form_dict = legacy_plug_script_meta.from_dict(legacy_plug_script_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


