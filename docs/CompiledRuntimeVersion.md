# CompiledRuntimeVersion

Compiled build and deployment information for a runtime version. Contains all defaults applied on the _global_, _functionType_, _archiveFormat_, _runtime_ and _runtime version_ level.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | If true, this runtime should no longer be used for new functions. | 
**upgradable** | **bool** | If true, a newer runtime for this function is available using the &#x60;rebuild&#x60; API. | 
**name** | **str** |  | 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**archive_format** | [**ArchiveFormat**](ArchiveFormat.md) |  | 
**build** | [**BuildSpec**](BuildSpec.md) |  | [optional] 
**deploy** | [**DeploySpec**](DeploySpec.md) |  | [optional] 
**language** | [**LanguageRelease**](LanguageRelease.md) |  | [optional] 
**provided_dependencies** | [**List[ProvidedDependency]**](ProvidedDependency.md) | Description of dependencies provided by this runtime version. | [optional] 
**assets** | [**AssetsConditions**](AssetsConditions.md) |  | [optional] 
**invocation** | [**InvocationAttributes**](InvocationAttributes.md) |  | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.compiled_runtime_version import CompiledRuntimeVersion

# TODO update the JSON string below
json = "{}"
# create an instance of CompiledRuntimeVersion from a JSON string
compiled_runtime_version_instance = CompiledRuntimeVersion.from_json(json)
# print the JSON string representation of the object
print CompiledRuntimeVersion.to_json()

# convert the object into a dict
compiled_runtime_version_dict = compiled_runtime_version_instance.to_dict()
# create an instance of CompiledRuntimeVersion from a dict
compiled_runtime_version_form_dict = compiled_runtime_version.from_dict(compiled_runtime_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


