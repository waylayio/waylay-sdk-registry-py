# FunctionRef


**Source:** `waylay.services.registry.models.function_ref`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**name** | **str** | The logical name for the function. | 
**version** | **str** | The semantic version of the function (all versions if undefined) | [optional] 
**runtime** | **str** |  | [optional] 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | [optional] 


## Example

```python
from waylay.services.registry.models.function_ref import FunctionRef

function_ref = FunctionRef(
    function_type=..., name=..., version=..., runtime=..., runtime_version=...
)

# Create from JSON
function_ref = FunctionRef.from_json(
    '{ "functionType": ..., "name": ..., "version": ..., "runtime": ..., "runtimeVersion": ... }'
)

# Export to dictionary
function_ref_dict = function_ref.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


