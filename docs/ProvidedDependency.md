# ProvidedDependency

Library dependency that is provided by this runtime.

**Source:** `waylay.services.registry.models.provided_dependency`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of a provided dependency. | 
**title** | **str** | Optional display title. | [optional] 
**description** | **str** | Optional description. | [optional] 
**version** | **str** | Versions specification of a provided dependency | [optional] 
**deprecated** | **bool** | If true, this provided dependency is scheduled for removal (or incompatible upgrade) in a next runtime version. | [optional] [default to False]
**removed** | **bool** | If true, this dependency has been removed from the runtime (version) | [optional] [default to False]
**globals** | **List[str]** | Global variables that expose this library to the user code. As the usage of these globals is deprecated, any usage of such global will pose issues in an next runtime version. | [optional] 
**native** | **bool** | If true, the library is provided natively by the runtime: e.g. node for javascript. | [optional] 


## Example

```python
from waylay.services.registry.models.provided_dependency import ProvidedDependency

provided_dependency = ProvidedDependency(
    name=...,
    title=...,
    description=...,
    version=...,
    deprecated=...,
    removed=...,
    globals=...,
    native=...,
)

# Create from JSON
provided_dependency = ProvidedDependency.from_json(
    '{ "name": ..., "title": ..., "description": ..., "version": ..., "deprecated": ..., "removed": ..., "globals": ..., "native": ... }'
)

# Export to dictionary
provided_dependency_dict = provided_dependency.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


