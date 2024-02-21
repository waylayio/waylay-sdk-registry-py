# FunctionRef


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

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionRef from a JSON string
function_ref_instance = FunctionRef.from_json(json)
# print the JSON string representation of the object
print FunctionRef.to_json()

# convert the object into a dict
function_ref_dict = function_ref_instance.to_dict()
# create an instance of FunctionRef from a dict
function_ref_form_dict = function_ref.from_dict(function_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


