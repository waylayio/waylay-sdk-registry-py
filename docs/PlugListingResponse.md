# PlugListingResponse

Successful Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plugs** | [**List[PlugResponse]**](PlugResponse.md) |  | 

## Example

```python
from waylay.services.registry.models.plug_listing_response import PlugListingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlugListingResponse from a JSON string
plug_listing_response_instance = PlugListingResponse.from_json(json)
# print the JSON string representation of the object
print PlugListingResponse.to_json()

# convert the object into a dict
plug_listing_response_dict = plug_listing_response_instance.to_dict()
# create an instance of PlugListingResponse from a dict
plug_listing_response_form_dict = plug_listing_response.from_dict(plug_listing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


