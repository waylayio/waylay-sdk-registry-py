# RuntimeVersionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**latest** | [**LatestVersionLevel**](LatestVersionLevel.md) |  | [optional] 
**include_deprecated** | **bool** | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to False]

## Example

```python
from waylay.services.registry.models.runtime_version_query import RuntimeVersionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersionQuery from a JSON string
runtime_version_query_instance = RuntimeVersionQuery.from_json(json)
# print the JSON string representation of the object
print RuntimeVersionQuery.to_json()

# convert the object into a dict
runtime_version_query_dict = runtime_version_query_instance.to_dict()
# create an instance of RuntimeVersionQuery from a dict
runtime_version_query_form_dict = runtime_version_query.from_dict(runtime_version_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


