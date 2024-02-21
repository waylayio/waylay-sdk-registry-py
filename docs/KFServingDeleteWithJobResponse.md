# KFServingDeleteWithJobResponse

Model Delete Initiated

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**name** | **str** | The name of the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.kf_serving_delete_with_job_response import KFServingDeleteWithJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KFServingDeleteWithJobResponse from a JSON string
kf_serving_delete_with_job_response_instance = KFServingDeleteWithJobResponse.from_json(json)
# print the JSON string representation of the object
print KFServingDeleteWithJobResponse.to_json()

# convert the object into a dict
kf_serving_delete_with_job_response_dict = kf_serving_delete_with_job_response_instance.to_dict()
# create an instance of KFServingDeleteWithJobResponse from a dict
kf_serving_delete_with_job_response_form_dict = kf_serving_delete_with_job_response.from_dict(kf_serving_delete_with_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


