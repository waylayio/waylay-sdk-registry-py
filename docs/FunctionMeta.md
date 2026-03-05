# FunctionMeta


**Source:** `waylay.services.registry.models.function_meta`




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

function_meta = FunctionMeta(author=..., description=..., icon_url=..., category=...)

# Create from JSON
function_meta = FunctionMeta.from_json(
    '{ "author": ..., "description": ..., "iconURL": ..., "category": ... }'
)

# Export to dictionary
function_meta_dict = function_meta.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


