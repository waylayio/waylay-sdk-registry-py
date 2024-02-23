# AssetSummaryWithHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**AssetSummaryWithHALLinkLinks**](AssetSummaryWithHALLinkLinks.md) |  | 
**name** | **str** | File name | 
**title** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**role** | [**AssetRole**](AssetRole.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.asset_summary_with_hal_link import AssetSummaryWithHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of AssetSummaryWithHALLink from a JSON string
asset_summary_with_hal_link_instance = AssetSummaryWithHALLink.from_json(json)
# print the JSON string representation of the object
print AssetSummaryWithHALLink.to_json()

# convert the object into a dict
asset_summary_with_hal_link_dict = asset_summary_with_hal_link_instance.to_dict()
# create an instance of AssetSummaryWithHALLink from a dict
asset_summary_with_hal_link_form_dict = asset_summary_with_hal_link.from_dict(asset_summary_with_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


