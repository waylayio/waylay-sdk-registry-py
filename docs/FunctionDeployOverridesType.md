# FunctionDeployOverridesType


**Source:** `waylay.services.registry.models.function_deploy_overrides_type`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**requests** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**secrets** | **List[str]** |  | [optional] 


## Example

```python
from waylay.services.registry.models.function_deploy_overrides_type import (
    FunctionDeployOverridesType,
)

function_deploy_overrides_type = FunctionDeployOverridesType(
    env_vars=..., labels=..., annotations=..., limits=..., requests=..., secrets=...
)

# Create from JSON
function_deploy_overrides_type = FunctionDeployOverridesType.from_json(
    '{ "envVars": ..., "labels": ..., "annotations": ..., "limits": ..., "requests": ..., "secrets": ... }'
)

# Export to dictionary
function_deploy_overrides_type_dict = function_deploy_overrides_type.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


