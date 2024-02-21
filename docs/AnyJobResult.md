# AnyJobResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | SHA digest of the built image. | 
**log** | **List[str]** | Detailed logs of the build steps. | [optional] 
**status** | **str** | Outcome of the build. | [optional] 
**deploy_spec** | [**ExposedOpenfaasDeploySpec**](ExposedOpenfaasDeploySpec.md) |  | 
**healthy** | **bool** | If true, the deployment check succeeded. | 
**replicas** | **float** | The number of replicas this function was running at the time of the check. | [optional] 
**deployment** | **bool** |  | 
**assets** | **bool** |  | 
**registration** | **bool** |  | 
**job_count** | **float** |  | [optional] 
**scheduled_job** | [**JobReference**](JobReference.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.any_job_result import AnyJobResult

# TODO update the JSON string below
json = "{}"
# create an instance of AnyJobResult from a JSON string
any_job_result_instance = AnyJobResult.from_json(json)
# print the JSON string representation of the object
print AnyJobResult.to_json()

# convert the object into a dict
any_job_result_dict = any_job_result_instance.to_dict()
# create an instance of AnyJobResult from a dict
any_job_result_form_dict = any_job_result.from_dict(any_job_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


