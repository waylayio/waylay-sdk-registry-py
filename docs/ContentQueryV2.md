# ContentQueryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ls** | **bool** | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]

## Example

```python
from waylay.services.registry.models.content_query_v2 import ContentQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of ContentQueryV2 from a JSON string
content_query_v2_instance = ContentQueryV2.from_json(json)
# print the JSON string representation of the object
print ContentQueryV2.to_json()

# convert the object into a dict
content_query_v2_dict = content_query_v2_instance.to_dict()
# create an instance of ContentQueryV2 from a dict
content_query_v2_form_dict = content_query_v2.from_dict(content_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


