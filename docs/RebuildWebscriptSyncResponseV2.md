# RebuildWebscriptSyncResponseV2

Webscript Rebuild Ignored

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**causes** | [**JobCauses**](JobCauses.md) |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 

## Example

```python
from waylay.services.registry.models.rebuild_webscript_sync_response_v2 import RebuildWebscriptSyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildWebscriptSyncResponseV2 from a JSON string
rebuild_webscript_sync_response_v2_instance = RebuildWebscriptSyncResponseV2.from_json(json)
# print the JSON string representation of the object
print RebuildWebscriptSyncResponseV2.to_json()

# convert the object into a dict
rebuild_webscript_sync_response_v2_dict = rebuild_webscript_sync_response_v2_instance.to_dict()
# create an instance of RebuildWebscriptSyncResponseV2 from a dict
rebuild_webscript_sync_response_v2_form_dict = rebuild_webscript_sync_response_v2.from_dict(rebuild_webscript_sync_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


