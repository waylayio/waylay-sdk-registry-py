# ScaleJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ScaleType**](ScaleType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**ScaleArgs**](ScaleArgs.md) |  | 
**result** | **object** | The result data for a completed scale job. | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from waylay.services.registry.models.scale_job_status import ScaleJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of ScaleJobStatus from a JSON string
scale_job_status_instance = ScaleJobStatus.from_json(json)
# print the JSON string representation of the object
print ScaleJobStatus.to_json()

# convert the object into a dict
scale_job_status_dict = scale_job_status_instance.to_dict()
# create an instance of ScaleJobStatus from a dict
scale_job_status_form_dict = scale_job_status.from_dict(scale_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


