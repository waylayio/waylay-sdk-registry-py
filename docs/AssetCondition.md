# AssetCondition

Describes conditions on the set of files that match a file pattern.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role** | [**AssetRole**](AssetRole.md) |  | 
**pattern** | [**AssetConditionPattern**](AssetConditionPattern.md) |  | 
**content_type** | [**AssetConditionContentType**](AssetConditionContentType.md) |  | [optional] 
**min** | **float** | The minimal number of files that must match this pattern. Use &#x60;0&#x60; for an optional file. | [optional] 
**max** | **float** | The maximal number of files that can match this pattern. Use &#x60;0&#x60; for a disallowed file. This condition only raises an error if there are no other conditions that | [optional] 
**max_size** | **str** | The maximum size for each file matching this pattern (in bytes, unless unit is provided) | [optional] 
**var_schema** | **object** | The json schema validator that applies (in case of &#x60;application/json&#x60; entries). | [optional] 

## Example

```python
from waylay.services.registry.models.asset_condition import AssetCondition

# TODO update the JSON string below
json = "{}"
# create an instance of AssetCondition from a JSON string
asset_condition_instance = AssetCondition.from_json(json)
# print the JSON string representation of the object
print AssetCondition.to_json()

# convert the object into a dict
asset_condition_dict = asset_condition_instance.to_dict()
# create an instance of AssetCondition from a dict
asset_condition_form_dict = asset_condition.from_dict(asset_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


