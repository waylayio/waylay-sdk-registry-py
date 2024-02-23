# InvokableWebscriptResponse

Webscript Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**InvokableWebscriptResponseEntity**](InvokableWebscriptResponseEntity.md) |  | 
**links** | [**InvokeInternalHALLink**](InvokeInternalHALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.invokable_webscript_response import InvokableWebscriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvokableWebscriptResponse from a JSON string
invokable_webscript_response_instance = InvokableWebscriptResponse.from_json(json)
# print the JSON string representation of the object
print InvokableWebscriptResponse.to_json()

# convert the object into a dict
invokable_webscript_response_dict = invokable_webscript_response_instance.to_dict()
# create an instance of InvokableWebscriptResponse from a dict
invokable_webscript_response_form_dict = invokable_webscript_response.from_dict(invokable_webscript_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


