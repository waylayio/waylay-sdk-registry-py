# Model


**Source:** `waylay.services.registry.models.model`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**model** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.model import Model

model = Model(event=..., model=...)

# Create from JSON
model = Model.from_json('{ "event": ..., "model": ... }')

# Export to dictionary
model_dict = model.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


