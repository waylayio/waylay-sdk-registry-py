# AssetsConditions

Describes the assets that are required/allowed/supported for a function.

**Source:** `waylay.services.registry.models.assets_conditions`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[AssetCondition]**](AssetCondition.md) | All files in a function archive are checked against these conditions. A file that is not matched is ignored. | [optional] 
**max_size** | **str** | The maximum size of the archive (in bytes, unless unit is provided) | [optional] 


## Example

```python
from waylay.services.registry.models.assets_conditions import AssetsConditions

assets_conditions = AssetsConditions(conditions=..., max_size=...)

# Create from JSON
assets_conditions = AssetsConditions.from_json('{ "conditions": ..., "maxSize": ... }')

# Export to dictionary
assets_conditions_dict = assets_conditions.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


