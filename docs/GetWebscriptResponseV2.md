# GetWebscriptResponseV2

Webscript Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**GetPlugResponseV2Embedded**](GetPlugResponseV2Embedded.md) |  | [optional] 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 
**links** | [**GetWebscriptResponseV2Links**](GetWebscriptResponseV2Links.md) |  | 

## Example

```python
from waylay.services.registry.models.get_webscript_response_v2 import GetWebscriptResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebscriptResponseV2 from a JSON string
get_webscript_response_v2_instance = GetWebscriptResponseV2.from_json(json)
# print the JSON string representation of the object
print GetWebscriptResponseV2.to_json()

# convert the object into a dict
get_webscript_response_v2_dict = get_webscript_response_v2_instance.to_dict()
# create an instance of GetWebscriptResponseV2 from a dict
get_webscript_response_v2_form_dict = get_webscript_response_v2.from_dict(get_webscript_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


