# BuildJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**BuildType**](BuildType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**BuildArgs**](BuildArgs.md) |  | 
**result** | [**BuildResult**](BuildResult.md) |  | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from waylay.services.registry.models.build_job_status import BuildJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of BuildJobStatus from a JSON string
build_job_status_instance = BuildJobStatus.from_json(json)
# print the JSON string representation of the object
print BuildJobStatus.to_json()

# convert the object into a dict
build_job_status_dict = build_job_status_instance.to_dict()
# create an instance of BuildJobStatus from a dict
build_job_status_form_dict = build_job_status.from_dict(build_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


