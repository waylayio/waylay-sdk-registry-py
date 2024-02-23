# WithPaging


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The page size used for this query result. | [optional] 
**count** | **float** | The total count of matching items, from which this result is one page. | 
**page** | **float** | The page number of a paged query result. | [optional] 

## Example

```python
from waylay.services.registry.models.with_paging import WithPaging

# TODO update the JSON string below
json = "{}"
# create an instance of WithPaging from a JSON string
with_paging_instance = WithPaging.from_json(json)
# print the JSON string representation of the object
print WithPaging.to_json()

# convert the object into a dict
with_paging_dict = with_paging_instance.to_dict()
# create an instance of WithPaging from a dict
with_paging_form_dict = with_paging.from_dict(with_paging_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


