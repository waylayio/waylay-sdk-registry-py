# ProvidedDependency

Library dependency that is provided by this runtime.

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

# TODO update the JSON string below
json = "{}"
# create an instance of ProvidedDependency from a JSON string
provided_dependency_instance = ProvidedDependency.from_json(json)
# print the JSON string representation of the object
print ProvidedDependency.to_json()

# convert the object into a dict
provided_dependency_dict = provided_dependency_instance.to_dict()
# create an instance of ProvidedDependency from a dict
provided_dependency_form_dict = provided_dependency.from_dict(provided_dependency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


