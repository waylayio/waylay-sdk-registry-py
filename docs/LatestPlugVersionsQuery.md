# LatestPlugVersionsQuery

Plug versions listing query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**TagsFilter**](TagsFilter.md) |  | [optional] 
**type** | [**PlugType**](PlugType.md) |  | [optional] 
**limit** | **float** | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**page** | **float** | The number of pages to skip when returning result to this query. | [optional] 
**include_draft** | **bool** | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**include_deprecated** | **bool** | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 
**deprecated** | **bool** | Filter on the deprecation status of the function. | [optional] 
**draft** | **bool** | Filter on the draft status of the function. | [optional] 
**name_version** | **List[str]** | Filter on exact &#x60;{name}@{version}&#x60; functions. Using this filter implies a &#x60;latest&#x3D;false&#x60; default, returning multiple versions of the same named versions if they are filtered. | [optional] 
**version** | **str** | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**status** | [**List[StatusFilter]**](StatusFilter.md) | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**created_by** | **str** | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**updated_by** | **str** | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**created_before** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**created_after** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**updated_before** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**updated_after** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**name** | **str** | Filter on the name of the function. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md) | Filter on the archive format of the function. | [optional] 
**runtime** | **List[str]** | Filter on the runtime of the function. | [optional] 
**latest** | **bool** | When &#x60;true&#x60;, only the latest version per function name is returned. If set to &#x60;false&#x60;, multiple versions per named function can be returned. Defaults to &#x60;true&#x60;, except when specific versions are selected with the &#x60;nameVersion&#x60; filter. | [optional] 
**show_related** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.latest_plug_versions_query import LatestPlugVersionsQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LatestPlugVersionsQuery from a JSON string
latest_plug_versions_query_instance = LatestPlugVersionsQuery.from_json(json)
# print the JSON string representation of the object
print LatestPlugVersionsQuery.to_json()

# convert the object into a dict
latest_plug_versions_query_dict = latest_plug_versions_query_instance.to_dict()
# create an instance of LatestPlugVersionsQuery from a dict
latest_plug_versions_query_form_dict = latest_plug_versions_query.from_dict(latest_plug_versions_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


