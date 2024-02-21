# AnyJobStatusSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the background task. | 
**operation** | **str** | The operation name for the background task. | 
**id** | **str** | The id of the background job, or the constant &#x60;_unknown_&#x60; | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**created_at** | **datetime** | The creation time of this job | 
**created_by** | **str** | The user that initiated this job | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.any_job_status_summary import AnyJobStatusSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AnyJobStatusSummary from a JSON string
any_job_status_summary_instance = AnyJobStatusSummary.from_json(json)
# print the JSON string representation of the object
print AnyJobStatusSummary.to_json()

# convert the object into a dict
any_job_status_summary_dict = any_job_status_summary_instance.to_dict()
# create an instance of AnyJobStatusSummary from a dict
any_job_status_summary_form_dict = any_job_status_summary.from_dict(any_job_status_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


