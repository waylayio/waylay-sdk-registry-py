# Documentation


**Source:** `waylay.services.registry.models.documentation`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**states** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug states. | [optional] 
**input** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug input parameters. | [optional] 
**output** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug response parameters. | [optional] 
**examples** | [**List[DocumentationExample]**](DocumentationExample.md) | Example scenarios for testing the plug. | [optional] 


## Example

```python
from waylay.services.registry.models.documentation import Documentation

documentation = Documentation(
    description=..., states=..., input=..., output=..., examples=...
)

# Create from JSON
documentation = Documentation.from_json(
    '{ "description": ..., "states": ..., "input": ..., "output": ..., "examples": ... }'
)

# Export to dictionary
documentation_dict = documentation.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


