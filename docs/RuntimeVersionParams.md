# RuntimeVersionParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_version_params import RuntimeVersionParams

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersionParams from a JSON string
runtime_version_params_instance = RuntimeVersionParams.from_json(json)
# print the JSON string representation of the object
print RuntimeVersionParams.to_json()

# convert the object into a dict
runtime_version_params_dict = runtime_version_params_instance.to_dict()
# create an instance of RuntimeVersionParams from a dict
runtime_version_params_form_dict = runtime_version_params.from_dict(runtime_version_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


