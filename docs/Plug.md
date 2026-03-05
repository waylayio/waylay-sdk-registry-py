# Plug


**Source:** `waylay.services.registry.models.plug`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**plug** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.plug import Plug

plug = Plug(event=..., plug=...)

# Create from JSON
plug = Plug.from_json('{ "event": ..., "plug": ... }')

# Export to dictionary
plug_dict = plug.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


