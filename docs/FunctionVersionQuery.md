# FunctionVersionQuery

Filter on function attributes that can change across function versions. When these query parameters are used, the query is considered a _function version_ listing and no HAL links to latest (_draft_, _published_) versions are included.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | Filter on the version of the function (case-sensitive, supports wildcards). | [optional] 
**status** | [**List[StatusFilter]**](StatusFilter.md) | Filter on the status of the plug. Filter values with a &#x60;-&#x60; postfix exclude the status. Use the &#x60;any&#x60; filter value to include all states. When not specified, a default &#x60;undeployed-&#x60; filter excludes _undeployed_ functions. | [optional] 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**created_by** | **str** | Filter on the user that create the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**updated_by** | **str** | Filter on the user that last updated the plug. You can use the &#x60;@me&#x60; token to indicate your own plugs. | [optional] 
**created_before** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**created_after** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**updated_before** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**updated_after** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.function_version_query import FunctionVersionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionVersionQuery from a JSON string
function_version_query_instance = FunctionVersionQuery.from_json(json)
# print the JSON string representation of the object
print FunctionVersionQuery.to_json()

# convert the object into a dict
function_version_query_dict = function_version_query_instance.to_dict()
# create an instance of FunctionVersionQuery from a dict
function_version_query_form_dict = function_version_query.from_dict(function_version_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


