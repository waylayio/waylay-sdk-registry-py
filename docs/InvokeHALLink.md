# InvokeHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.invoke_hal_link import InvokeHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeHALLink from a JSON string
invoke_hal_link_instance = InvokeHALLink.from_json(json)
# print the JSON string representation of the object
print InvokeHALLink.to_json()

# convert the object into a dict
invoke_hal_link_dict = invoke_hal_link_instance.to_dict()
# create an instance of InvokeHALLink from a dict
invoke_hal_link_form_dict = invoke_hal_link.from_dict(invoke_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


