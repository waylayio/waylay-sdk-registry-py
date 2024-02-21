# RuntimeVersionSpecification


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**BuildSpec**](BuildSpec.md) |  | [optional] 
**deploy** | [**DeploySpec**](DeploySpec.md) |  | [optional] 
**language** | [**LanguageRelease**](LanguageRelease.md) |  | [optional] 
**provided_dependencies** | [**List[ProvidedDependency]**](ProvidedDependency.md) | Description of dependencies provided by this runtime version. | [optional] 
**assets** | [**AssetsConditions**](AssetsConditions.md) |  | [optional] 
**deprecated** | **bool** | If true, this runtime should no longer be used for new functions. | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.runtime_version_specification import RuntimeVersionSpecification

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersionSpecification from a JSON string
runtime_version_specification_instance = RuntimeVersionSpecification.from_json(json)
# print the JSON string representation of the object
print RuntimeVersionSpecification.to_json()

# convert the object into a dict
runtime_version_specification_dict = runtime_version_specification_instance.to_dict()
# create an instance of RuntimeVersionSpecification from a dict
runtime_version_specification_form_dict = runtime_version_specification.from_dict(runtime_version_specification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


