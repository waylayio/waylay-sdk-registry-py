# JobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**progress** | [**JobStatusProgress**](JobStatusProgress.md) |  | 
**attempts_made** | **float** |  | 
**finished_on** | **datetime** |  | [optional] 
**processed_on** | **datetime** |  | [optional] 
**failed_reason** | **str** |  | [optional] 
**parent** | [**ParentKeys**](ParentKeys.md) |  | [optional] 
**delay** | **float** |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_status import JobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatus from a JSON string
job_status_instance = JobStatus.from_json(json)
# print the JSON string representation of the object
print JobStatus.to_json()

# convert the object into a dict
job_status_dict = job_status_instance.to_dict()
# create an instance of JobStatus from a dict
job_status_form_dict = job_status.from_dict(job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


