# PlugInterface


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | **List[str]** | The states of a plug as implemented in the plug code. | [optional] 
**input** | [**List[PlugProperty]**](PlugProperty.md) | The named input parameters of a plug | [optional] 
**output** | [**List[PlugProperty]**](PlugProperty.md) | The named output parameters of a plug | [optional] 

## Example

```python
from waylay.services.registry.models.plug_interface import PlugInterface

# TODO update the JSON string below
json = "{}"
# create an instance of PlugInterface from a JSON string
plug_interface_instance = PlugInterface.from_json(json)
# print the JSON string representation of the object
print PlugInterface.to_json()

# convert the object into a dict
plug_interface_dict = plug_interface_instance.to_dict()
# create an instance of PlugInterface from a dict
plug_interface_form_dict = plug_interface.from_dict(plug_interface_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


