# BuildArgs

Input arguments to a job that builds a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_location** | **str** | Location of the function assets. | 
**image_name** | **str** | The container image name for the target function. | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 
**args** | **Dict[str, str]** | Parameters to the runtime configuration. | 

## Example

```python
from waylay.services.registry.models.build_args import BuildArgs

# TODO update the JSON string below
json = "{}"
# create an instance of BuildArgs from a JSON string
build_args_instance = BuildArgs.from_json(json)
# print the JSON string representation of the object
print BuildArgs.to_json()

# convert the object into a dict
build_args_dict = build_args_instance.to_dict()
# create an instance of BuildArgs from a dict
build_args_form_dict = build_args.from_dict(build_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


