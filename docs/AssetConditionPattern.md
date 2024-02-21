# AssetConditionPattern

Pattern that selects a file in a function archive

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.asset_condition_pattern import AssetConditionPattern

# TODO update the JSON string below
json = "{}"
# create an instance of AssetConditionPattern from a JSON string
asset_condition_pattern_instance = AssetConditionPattern.from_json(json)
# print the JSON string representation of the object
print AssetConditionPattern.to_json()

# convert the object into a dict
asset_condition_pattern_dict = asset_condition_pattern_instance.to_dict()
# create an instance of AssetConditionPattern from a dict
asset_condition_pattern_form_dict = asset_condition_pattern.from_dict(asset_condition_pattern_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


