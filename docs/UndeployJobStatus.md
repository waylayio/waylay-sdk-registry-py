# UndeployJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the background task. | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**UndeployArgs**](UndeployArgs.md) |  | 
**result** | [**UndeployResult**](UndeployResult.md) |  | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from waylay.services.registry.models.undeploy_job_status import UndeployJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of UndeployJobStatus from a JSON string
undeploy_job_status_instance = UndeployJobStatus.from_json(json)
# print the JSON string representation of the object
print UndeployJobStatus.to_json()

# convert the object into a dict
undeploy_job_status_dict = undeploy_job_status_instance.to_dict()
# create an instance of UndeployJobStatus from a dict
undeploy_job_status_form_dict = undeploy_job_status.from_dict(undeploy_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


