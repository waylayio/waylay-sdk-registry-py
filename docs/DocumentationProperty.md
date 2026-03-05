# DocumentationProperty


**Source:** `waylay.services.registry.models.documentation_property`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the documented property. | 
**description** | **str** | Documentation of the property. | 
**examples** | **List[object]** | Example values for the property. | [optional] 


## Example

```python
from waylay.services.registry.models.documentation_property import DocumentationProperty

documentation_property = DocumentationProperty(name=..., description=..., examples=...)

# Create from JSON
documentation_property = DocumentationProperty.from_json(
    '{ "name": ..., "description": ..., "examples": ... }'
)

# Export to dictionary
documentation_property_dict = documentation_property.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


