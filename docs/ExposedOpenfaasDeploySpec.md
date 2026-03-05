# ExposedOpenfaasDeploySpec


**Source:** `waylay.services.registry.models.exposed_openfaas_deploy_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | 
**image** | **str** |  | 
**namespace** | **str** |  | 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**requests** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.exposed_openfaas_deploy_spec import (
    ExposedOpenfaasDeploySpec,
)

exposed_openfaas_deploy_spec = ExposedOpenfaasDeploySpec(
    service=...,
    image=...,
    namespace=...,
    labels=...,
    annotations=...,
    limits=...,
    requests=...,
)

# Create from JSON
exposed_openfaas_deploy_spec = ExposedOpenfaasDeploySpec.from_json(
    '{ "service": ..., "image": ..., "namespace": ..., "labels": ..., "annotations": ..., "limits": ..., "requests": ... }'
)

# Export to dictionary
exposed_openfaas_deploy_spec_dict = exposed_openfaas_deploy_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


