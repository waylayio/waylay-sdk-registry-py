# FunctionDeployOverrides


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.function_deploy_overrides import FunctionDeployOverrides

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionDeployOverrides from a JSON string
function_deploy_overrides_instance = FunctionDeployOverrides.from_json(json)
# print the JSON string representation of the object
print FunctionDeployOverrides.to_json()

# convert the object into a dict
function_deploy_overrides_dict = function_deploy_overrides_instance.to_dict()
# create an instance of FunctionDeployOverrides from a dict
function_deploy_overrides_form_dict = function_deploy_overrides.from_dict(function_deploy_overrides_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


