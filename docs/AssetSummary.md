# AssetSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | File name | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role** | [**AssetRole**](AssetRole.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.asset_summary import AssetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AssetSummary from a JSON string
asset_summary_instance = AssetSummary.from_json(json)
# print the JSON string representation of the object
print AssetSummary.to_json()

# convert the object into a dict
asset_summary_dict = asset_summary_instance.to_dict()
# create an instance of AssetSummary from a dict
asset_summary_form_dict = asset_summary.from_dict(asset_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


