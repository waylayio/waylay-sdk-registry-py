# GetPlugResponseV2LinksPublished

Link to the lastest published version.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**draft** | **bool** |  | 
**href** | **str** |  | 
**version** | **str** |  | 
**deprecated** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.get_plug_response_v2_links_published import GetPlugResponseV2LinksPublished

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlugResponseV2LinksPublished from a JSON string
get_plug_response_v2_links_published_instance = GetPlugResponseV2LinksPublished.from_json(json)
# print the JSON string representation of the object
print GetPlugResponseV2LinksPublished.to_json()

# convert the object into a dict
get_plug_response_v2_links_published_dict = get_plug_response_v2_links_published_instance.to_dict()
# create an instance of GetPlugResponseV2LinksPublished from a dict
get_plug_response_v2_links_published_form_dict = get_plug_response_v2_links_published.from_dict(get_plug_response_v2_links_published_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


