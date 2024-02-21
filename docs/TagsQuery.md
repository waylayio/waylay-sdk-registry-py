# TagsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**TagsFilter**](TagsFilter.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.tags_query import TagsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TagsQuery from a JSON string
tags_query_instance = TagsQuery.from_json(json)
# print the JSON string representation of the object
print TagsQuery.to_json()

# convert the object into a dict
tags_query_dict = tags_query_instance.to_dict()
# create an instance of TagsQuery from a dict
tags_query_form_dict = tags_query.from_dict(tags_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


