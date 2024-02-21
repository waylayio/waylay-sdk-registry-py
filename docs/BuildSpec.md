# BuildSpec


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | 
**args** | **Dict[str, str]** |  | 

## Example

```python
from waylay.services.registry.models.build_spec import BuildSpec

# TODO update the JSON string below
json = "{}"
# create an instance of BuildSpec from a JSON string
build_spec_instance = BuildSpec.from_json(json)
# print the JSON string representation of the object
print BuildSpec.to_json()

# convert the object into a dict
build_spec_dict = build_spec_instance.to_dict()
# create an instance of BuildSpec from a dict
build_spec_form_dict = build_spec.from_dict(build_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


