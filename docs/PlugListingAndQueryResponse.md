# PlugListingAndQueryResponse

Successful Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** | The total count of matching items, from which this result is one page. | [optional] 
**limit** | **float** | The page size used for this query result. | [optional] 
**page** | **float** | The page number of a paged query result. | [optional] 
**plugs** | [**List[PlugResponse]**](PlugResponse.md) |  | 

## Example

```python
from waylay.services.registry.models.plug_listing_and_query_response import PlugListingAndQueryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlugListingAndQueryResponse from a JSON string
plug_listing_and_query_response_instance = PlugListingAndQueryResponse.from_json(json)
# print the JSON string representation of the object
print PlugListingAndQueryResponse.to_json()

# convert the object into a dict
plug_listing_and_query_response_dict = plug_listing_and_query_response_instance.to_dict()
# create an instance of PlugListingAndQueryResponse from a dict
plug_listing_and_query_response_form_dict = plug_listing_and_query_response.from_dict(plug_listing_and_query_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


