# JobReferenceParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobType**](JobType.md) |  | 
**id** | **str** |  | 

## Example

```python
from waylay.services.registry.models.job_reference_params import JobReferenceParams

# TODO update the JSON string below
json = "{}"
# create an instance of JobReferenceParams from a JSON string
job_reference_params_instance = JobReferenceParams.from_json(json)
# print the JSON string representation of the object
print JobReferenceParams.to_json()

# convert the object into a dict
job_reference_params_dict = job_reference_params_instance.to_dict()
# create an instance of JobReferenceParams from a dict
job_reference_params_form_dict = job_reference_params.from_dict(job_reference_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


