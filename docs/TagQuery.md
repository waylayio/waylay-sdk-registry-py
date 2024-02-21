# TagQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | If set, filters on the &lt;code&gt;name&lt;/code&gt; of a tag. Supports &lt;code&gt;*&lt;/code&gt; and &lt;code&gt;?&lt;/code&gt; wildcards and is case-insensitive. | [optional] 
**color** | **str** | If set, filters on the &lt;code&gt;color&lt;/code&gt; of a tag. Uses an exact match. | [optional] 

## Example

```python
from waylay.services.registry.models.tag_query import TagQuery

# TODO update the JSON string below
json = "{}"
# create an instance of TagQuery from a JSON string
tag_query_instance = TagQuery.from_json(json)
# print the JSON string representation of the object
print TagQuery.to_json()

# convert the object into a dict
tag_query_dict = tag_query_instance.to_dict()
# create an instance of TagQuery from a dict
tag_query_form_dict = tag_query.from_dict(tag_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


