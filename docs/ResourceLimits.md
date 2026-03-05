# ResourceLimits


**Source:** `waylay.services.registry.models.resource_limits`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | **str** |  | [optional] 
**cpu** | **str** |  | [optional] 


## Example

```python
from waylay.services.registry.models.resource_limits import ResourceLimits

resource_limits = ResourceLimits(memory=..., cpu=...)

# Create from JSON
resource_limits = ResourceLimits.from_json('{ "memory": ..., "cpu": ... }')

# Export to dictionary
resource_limits_dict = resource_limits.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


