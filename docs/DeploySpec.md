# DeploySpec


**Source:** `waylay.services.registry.models.deploy_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openfaas_spec** | [**DeploySpecOpenfaasSpec**](DeploySpecOpenfaasSpec.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.deploy_spec import DeploySpec

deploy_spec = DeploySpec(openfaas_spec=...)

# Create from JSON
deploy_spec = DeploySpec.from_json('{ "openfaasSpec": ... }')

# Export to dictionary
deploy_spec_dict = deploy_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


