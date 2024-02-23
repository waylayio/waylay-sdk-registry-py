# WithAssetHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**AssetSummaryWithHALLinkLinks**](AssetSummaryWithHALLinkLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.with_asset_hal_link import WithAssetHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of WithAssetHALLink from a JSON string
with_asset_hal_link_instance = WithAssetHALLink.from_json(json)
# print the JSON string representation of the object
print WithAssetHALLink.to_json()

# convert the object into a dict
with_asset_hal_link_dict = with_asset_hal_link_instance.to_dict()
# create an instance of WithAssetHALLink from a dict
with_asset_hal_link_form_dict = with_asset_hal_link.from_dict(with_asset_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


