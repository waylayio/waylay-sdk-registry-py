# AssetSummaryWithHALLink


**Source:** `waylay.services.registry.models.asset_summary_with_hal_link`




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
from waylay.services.registry.models.asset_summary_with_hal_link import (
    AssetSummaryWithHALLink,
)

asset_summary_with_hal_link = AssetSummaryWithHALLink(
    links=..., name=..., title=..., description=..., role=...
)

# Create from JSON
asset_summary_with_hal_link = AssetSummaryWithHALLink.from_json(
    '{ "_links": ..., "name": ..., "title": ..., "description": ..., "role": ... }'
)

# Export to dictionary
asset_summary_with_hal_link_dict = asset_summary_with_hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


