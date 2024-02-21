# KFServingDeleteMultipleWithJobResponse

Model Deletions Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**versions** | **List[str]** |  | 
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.kf_serving_delete_multiple_with_job_response import KFServingDeleteMultipleWithJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KFServingDeleteMultipleWithJobResponse from a JSON string
kf_serving_delete_multiple_with_job_response_instance = KFServingDeleteMultipleWithJobResponse.from_json(json)
# print the JSON string representation of the object
print KFServingDeleteMultipleWithJobResponse.to_json()

# convert the object into a dict
kf_serving_delete_multiple_with_job_response_dict = kf_serving_delete_multiple_with_job_response_instance.to_dict()
# create an instance of KFServingDeleteMultipleWithJobResponse from a dict
kf_serving_delete_multiple_with_job_response_form_dict = kf_serving_delete_multiple_with_job_response.from_dict(kf_serving_delete_multiple_with_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


