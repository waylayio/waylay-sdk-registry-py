# DeployResult

The result data for a completed deployment job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy_spec** | [**ExposedOpenfaasDeploySpec**](ExposedOpenfaasDeploySpec.md) |  | 

## Example

```python
from waylay.services.registry.models.deploy_result import DeployResult

# TODO update the JSON string below
json = "{}"
# create an instance of DeployResult from a JSON string
deploy_result_instance = DeployResult.from_json(json)
# print the JSON string representation of the object
print DeployResult.to_json()

# convert the object into a dict
deploy_result_dict = deploy_result_instance.to_dict()
# create an instance of DeployResult from a dict
deploy_result_form_dict = deploy_result.from_dict(deploy_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


