# DeployJobStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of the background task. | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**DeployArgs**](DeployArgs.md) |  | 
**result** | [**DeployResult**](DeployResult.md) |  | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | 

## Example

```python
from waylay.services.registry.models.deploy_job_status import DeployJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of DeployJobStatus from a JSON string
deploy_job_status_instance = DeployJobStatus.from_json(json)
# print the JSON string representation of the object
print DeployJobStatus.to_json()

# convert the object into a dict
deploy_job_status_dict = deploy_job_status_instance.to_dict()
# create an instance of DeployJobStatus from a dict
deploy_job_status_form_dict = deploy_job_status.from_dict(deploy_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


