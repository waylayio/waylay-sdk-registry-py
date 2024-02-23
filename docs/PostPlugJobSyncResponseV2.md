# PostPlugJobSyncResponseV2

Plug Deployed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**PlugResponseV2**](PlugResponseV2.md) |  | 

## Example

```python
from waylay.services.registry.models.post_plug_job_sync_response_v2 import PostPlugJobSyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of PostPlugJobSyncResponseV2 from a JSON string
post_plug_job_sync_response_v2_instance = PostPlugJobSyncResponseV2.from_json(json)
# print the JSON string representation of the object
print PostPlugJobSyncResponseV2.to_json()

# convert the object into a dict
post_plug_job_sync_response_v2_dict = post_plug_job_sync_response_v2_instance.to_dict()
# create an instance of PostPlugJobSyncResponseV2 from a dict
post_plug_job_sync_response_v2_form_dict = post_plug_job_sync_response_v2.from_dict(post_plug_job_sync_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


