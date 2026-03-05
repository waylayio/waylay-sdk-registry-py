# AssetSummaryWithHALLinkLinks

HAL links to the asset

**Source:** `waylay.services.registry.models.asset_summary_with_hal_link_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.asset_summary_with_hal_link_links import (
    AssetSummaryWithHALLinkLinks,
)

asset_summary_with_hal_link_links = AssetSummaryWithHALLinkLinks(asset=...)

# Create from JSON
asset_summary_with_hal_link_links = AssetSummaryWithHALLinkLinks.from_json(
    '{ "asset": ... }'
)

# Export to dictionary
asset_summary_with_hal_link_links_dict = asset_summary_with_hal_link_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


