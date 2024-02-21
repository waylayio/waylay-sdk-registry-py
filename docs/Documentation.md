# Documentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**states** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug states. | [optional] 
**input** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug input parameters. | [optional] 
**output** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug response parameters. | [optional] 

## Example

```python
from waylay.services.registry.models.documentation import Documentation

# TODO update the JSON string below
json = "{}"
# create an instance of Documentation from a JSON string
documentation_instance = Documentation.from_json(json)
# print the JSON string representation of the object
print Documentation.to_json()

# convert the object into a dict
documentation_dict = documentation_instance.to_dict()
# create an instance of Documentation from a dict
documentation_form_dict = documentation.from_dict(documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


