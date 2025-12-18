# DocumentationExample


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description of the example scenario. | 
**input** | **object** | Example input values. | [optional] 
**output** | **object** | Example output values. | [optional] 
**state** | **str** | Example state value. | [optional] 

## Example

```python
from waylay.services.registry.models.documentation_example import DocumentationExample

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentationExample from a JSON string
documentation_example_instance = DocumentationExample.from_json(json)
# print the JSON string representation of the object
print DocumentationExample.to_json()

# convert the object into a dict
documentation_example_dict = documentation_example_instance.to_dict()
# create an instance of DocumentationExample from a dict
documentation_example_form_dict = documentation_example.from_dict(documentation_example_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


