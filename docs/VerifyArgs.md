# VerifyArgs

Input arguments for an (openfaas) deployment verification job.

**Source:** `waylay.services.registry.models.verify_args`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**namespace** | **str** | The (openfaas) namespace for the target function. | 
**endpoint** | **str** | The (openfaas) endpoint service name | 
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 


## Example

```python
from waylay.services.registry.models.verify_args import VerifyArgs

verify_args = VerifyArgs(
    namespace=..., endpoint=..., runtime_name=..., runtime_version=..., revision=...
)

# Create from JSON
verify_args = VerifyArgs.from_json(
    '{ "namespace": ..., "endpoint": ..., "runtimeName": ..., "runtimeVersion": ..., "revision": ... }'
)

# Export to dictionary
verify_args_dict = verify_args.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


