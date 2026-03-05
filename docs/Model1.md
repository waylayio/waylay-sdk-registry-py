# Model1


**Source:** `waylay.services.registry.models.model1`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**model** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.model1 import Model1

model1 = Model1(event=..., job=..., model=...)

# Create from JSON
model1 = Model1.from_json('{ "event": ..., "job": ..., "model": ... }')

# Export to dictionary
model1_dict = model1.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


