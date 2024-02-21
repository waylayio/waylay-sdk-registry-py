# FunctionNameVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The logical name for the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.function_name_version import FunctionNameVersion

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionNameVersion from a JSON string
function_name_version_instance = FunctionNameVersion.from_json(json)
# print the JSON string representation of the object
print FunctionNameVersion.to_json()

# convert the object into a dict
function_name_version_dict = function_name_version_instance.to_dict()
# create an instance of FunctionNameVersion from a dict
function_name_version_form_dict = function_name_version.from_dict(function_name_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


