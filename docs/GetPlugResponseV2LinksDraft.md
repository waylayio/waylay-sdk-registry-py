# GetPlugResponseV2LinksDraft

Link to the lastest draft version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** |  | 
**href** | [**HALLinkHref**](HALLinkHref.md) |  | 
**version** | **str** |  | 
**deprecated** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.get_plug_response_v2_links_draft import GetPlugResponseV2LinksDraft

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlugResponseV2LinksDraft from a JSON string
get_plug_response_v2_links_draft_instance = GetPlugResponseV2LinksDraft.from_json(json)
# print the JSON string representation of the object
print GetPlugResponseV2LinksDraft.to_json()

# convert the object into a dict
get_plug_response_v2_links_draft_dict = get_plug_response_v2_links_draft_instance.to_dict()
# create an instance of GetPlugResponseV2LinksDraft from a dict
get_plug_response_v2_links_draft_form_dict = get_plug_response_v2_links_draft.from_dict(get_plug_response_v2_links_draft_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


