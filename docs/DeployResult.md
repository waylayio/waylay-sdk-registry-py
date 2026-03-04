# DeployResult

The result data for a completed deployment job.

**Source:** `waylay.services.registry.models.deploy_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy_spec** | [**ExposedOpenfaasDeploySpec**](ExposedOpenfaasDeploySpec.md) |  | 


## Example

```python
from waylay.services.registry.models.deploy_result import DeployResult

deploy_result = DeployResult(deploy_spec=...)

# Create from JSON
deploy_result = DeployResult.from_json('{ "deploySpec": ... }')

# Export to dictionary
deploy_result_dict = deploy_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


