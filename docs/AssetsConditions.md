# AssetsConditions

Describes the assets that are required/allowed/supported for a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conditions** | [**List[AssetCondition]**](AssetCondition.md) | All files in a function archive are checked against these conditions. A file that is not matched is ignored. | [optional] 
**max_size** | **str** | The maximum size of the archive (in bytes, unless unit is provided) | [optional] 

## Example

```python
from waylay.services.registry.models.assets_conditions import AssetsConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AssetsConditions from a JSON string
assets_conditions_instance = AssetsConditions.from_json(json)
# print the JSON string representation of the object
print AssetsConditions.to_json()

# convert the object into a dict
assets_conditions_dict = assets_conditions_instance.to_dict()
# create an instance of AssetsConditions from a dict
assets_conditions_form_dict = assets_conditions.from_dict(assets_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


