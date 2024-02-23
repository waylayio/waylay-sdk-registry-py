# LatestPlugVersionQueryV2

Latest named plug version listing query

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugType**](PlugType.md) |  | [optional] 
**include_draft** | **bool** | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**include_deprecated** | **bool** | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 

## Example

```python
from waylay.services.registry.models.latest_plug_version_query_v2 import LatestPlugVersionQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of LatestPlugVersionQueryV2 from a JSON string
latest_plug_version_query_v2_instance = LatestPlugVersionQueryV2.from_json(json)
# print the JSON string representation of the object
print LatestPlugVersionQueryV2.to_json()

# convert the object into a dict
latest_plug_version_query_v2_dict = latest_plug_version_query_v2_instance.to_dict()
# create an instance of LatestPlugVersionQueryV2 from a dict
latest_plug_version_query_v2_form_dict = latest_plug_version_query_v2.from_dict(latest_plug_version_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


