# PagingQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**page** | **float** | The number of pages to skip when returning result to this query. | [optional] 

## Example

```python
from waylay.services.registry.models.paging_query import PagingQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PagingQuery from a JSON string
paging_query_instance = PagingQuery.from_json(json)
# print the JSON string representation of the object
print PagingQuery.to_json()

# convert the object into a dict
paging_query_dict = paging_query_instance.to_dict()
# create an instance of PagingQuery from a dict
paging_query_form_dict = paging_query.from_dict(paging_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


