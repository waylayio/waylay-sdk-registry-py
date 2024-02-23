# RuntimeSpecification

Runtime (version) specification that says * what assets are required/allowed to build the function * what build parameters are used * what deployment parameters are used * which dependencies are provided by the runtime

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**BuildSpec**](BuildSpec.md) |  | [optional] 
**deploy** | [**DeploySpec**](DeploySpec.md) |  | [optional] 
**language** | [**LanguageRelease**](LanguageRelease.md) |  | [optional] 
**provided_dependencies** | [**List[ProvidedDependency]**](ProvidedDependency.md) | Description of dependencies provided by this runtime version. | [optional] 
**assets** | [**AssetsConditions**](AssetsConditions.md) |  | [optional] 
**deprecated** | **bool** | If true, this runtime should no longer be used for new functions. | [optional] 

## Example

```python
from waylay.services.registry.models.runtime_specification import RuntimeSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeSpecification from a JSON string
runtime_specification_instance = RuntimeSpecification.from_json(json)
# print the JSON string representation of the object
print RuntimeSpecification.to_json()

# convert the object into a dict
runtime_specification_dict = runtime_specification_instance.to_dict()
# create an instance of RuntimeSpecification from a dict
runtime_specification_form_dict = runtime_specification.from_dict(runtime_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


