# GetInvokableWebscriptQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_draft** | **bool** | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**include_deprecated** | **bool** | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**status** | [**List[StatusFilter]**](StatusFilter.md) | If set, filters on the &#x60;status&#x60; of the webscript. | [optional] [default to ["running","deployed","unhealthy"]]

## Example

```python
from waylay.services.registry.models.get_invokable_webscript_query import GetInvokableWebscriptQuery

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvokableWebscriptQuery from a JSON string
get_invokable_webscript_query_instance = GetInvokableWebscriptQuery.from_json(json)
# print the JSON string representation of the object
print GetInvokableWebscriptQuery.to_json()

# convert the object into a dict
get_invokable_webscript_query_dict = get_invokable_webscript_query_instance.to_dict()
# create an instance of GetInvokableWebscriptQuery from a dict
get_invokable_webscript_query_form_dict = get_invokable_webscript_query.from_dict(get_invokable_webscript_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


