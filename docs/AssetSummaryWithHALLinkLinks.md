# AssetSummaryWithHALLinkLinks

HAL links to the asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**HALLink**](HALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.asset_summary_with_hal_link_links import AssetSummaryWithHALLinkLinks

# TODO update the JSON string below
json = "{}"
# create an instance of AssetSummaryWithHALLinkLinks from a JSON string
asset_summary_with_hal_link_links_instance = AssetSummaryWithHALLinkLinks.from_json(json)
# print the JSON string representation of the object
print AssetSummaryWithHALLinkLinks.to_json()

# convert the object into a dict
asset_summary_with_hal_link_links_dict = asset_summary_with_hal_link_links_instance.to_dict()
# create an instance of AssetSummaryWithHALLinkLinks from a dict
asset_summary_with_hal_link_links_form_dict = asset_summary_with_hal_link_links.from_dict(asset_summary_with_hal_link_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


