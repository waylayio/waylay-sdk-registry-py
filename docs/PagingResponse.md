# PagingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **float** | The total count of matching items, from which this result is one page. | [optional] 
**limit** | **float** | The page size used for this query result. | [optional] 
**page** | **float** | The page number of a paged query result. | [optional] 

## Example

```python
from waylay.services.registry.models.paging_response import PagingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagingResponse from a JSON string
paging_response_instance = PagingResponse.from_json(json)
# print the JSON string representation of the object
print PagingResponse.to_json()

# convert the object into a dict
paging_response_dict = paging_response_instance.to_dict()
# create an instance of PagingResponse from a dict
paging_response_form_dict = paging_response.from_dict(paging_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


