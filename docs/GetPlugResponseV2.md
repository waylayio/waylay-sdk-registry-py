# GetPlugResponseV2

Plug Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**PlugWithInvocationResponseV2**](PlugWithInvocationResponseV2.md) |  | 
**links** | [**GetPlugResponseV2Links**](GetPlugResponseV2Links.md) |  | 

## Example

```python
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlugResponseV2 from a JSON string
get_plug_response_v2_instance = GetPlugResponseV2.from_json(json)
# print the JSON string representation of the object
print GetPlugResponseV2.to_json()

# convert the object into a dict
get_plug_response_v2_dict = get_plug_response_v2_instance.to_dict()
# create an instance of GetPlugResponseV2 from a dict
get_plug_response_v2_form_dict = get_plug_response_v2.from_dict(get_plug_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


