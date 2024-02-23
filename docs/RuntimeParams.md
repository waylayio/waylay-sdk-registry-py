# RuntimeParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 

## Example

```python
from waylay.services.registry.models.runtime_params import RuntimeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeParams from a JSON string
runtime_params_instance = RuntimeParams.from_json(json)
# print the JSON string representation of the object
print RuntimeParams.to_json()

# convert the object into a dict
runtime_params_dict = runtime_params_instance.to_dict()
# create an instance of RuntimeParams from a dict
runtime_params_form_dict = runtime_params.from_dict(runtime_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


