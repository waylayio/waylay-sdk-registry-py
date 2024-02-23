# RuntimeQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**latest** | [**LatestVersionLevel**](LatestVersionLevel.md) |  | [optional] 
**include_deprecated** | **bool** | If set to &#x60;true&#x60;, deprecated runtimes will be included in the query. | [optional] [default to False]
**name** | **str** | If set, filters on the &lt;code&gt;name&lt;/code&gt; of a runtime. Supports &lt;code&gt;*&lt;/code&gt; and &lt;code&gt;?&lt;/code&gt; wildcards and is case-insensitive. | [optional] 
**function_type** | [**List[FunctionType]**](FunctionType.md) | If set, filters on the &lt;code&gt;functionType&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 
**archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md) | If set, filters on the &lt;code&gt;archiveFormat&lt;/code&gt; of a runtime. Uses an exact match. | [optional] 

## Example

```python
from waylay.services.registry.models.runtime_query import RuntimeQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeQuery from a JSON string
runtime_query_instance = RuntimeQuery.from_json(json)
# print the JSON string representation of the object
print RuntimeQuery.to_json()

# convert the object into a dict
runtime_query_dict = runtime_query_instance.to_dict()
# create an instance of RuntimeQuery from a dict
runtime_query_form_dict = runtime_query.from_dict(runtime_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


