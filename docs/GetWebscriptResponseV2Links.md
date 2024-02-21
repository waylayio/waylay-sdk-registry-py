# GetWebscriptResponseV2Links

HAL links to related actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke** | [**HALLink**](HALLink.md) |  | [optional] 
**jobs** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.get_webscript_response_v2_links import GetWebscriptResponseV2Links

# TODO update the JSON string below
json = "{}"
# create an instance of GetWebscriptResponseV2Links from a JSON string
get_webscript_response_v2_links_instance = GetWebscriptResponseV2Links.from_json(json)
# print the JSON string representation of the object
print GetWebscriptResponseV2Links.to_json()

# convert the object into a dict
get_webscript_response_v2_links_dict = get_webscript_response_v2_links_instance.to_dict()
# create an instance of GetWebscriptResponseV2Links from a dict
get_webscript_response_v2_links_form_dict = get_webscript_response_v2_links.from_dict(get_webscript_response_v2_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


