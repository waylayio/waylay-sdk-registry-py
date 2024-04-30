# DeployArgs

Input argument to an (openfaas) deployment job for a function.

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

# TODO update the JSON string below
json = "{}"
# create an instance of DeployArgs from a JSON string
deploy_args_instance = DeployArgs.from_json(json)
# print the JSON string representation of the object
print DeployArgs.to_json()

# convert the object into a dict
deploy_args_dict = deploy_args_instance.to_dict()
# create an instance of DeployArgs from a dict
deploy_args_form_dict = deploy_args.from_dict(deploy_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


