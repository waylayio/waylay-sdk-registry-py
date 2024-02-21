# UnhealthyInvokableWebscriptError

Webscript Not Healthy

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity** | [**InvokableWebscriptResponseEntity**](InvokableWebscriptResponseEntity.md) |  | 
**links** | [**InvokeInternalHALLink**](InvokeInternalHALLink.md) |  | 
**error** | **str** |  | 
**code** | **str** |  | 

## Example

```python
from waylay.services.registry.models.unhealthy_invokable_webscript_error import UnhealthyInvokableWebscriptError

# TODO update the JSON string below
json = "{}"
# create an instance of UnhealthyInvokableWebscriptError from a JSON string
unhealthy_invokable_webscript_error_instance = UnhealthyInvokableWebscriptError.from_json(json)
# print the JSON string representation of the object
print UnhealthyInvokableWebscriptError.to_json()

# convert the object into a dict
unhealthy_invokable_webscript_error_dict = unhealthy_invokable_webscript_error_instance.to_dict()
# create an instance of UnhealthyInvokableWebscriptError from a dict
unhealthy_invokable_webscript_error_form_dict = unhealthy_invokable_webscript_error.from_dict(unhealthy_invokable_webscript_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


