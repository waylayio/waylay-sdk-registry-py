# VerifyWebscriptSyncResponseV2

Webscript Health Verified

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 
**result** | [**VerifyResult**](VerifyResult.md) |  | 

## Example

```python
from waylay.services.registry.models.verify_webscript_sync_response_v2 import VerifyWebscriptSyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyWebscriptSyncResponseV2 from a JSON string
verify_webscript_sync_response_v2_instance = VerifyWebscriptSyncResponseV2.from_json(json)
# print the JSON string representation of the object
print VerifyWebscriptSyncResponseV2.to_json()

# convert the object into a dict
verify_webscript_sync_response_v2_dict = verify_webscript_sync_response_v2_instance.to_dict()
# create an instance of VerifyWebscriptSyncResponseV2 from a dict
verify_webscript_sync_response_v2_form_dict = verify_webscript_sync_response_v2.from_dict(verify_webscript_sync_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


