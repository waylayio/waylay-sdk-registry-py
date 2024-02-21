# NamedParametersTypeofAsJobReferenceJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**type** | **object** | The type of the background task. | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | **object** | The request that initiated this job. | [optional] 
**result** | **object** | The result of the job if completed. | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.named_parameters_typeof_as_job_reference_job_status import NamedParametersTypeofAsJobReferenceJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of NamedParametersTypeofAsJobReferenceJobStatus from a JSON string
named_parameters_typeof_as_job_reference_job_status_instance = NamedParametersTypeofAsJobReferenceJobStatus.from_json(json)
# print the JSON string representation of the object
print NamedParametersTypeofAsJobReferenceJobStatus.to_json()

# convert the object into a dict
named_parameters_typeof_as_job_reference_job_status_dict = named_parameters_typeof_as_job_reference_job_status_instance.to_dict()
# create an instance of NamedParametersTypeofAsJobReferenceJobStatus from a dict
named_parameters_typeof_as_job_reference_job_status_form_dict = named_parameters_typeof_as_job_reference_job_status.from_dict(named_parameters_typeof_as_job_reference_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


