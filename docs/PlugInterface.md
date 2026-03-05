# PlugInterface


**Source:** `waylay.services.registry.models.plug_interface`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**states** | **List[str]** | The states of a plug as implemented in the plug code. Required and supported for &#x60;type&#x3D;sensor&#x60; plugs _only_. | [optional] 
**input** | [**List[PlugProperty]**](PlugProperty.md) | The named input parameters of a plug. Supported for &#x60;type&#x3D;sensor&#x60; plugs; fixed with input attributes &#x60;data&#x60; and &#x60;resource&#x60; for &#x60;type&#x3D;transformer&#x60;plugs. | [optional] 
**output** | [**List[PlugProperty]**](PlugProperty.md) | The named output parameters of a plug. Supported for all plug types. | [optional] 


## Example

```python
from waylay.services.registry.models.plug_interface import PlugInterface

plug_interface = PlugInterface(states=..., input=..., output=...)

# Create from JSON
plug_interface = PlugInterface.from_json(
    '{ "states": ..., "input": ..., "output": ... }'
)

# Export to dictionary
plug_interface_dict = plug_interface.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


