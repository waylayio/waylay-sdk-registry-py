# GetRuntimeVersionsQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**latest** | [**LatestVersionLevel**](LatestVersionLevel.md) |  | [optional] 
**include_deprecated** | **bool** | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to False]
**function_type** | [**List[FunctionType]**](FunctionType.md) | If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md) | If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 

## Example

```python
from waylay.services.registry.models.get_runtime_versions_query import GetRuntimeVersionsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetRuntimeVersionsQuery from a JSON string
get_runtime_versions_query_instance = GetRuntimeVersionsQuery.from_json(json)
# print the JSON string representation of the object
print GetRuntimeVersionsQuery.to_json()

# convert the object into a dict
get_runtime_versions_query_dict = get_runtime_versions_query_instance.to_dict()
# create an instance of GetRuntimeVersionsQuery from a dict
get_runtime_versions_query_form_dict = get_runtime_versions_query.from_dict(get_runtime_versions_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


