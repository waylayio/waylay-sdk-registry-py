# Undeploy1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | **str** | The type of operation that was executed. | 
**created_by** | **str** | The user identity that was used to execute the job. | 
**created_at** | **datetime** | The timestamp of when the job was created. | 
**processed_at** | **datetime** | The timestamp of when the job has begun processing. | [optional] 
**finished_at** | **object** | The timestamp of when the job has finished processing. | [optional] 
**attempts_made** | **float** | The number of retries that were attempted. | [optional] 
**type** | [**UndeployType**](UndeployType.md) |  | 
**id** | **str** | The id of the background job, or the constant &#x60;_unknown_&#x60; | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**links** | [**JobAndFunctionHALLink**](JobAndFunctionHALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.undeploy1 import Undeploy1

# TODO update the JSON string below
json = "{}"
# create an instance of Undeploy1 from a JSON string
undeploy1_instance = Undeploy1.from_json(json)
# print the JSON string representation of the object
print Undeploy1.to_json()

# convert the object into a dict
undeploy1_dict = undeploy1_instance.to_dict()
# create an instance of Undeploy1 from a dict
undeploy1_form_dict = undeploy1.from_dict(undeploy1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


