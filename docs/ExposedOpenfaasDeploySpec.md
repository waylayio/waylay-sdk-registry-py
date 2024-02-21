# ExposedOpenfaasDeploySpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | 
**image** | **str** |  | 
**namespace** | **str** |  | 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**requests** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.exposed_openfaas_deploy_spec import ExposedOpenfaasDeploySpec

# TODO update the JSON string below
json = "{}"
# create an instance of ExposedOpenfaasDeploySpec from a JSON string
exposed_openfaas_deploy_spec_instance = ExposedOpenfaasDeploySpec.from_json(json)
# print the JSON string representation of the object
print ExposedOpenfaasDeploySpec.to_json()

# convert the object into a dict
exposed_openfaas_deploy_spec_dict = exposed_openfaas_deploy_spec_instance.to_dict()
# create an instance of ExposedOpenfaasDeploySpec from a dict
exposed_openfaas_deploy_spec_form_dict = exposed_openfaas_deploy_spec.from_dict(exposed_openfaas_deploy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


