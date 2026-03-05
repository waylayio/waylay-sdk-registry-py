# Webscript


**Source:** `waylay.services.registry.models.webscript`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**webscript** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.webscript import Webscript

webscript = Webscript(event=..., webscript=...)

# Create from JSON
webscript = Webscript.from_json('{ "event": ..., "webscript": ... }')

# Export to dictionary
webscript_dict = webscript.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


