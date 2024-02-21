# LegacyFunctionMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_function_meta import LegacyFunctionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyFunctionMeta from a JSON string
legacy_function_meta_instance = LegacyFunctionMeta.from_json(json)
# print the JSON string representation of the object
print LegacyFunctionMeta.to_json()

# convert the object into a dict
legacy_function_meta_dict = legacy_function_meta_instance.to_dict()
# create an instance of LegacyFunctionMeta from a dict
legacy_function_meta_form_dict = legacy_function_meta.from_dict(legacy_function_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


