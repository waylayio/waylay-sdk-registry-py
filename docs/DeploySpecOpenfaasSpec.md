# DeploySpecOpenfaasSpec

If specified, it overrides the properties in `default`. Non-specified properties are taken from `default`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** |  | [optional] 
**image** | **str** |  | [optional] 
**namespace** | **str** |  | [optional] 
**env_process** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**env_vars** | **Dict[str, str]** |  | [optional] 
**constraints** | **List[str]** |  | [optional] 
**labels** | **Dict[str, str]** |  | [optional] 
**annotations** | **Dict[str, str]** |  | [optional] 
**secrets** | **List[str]** |  | [optional] 
**registry_auth** | **str** |  | [optional] 
**limits** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**requests** | [**ResourceLimits**](ResourceLimits.md) |  | [optional] 
**read_only_root_filesystem** | **bool** |  | [optional] 

## Example

```python
from waylay.services.registry.models.deploy_spec_openfaas_spec import DeploySpecOpenfaasSpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeploySpecOpenfaasSpec from a JSON string
deploy_spec_openfaas_spec_instance = DeploySpecOpenfaasSpec.from_json(json)
# print the JSON string representation of the object
print DeploySpecOpenfaasSpec.to_json()

# convert the object into a dict
deploy_spec_openfaas_spec_dict = deploy_spec_openfaas_spec_instance.to_dict()
# create an instance of DeploySpecOpenfaasSpec from a dict
deploy_spec_openfaas_spec_form_dict = deploy_spec_openfaas_spec.from_dict(deploy_spec_openfaas_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


