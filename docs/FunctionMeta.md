# FunctionMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The author of the function. | [optional] 
**description** | **str** | A description of the function | [optional] 
**icon_url** | **str** | An url to an icon that represents this function. | [optional] 
**category** | **str** | A category for this function (Deprecated: use tags to categorise your functions) | [optional] 

## Example

```python
from waylay.services.registry.models.function_meta import FunctionMeta

# TODO update the JSON string below
json = "{}"
# create an instance of FunctionMeta from a JSON string
function_meta_instance = FunctionMeta.from_json(json)
# print the JSON string representation of the object
print FunctionMeta.to_json()

# convert the object into a dict
function_meta_dict = function_meta_instance.to_dict()
# create an instance of FunctionMeta from a dict
function_meta_form_dict = function_meta.from_dict(function_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


