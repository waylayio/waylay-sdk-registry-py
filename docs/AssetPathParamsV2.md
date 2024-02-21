# AssetPathParamsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wildcard** | **str** | Full path or path prefix of the asset within the archive | 

## Example

```python
from waylay.services.registry.models.asset_path_params_v2 import AssetPathParamsV2

# TODO update the JSON string below
json = "{}"
# create an instance of AssetPathParamsV2 from a JSON string
asset_path_params_v2_instance = AssetPathParamsV2.from_json(json)
# print the JSON string representation of the object
print AssetPathParamsV2.to_json()

# convert the object into a dict
asset_path_params_v2_dict = asset_path_params_v2_instance.to_dict()
# create an instance of AssetPathParamsV2 from a dict
asset_path_params_v2_form_dict = asset_path_params_v2.from_dict(asset_path_params_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


