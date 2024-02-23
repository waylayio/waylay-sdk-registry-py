# BuildResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | SHA digest of the built image. | 
**log** | **List[str]** | Detailed logs of the build steps. | [optional] 
**status** | **str** | Outcome of the build. | [optional] 

## Example

```python
from waylay.services.registry.models.build_result import BuildResult

# TODO update the JSON string below
json = "{}"
# create an instance of BuildResult from a JSON string
build_result_instance = BuildResult.from_json(json)
# print the JSON string representation of the object
print BuildResult.to_json()

# convert the object into a dict
build_result_dict = build_result_instance.to_dict()
# create an instance of BuildResult from a dict
build_result_form_dict = build_result.from_dict(build_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


