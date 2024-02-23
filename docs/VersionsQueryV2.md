# VersionsQueryV2

Function versions paged query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**page** | **float** | The number of pages to skip when returning result to this query. | [optional] 
**endpoint** | **str** | Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**image_name** | **str** | Filter on the container image name. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**storage_location** | **str** | Filter on the storageLocation. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
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

## Example

```python
from waylay.services.registry.models.versions_query_v2 import VersionsQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of VersionsQueryV2 from a JSON string
versions_query_v2_instance = VersionsQueryV2.from_json(json)
# print the JSON string representation of the object
print VersionsQueryV2.to_json()

# convert the object into a dict
versions_query_v2_dict = versions_query_v2_instance.to_dict()
# create an instance of VersionsQueryV2 from a dict
versions_query_v2_form_dict = versions_query_v2.from_dict(versions_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


