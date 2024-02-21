# FunctionDeployOverridesType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**env_vars** | **Dict[str, str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**requests** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.function_deploy_overrides_type import FunctionDeployOverridesType

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDeployOverridesType from a JSON string
function_deploy_overrides_type_instance = FunctionDeployOverridesType.from_json(json)
# print the JSON string representation of the object
print FunctionDeployOverridesType.to_json()

# convert the object into a dict
function_deploy_overrides_type_dict = function_deploy_overrides_type_instance.to_dict()
# create an instance of FunctionDeployOverridesType from a dict
function_deploy_overrides_type_form_dict = function_deploy_overrides_type.from_dict(function_deploy_overrides_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


