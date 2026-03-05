# BuildArgs

Input arguments to a job that builds a function.

**Source:** `waylay.services.registry.models.build_args`




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

build_args = BuildArgs(
    storage_location=...,
    image_name=...,
    runtime_name=...,
    runtime_version=...,
    revision=...,
    args=...,
)

# Create from JSON
build_args = BuildArgs.from_json(
    '{ "storageLocation": ..., "imageName": ..., "runtimeName": ..., "runtimeVersion": ..., "revision": ..., "args": ... }'
)

# Export to dictionary
build_args_dict = build_args.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


