# Plug1


**Source:** `waylay.services.registry.models.plug1`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**plug** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.plug1 import Plug1

plug1 = Plug1(event=..., job=..., plug=...)

# Create from JSON
plug1 = Plug1.from_json('{ "event": ..., "job": ..., "plug": ... }')

# Export to dictionary
plug1_dict = plug1.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


