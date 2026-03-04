# DocumentationExample


**Source:** `waylay.services.registry.models.documentation_example`




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

documentation_example = DocumentationExample(
    description=..., input=..., output=..., state=...
)

# Create from JSON
documentation_example = DocumentationExample.from_json(
    '{ "description": ..., "input": ..., "output": ..., "state": ... }'
)

# Export to dictionary
documentation_example_dict = documentation_example.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


