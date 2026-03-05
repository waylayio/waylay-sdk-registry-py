# BuildSpec


**Source:** `waylay.services.registry.models.build_spec`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** |  | 
**file** | **str** |  | [optional] 
**args** | **Dict[str, str]** |  | 


## Example

```python
from waylay.services.registry.models.build_spec import BuildSpec

build_spec = BuildSpec(context=..., file=..., args=...)

# Create from JSON
build_spec = BuildSpec.from_json('{ "context": ..., "file": ..., "args": ... }')

# Export to dictionary
build_spec_dict = build_spec.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


