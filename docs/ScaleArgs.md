# ScaleArgs

Input argument to an (openfaas) scale job for a function.

**Source:** `waylay.services.registry.models.scale_args`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 
**replicas** | **float** | Number of target replicas | 


## Example

```python
from waylay.services.registry.models.scale_args import ScaleArgs

scale_args = ScaleArgs(
    namespace=...,
    endpoint=...,
    runtime_name=...,
    runtime_version=...,
    revision=...,
    replicas=...,
)

# Create from JSON
scale_args = ScaleArgs.from_json(
    '{ "namespace": ..., "endpoint": ..., "runtimeName": ..., "runtimeVersion": ..., "revision": ..., "replicas": ... }'
)

# Export to dictionary
scale_args_dict = scale_args.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


