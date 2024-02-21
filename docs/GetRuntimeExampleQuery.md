# GetRuntimeExampleQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ls** | **bool** | If set to &#x60;true&#x60;, the result will be a listing of the files in the asset, annotated with metadata and validation report from the asset conditions of the functions runtime. | [optional] [default to False]
**include_deprecated** | **bool** | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.get_runtime_example_query import GetRuntimeExampleQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetRuntimeExampleQuery from a JSON string
get_runtime_example_query_instance = GetRuntimeExampleQuery.from_json(json)
# print the JSON string representation of the object
print GetRuntimeExampleQuery.to_json()

# convert the object into a dict
get_runtime_example_query_dict = get_runtime_example_query_instance.to_dict()
# create an instance of GetRuntimeExampleQuery from a dict
get_runtime_example_query_form_dict = get_runtime_example_query.from_dict(get_runtime_example_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


