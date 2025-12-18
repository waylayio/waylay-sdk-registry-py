# Undeploy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**UndeployType**](UndeployType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**UndeployArgs**](UndeployArgs.md) |  | [optional] 
**result** | [**UndeployResult**](UndeployResult.md) |  | [optional] 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.undeploy import Undeploy

# TODO update the JSON string below
json = "{}"
# create an instance of Undeploy from a JSON string
undeploy_instance = Undeploy.from_json(json)
# print the JSON string representation of the object
print Undeploy.to_json()

# convert the object into a dict
undeploy_dict = undeploy_instance.to_dict()
# create an instance of Undeploy from a dict
undeploy_form_dict = undeploy.from_dict(undeploy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


