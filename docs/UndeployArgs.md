# UndeployArgs

Input argument to an (openfaas) undeployment job for a function.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 
**is_native_plug** | **bool** | If true, the function is not expected to be deployed on openfaas. | 
**delete_entity** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.undeploy_args import UndeployArgs

# TODO update the JSON string below
json = "{}"
# create an instance of UndeployArgs from a JSON string
undeploy_args_instance = UndeployArgs.from_json(json)
# print the JSON string representation of the object
print UndeployArgs.to_json()

# convert the object into a dict
undeploy_args_dict = undeploy_args_instance.to_dict()
# create an instance of UndeployArgs from a dict
undeploy_args_form_dict = undeploy_args.from_dict(undeploy_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


