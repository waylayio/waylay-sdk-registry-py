# DeploySpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**openfaas_spec** | [**DeploySpecOpenfaasSpec**](DeploySpecOpenfaasSpec.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.deploy_spec import DeploySpec

# TODO update the JSON string below
json = "{}"
# create an instance of DeploySpec from a JSON string
deploy_spec_instance = DeploySpec.from_json(json)
# print the JSON string representation of the object
print DeploySpec.to_json()

# convert the object into a dict
deploy_spec_dict = deploy_spec_instance.to_dict()
# create an instance of DeploySpec from a dict
deploy_spec_form_dict = deploy_spec.from_dict(deploy_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


