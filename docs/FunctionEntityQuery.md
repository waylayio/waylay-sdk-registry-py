# FunctionEntityQuery

Filter on function attributes that do not change across function versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Filter on the name of the function. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**archive_format** | [**List[ArchiveFormat]**](ArchiveFormat.md) | Filter on the archive format of the function. | [optional] 
**runtime** | **List[str]** | Filter on the runtime of the function. | [optional] 

## Example

```python
from waylay.services.registry.models.function_entity_query import FunctionEntityQuery

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionEntityQuery from a JSON string
function_entity_query_instance = FunctionEntityQuery.from_json(json)
# print the JSON string representation of the object
print FunctionEntityQuery.to_json()

# convert the object into a dict
function_entity_query_dict = function_entity_query_instance.to_dict()
# create an instance of FunctionEntityQuery from a dict
function_entity_query_form_dict = function_entity_query.from_dict(function_entity_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


