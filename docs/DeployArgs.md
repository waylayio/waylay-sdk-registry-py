# DeployArgs

Input argument to an (openfaas) deployment job for a function.

**Source:** `waylay.services.registry.models.deploy_args`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**image_name** | **str** | The image name to use for deploying this function | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 
**deploy_spec_overrides** | [**DeployArgsDeploySpecOverrides**](DeployArgsDeploySpecOverrides.md) |  | 


## Example

```python
from waylay.services.registry.models.deploy_args import DeployArgs

deploy_args = DeployArgs(
    namespace=...,
    endpoint=...,
    image_name=...,
    runtime_name=...,
    runtime_version=...,
    revision=...,
    deploy_spec_overrides=...,
)

# Create from JSON
deploy_args = DeployArgs.from_json(
    '{ "namespace": ..., "endpoint": ..., "imageName": ..., "runtimeName": ..., "runtimeVersion": ..., "revision": ..., "deploySpecOverrides": ... }'
)

# Export to dictionary
deploy_args_dict = deploy_args.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


