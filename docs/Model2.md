# Model2


**Source:** `waylay.services.registry.models.model2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**model** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.model2 import Model2

model2 = Model2(job=..., model=...)

# Create from JSON
model2 = Model2.from_json('{ "job": ..., "model": ... }')

# Export to dictionary
model2_dict = model2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


