# LegacyDebugPlugRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugType**](PlugType.md) |  | [optional] 
**script** | **str** |  | 
**dependencies** | **Dict[str, str]** |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_debug_plug_request import LegacyDebugPlugRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDebugPlugRequest from a JSON string
legacy_debug_plug_request_instance = LegacyDebugPlugRequest.from_json(json)
# print the JSON string representation of the object
print LegacyDebugPlugRequest.to_json()

# convert the object into a dict
legacy_debug_plug_request_dict = legacy_debug_plug_request_instance.to_dict()
# create an instance of LegacyDebugPlugRequest from a dict
legacy_debug_plug_request_form_dict = legacy_debug_plug_request.from_dict(legacy_debug_plug_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


