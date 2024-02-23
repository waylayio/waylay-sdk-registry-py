# PostModelJobSyncResponseV2

Model Deployed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 

## Example

```python
from waylay.services.registry.models.post_model_job_sync_response_v2 import PostModelJobSyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of PostModelJobSyncResponseV2 from a JSON string
post_model_job_sync_response_v2_instance = PostModelJobSyncResponseV2.from_json(json)
# print the JSON string representation of the object
print PostModelJobSyncResponseV2.to_json()

# convert the object into a dict
post_model_job_sync_response_v2_dict = post_model_job_sync_response_v2_instance.to_dict()
# create an instance of PostModelJobSyncResponseV2 from a dict
post_model_job_sync_response_v2_form_dict = post_model_job_sync_response_v2.from_dict(post_model_job_sync_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


