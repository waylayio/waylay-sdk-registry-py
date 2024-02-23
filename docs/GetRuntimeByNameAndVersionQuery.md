# GetRuntimeByNameAndVersionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_deprecated** | **bool** | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.get_runtime_by_name_and_version_query import GetRuntimeByNameAndVersionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetRuntimeByNameAndVersionQuery from a JSON string
get_runtime_by_name_and_version_query_instance = GetRuntimeByNameAndVersionQuery.from_json(json)
# print the JSON string representation of the object
print GetRuntimeByNameAndVersionQuery.to_json()

# convert the object into a dict
get_runtime_by_name_and_version_query_dict = get_runtime_by_name_and_version_query_instance.to_dict()
# create an instance of GetRuntimeByNameAndVersionQuery from a dict
get_runtime_by_name_and_version_query_form_dict = get_runtime_by_name_and_version_query.from_dict(get_runtime_by_name_and_version_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


