# VerifyArgs

Input arguments for an (openfaas) deployment verification job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | [optional] 

## Example

```python
from waylay.services.registry.models.verify_args import VerifyArgs

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyArgs from a JSON string
verify_args_instance = VerifyArgs.from_json(json)
# print the JSON string representation of the object
print VerifyArgs.to_json()

# convert the object into a dict
verify_args_dict = verify_args_instance.to_dict()
# create an instance of VerifyArgs from a dict
verify_args_form_dict = verify_args.from_dict(verify_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


