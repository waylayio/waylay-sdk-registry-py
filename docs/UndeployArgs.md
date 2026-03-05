# UndeployArgs

Input argument to an (openfaas) undeployment job for a function.

**Source:** `waylay.services.registry.models.undeploy_args`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_location** | **str** | Location of the function assets. | 
**image_name** | **str** | The container image name for the target function. | 
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 
**delete_entity** | **bool** |  | 
**reset_entity** | **bool** |  | 
**delete_image** | **bool** |  | 


## Example

```python
from waylay.services.registry.models.undeploy_args import UndeployArgs

undeploy_args = UndeployArgs(
    storage_location=...,
    image_name=...,
    namespace=...,
    endpoint=...,
    runtime_name=...,
    runtime_version=...,
    revision=...,
    delete_entity=...,
    reset_entity=...,
    delete_image=...,
)

# Create from JSON
undeploy_args = UndeployArgs.from_json(
    '{ "storageLocation": ..., "imageName": ..., "namespace": ..., "endpoint": ..., "runtimeName": ..., "runtimeVersion": ..., "revision": ..., "deleteEntity": ..., "resetEntity": ..., "deleteImage": ... }'
)

# Export to dictionary
undeploy_args_dict = undeploy_args.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


