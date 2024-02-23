# InvokeInternalHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke_internal** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.invoke_internal_hal_link import InvokeInternalHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of InvokeInternalHALLink from a JSON string
invoke_internal_hal_link_instance = InvokeInternalHALLink.from_json(json)
# print the JSON string representation of the object
print InvokeInternalHALLink.to_json()

# convert the object into a dict
invoke_internal_hal_link_dict = invoke_internal_hal_link_instance.to_dict()
# create an instance of InvokeInternalHALLink from a dict
invoke_internal_hal_link_form_dict = invoke_internal_hal_link.from_dict(invoke_internal_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


