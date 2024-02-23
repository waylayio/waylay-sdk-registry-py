# InvokableWebscriptResponseEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Status**](Status.md) |  | 
**draft** | **bool** |  | 
**webscript** | [**InvokableWebscriptResponseEntityWebscript**](InvokableWebscriptResponseEntityWebscript.md) |  | 
**secret** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.invokable_webscript_response_entity import InvokableWebscriptResponseEntity

# TODO update the JSON string below
json = "{}"
# create an instance of InvokableWebscriptResponseEntity from a JSON string
invokable_webscript_response_entity_instance = InvokableWebscriptResponseEntity.from_json(json)
# print the JSON string representation of the object
print InvokableWebscriptResponseEntity.to_json()

# convert the object into a dict
invokable_webscript_response_entity_dict = invokable_webscript_response_entity_instance.to_dict()
# create an instance of InvokableWebscriptResponseEntity from a dict
invokable_webscript_response_entity_form_dict = invokable_webscript_response_entity.from_dict(invokable_webscript_response_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


