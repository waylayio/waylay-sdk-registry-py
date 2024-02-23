# PostModelJobAsyncResponseV2

Model Deployment Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 

## Example

```python
from waylay.services.registry.models.post_model_job_async_response_v2 import PostModelJobAsyncResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of PostModelJobAsyncResponseV2 from a JSON string
post_model_job_async_response_v2_instance = PostModelJobAsyncResponseV2.from_json(json)
# print the JSON string representation of the object
print PostModelJobAsyncResponseV2.to_json()

# convert the object into a dict
post_model_job_async_response_v2_dict = post_model_job_async_response_v2_instance.to_dict()
# create an instance of PostModelJobAsyncResponseV2 from a dict
post_model_job_async_response_v2_form_dict = post_model_job_async_response_v2.from_dict(post_model_job_async_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


