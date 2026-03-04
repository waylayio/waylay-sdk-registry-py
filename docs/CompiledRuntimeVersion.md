# CompiledRuntimeVersion

Compiled build and deployment information for a runtime version. Contains all defaults applied on the _global_, _functionType_, _archiveFormat_, _runtime_ and _runtime version_ level.

**Source:** `waylay.services.registry.models.compiled_runtime_version`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | If true, this runtime should no longer be used for new functions. | 
**upgradable** | **bool** | If true, a newer runtime for this function is available using the &#x60;rebuild&#x60; API. | 
**name** | **str** | A string that references a tag | 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**archive_format** | [**ArchiveFormat**](ArchiveFormat.md) |  | 
**build** | [**BuildSpec**](BuildSpec.md) |  | [optional] 
**deploy** | [**DeploySpec**](DeploySpec.md) |  | [optional] 
**language** | [**LanguageRelease**](LanguageRelease.md) |  | [optional] 
**provided_dependencies** | [**List[ProvidedDependency]**](ProvidedDependency.md) | Description of dependencies provided by this runtime version. | [optional] 
**assets** | [**AssetsConditions**](AssetsConditions.md) |  | [optional] 
**invocation** | [**InvocationAttributes**](InvocationAttributes.md) |  | [optional] 
**tags** | **List[str]** | Tags used for grouping or filtering. | [optional] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 


## Example

```python
from waylay.services.registry.models.compiled_runtime_version import (
    CompiledRuntimeVersion,
)

compiled_runtime_version = CompiledRuntimeVersion(
    deprecated=...,
    upgradable=...,
    name=...,
    function_type=...,
    archive_format=...,
    build=...,
    deploy=...,
    language=...,
    provided_dependencies=...,
    assets=...,
    invocation=...,
    tags=...,
    title=...,
    description=...,
    version=...,
)

# Create from JSON
compiled_runtime_version = CompiledRuntimeVersion.from_json(
    '{ "deprecated": ..., "upgradable": ..., "name": ..., "functionType": ..., "archiveFormat": ..., "build": ..., "deploy": ..., "language": ..., "providedDependencies": ..., "assets": ..., "invocation": ..., "tags": ..., "title": ..., "description": ..., "version": ... }'
)

# Export to dictionary
compiled_runtime_version_dict = compiled_runtime_version.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


