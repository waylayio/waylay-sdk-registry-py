# GetPlugResponseV2Links

HAL links to related jobs and plugs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**content** | [**HALLink**](HALLink.md) |  | [optional] 
**draft** | [**AltVersionHALLinkDraft**](AltVersionHALLinkDraft.md) |  | [optional] 
**published** | [**AltVersionHALLinkPublished**](AltVersionHALLinkPublished.md) |  | [optional] 
**jobs** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.get_plug_response_v2_links import GetPlugResponseV2Links

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlugResponseV2Links from a JSON string
get_plug_response_v2_links_instance = GetPlugResponseV2Links.from_json(json)
# print the JSON string representation of the object
print GetPlugResponseV2Links.to_json()

# convert the object into a dict
get_plug_response_v2_links_dict = get_plug_response_v2_links_instance.to_dict()
# create an instance of GetPlugResponseV2Links from a dict
get_plug_response_v2_links_form_dict = get_plug_response_v2_links.from_dict(get_plug_response_v2_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


