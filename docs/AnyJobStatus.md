# AnyJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the background task. | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**BatchArgs**](BatchArgs.md) |  | 
**result** | [**BatchResult**](BatchResult.md) |  | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from waylay.services.registry.models.any_job_status import AnyJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AnyJobStatus from a JSON string
any_job_status_instance = AnyJobStatus.from_json(json)
# print the JSON string representation of the object
print AnyJobStatus.to_json()

# convert the object into a dict
any_job_status_dict = any_job_status_instance.to_dict()
# create an instance of AnyJobStatus from a dict
any_job_status_form_dict = any_job_status.from_dict(any_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


