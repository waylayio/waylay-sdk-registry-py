# RuntimeVersionAndPathParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wildcard** | **str** | Full path or path prefix of the asset within the archive | 
**name** | **str** |  | 
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_version_and_path_params import RuntimeVersionAndPathParams

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersionAndPathParams from a JSON string
runtime_version_and_path_params_instance = RuntimeVersionAndPathParams.from_json(json)
# print the JSON string representation of the object
print RuntimeVersionAndPathParams.to_json()

# convert the object into a dict
runtime_version_and_path_params_dict = runtime_version_and_path_params_instance.to_dict()
# create an instance of RuntimeVersionAndPathParams from a dict
runtime_version_and_path_params_form_dict = runtime_version_and_path_params.from_dict(runtime_version_and_path_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


