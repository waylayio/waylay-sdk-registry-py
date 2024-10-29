# PlugVersionsResponseV2

Plugs Versions Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**GetPlugResponseV2Embedded**](GetPlugResponseV2Embedded.md) |  | [optional] 
**limit** | **float** | The page size used for this query result. | [optional] 
**count** | **float** | The total count of matching items, from which this result is one page. | 
**page** | **float** | The page number of a paged query result. | [optional] 
**entities** | [**List[PlugResponseV2]**](PlugResponseV2.md) | The specification and deployment status of the queried functions | 

## Example

```python
from waylay.services.registry.models.plug_versions_response_v2 import PlugVersionsResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of PlugVersionsResponseV2 from a JSON string
plug_versions_response_v2_instance = PlugVersionsResponseV2.from_json(json)
# print the JSON string representation of the object
print PlugVersionsResponseV2.to_json()

# convert the object into a dict
plug_versions_response_v2_dict = plug_versions_response_v2_instance.to_dict()
# create an instance of PlugVersionsResponseV2 from a dict
plug_versions_response_v2_form_dict = plug_versions_response_v2.from_dict(plug_versions_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


