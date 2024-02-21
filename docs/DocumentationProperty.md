# DocumentationProperty


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the documented property. | 
**description** | **str** | Documentation of the property. | 

## Example

```python
from waylay.services.registry.models.documentation_property import DocumentationProperty

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentationProperty from a JSON string
documentation_property_instance = DocumentationProperty.from_json(json)
# print the JSON string representation of the object
print DocumentationProperty.to_json()

# convert the object into a dict
documentation_property_dict = documentation_property_instance.to_dict()
# create an instance of DocumentationProperty from a dict
documentation_property_form_dict = documentation_property.from_dict(documentation_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


