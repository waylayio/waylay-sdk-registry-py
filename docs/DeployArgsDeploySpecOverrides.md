# DeployArgsDeploySpecOverrides

Overrides on the deployment specification.

**Source:** `waylay.services.registry.models.deploy_args_deploy_spec_overrides`




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
from waylay.services.registry.models.deploy_args_deploy_spec_overrides import (
    DeployArgsDeploySpecOverrides,
)

deploy_args_deploy_spec_overrides = DeployArgsDeploySpecOverrides(
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
deploy_args_deploy_spec_overrides = DeployArgsDeploySpecOverrides.from_json(
    '{ "service": ..., "image": ..., "namespace": ..., "network": ..., "envVars": ..., "constraints": ..., "labels": ..., "annotations": ..., "secrets": ..., "registryAuth": ..., "limits": ..., "requests": ..., "readOnlyRootFilesystem": ... }'
)

# Export to dictionary
deploy_args_deploy_spec_overrides_dict = deploy_args_deploy_spec_overrides.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


