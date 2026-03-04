# DeploySpecOpenfaasSpec

If specified, it overrides the properties in `default`. Non-specified properties are taken from `default`

**Source:** `waylay.services.registry.models.deploy_spec_openfaas_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**constraints** | **List[str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**secrets** | **List[str]** |  | [optional] 
**registry_auth** | **str** |  | [optional] 
**limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**requests** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**read_only_root_filesystem** | **bool** |  | [optional] 


## Example

```python
from waylay.services.registry.models.deploy_spec_openfaas_spec import (
    DeploySpecOpenfaasSpec,
)

deploy_spec_openfaas_spec = DeploySpecOpenfaasSpec(
    service=...,
    image=...,
    namespace=...,
    network=...,
    env_vars=...,
    constraints=...,
    labels=...,
    annotations=...,
    secrets=...,
    registry_auth=...,
    limits=...,
    requests=...,
    read_only_root_filesystem=...,
)

# Create from JSON
deploy_spec_openfaas_spec = DeploySpecOpenfaasSpec.from_json(
    '{ "service": ..., "image": ..., "namespace": ..., "network": ..., "envVars": ..., "constraints": ..., "labels": ..., "annotations": ..., "secrets": ..., "registryAuth": ..., "limits": ..., "requests": ..., "readOnlyRootFilesystem": ... }'
)

# Export to dictionary
deploy_spec_openfaas_spec_dict = deploy_spec_openfaas_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


