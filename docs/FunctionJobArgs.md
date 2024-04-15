# FunctionJobArgs

Job arguments shared by all function jobs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**runtime_name** | **str** |  | 
**runtime_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**revision** | **str** | The revision hash of the current (draft) function revision | 

## Example

```python
from waylay.services.registry.models.function_job_args import FunctionJobArgs

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionJobArgs from a JSON string
function_job_args_instance = FunctionJobArgs.from_json(json)
# print the JSON string representation of the object
print FunctionJobArgs.to_json()

# convert the object into a dict
function_job_args_dict = function_job_args_instance.to_dict()
# create an instance of FunctionJobArgs from a dict
function_job_args_form_dict = function_job_args.from_dict(function_job_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


