# PostWebscriptJobSyncResponseV2

Webscript Deployed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 

## Example

```python
from waylay.services.registry.models.post_webscript_job_sync_response_v2 import PostWebscriptJobSyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of PostWebscriptJobSyncResponseV2 from a JSON string
post_webscript_job_sync_response_v2_instance = PostWebscriptJobSyncResponseV2.from_json(json)
# print the JSON string representation of the object
print PostWebscriptJobSyncResponseV2.to_json()

# convert the object into a dict
post_webscript_job_sync_response_v2_dict = post_webscript_job_sync_response_v2_instance.to_dict()
# create an instance of PostWebscriptJobSyncResponseV2 from a dict
post_webscript_job_sync_response_v2_form_dict = post_webscript_job_sync_response_v2.from_dict(post_webscript_job_sync_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


