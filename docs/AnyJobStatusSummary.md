# AnyJobStatusSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**BatchJobStatusType**](BatchJobStatusType.md) |  | 
**id** | **str** | The id of the background job, or the constant &#x60;_unknown_&#x60; | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 

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


