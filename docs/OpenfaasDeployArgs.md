# OpenfaasDeployArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**image_name** | **str** | The image name to use for deploying this function | 

## Example

```python
from waylay.services.registry.models.openfaas_deploy_args import OpenfaasDeployArgs

# TODO update the JSON string below
json = "{}"
# create an instance of OpenfaasDeployArgs from a JSON string
openfaas_deploy_args_instance = OpenfaasDeployArgs.from_json(json)
# print the JSON string representation of the object
print OpenfaasDeployArgs.to_json()

# convert the object into a dict
openfaas_deploy_args_dict = openfaas_deploy_args_instance.to_dict()
# create an instance of OpenfaasDeployArgs from a dict
openfaas_deploy_args_form_dict = openfaas_deploy_args.from_dict(openfaas_deploy_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


