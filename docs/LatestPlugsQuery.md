# LatestPlugsQuery

Latest plug versions listing query with latest links. A request that only uses these query parameters will include links to the _latest_ draft/published versions of the plug.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugType**](PlugType.md) |  | [optional] 
**limit** | **float** | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**page** | **float** | The number of pages to skip when returning result to this query. | [optional] 
**include_draft** | **bool** | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**include_deprecated** | **bool** | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**name** | **str** | Filter on the name of the function. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md) | Filter on the archive format of the function. | [optional] 
**runtime** | **List[str]** | Filter on the runtime of the function. | [optional] 

## Example

```python
from waylay.services.registry.models.latest_plugs_query import LatestPlugsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LatestPlugsQuery from a JSON string
latest_plugs_query_instance = LatestPlugsQuery.from_json(json)
# print the JSON string representation of the object
print LatestPlugsQuery.to_json()

# convert the object into a dict
latest_plugs_query_dict = latest_plugs_query_instance.to_dict()
# create an instance of LatestPlugsQuery from a dict
latest_plugs_query_form_dict = latest_plugs_query.from_dict(latest_plugs_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


