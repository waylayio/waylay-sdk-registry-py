# OpenfaasFunctionRef


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 

## Example

```python
from waylay.services.registry.models.openfaas_function_ref import OpenfaasFunctionRef

# TODO update the JSON string below
json = "{}"
# create an instance of OpenfaasFunctionRef from a JSON string
openfaas_function_ref_instance = OpenfaasFunctionRef.from_json(json)
# print the JSON string representation of the object
print OpenfaasFunctionRef.to_json()

# convert the object into a dict
openfaas_function_ref_dict = openfaas_function_ref_instance.to_dict()
# create an instance of OpenfaasFunctionRef from a dict
openfaas_function_ref_form_dict = openfaas_function_ref.from_dict(openfaas_function_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


