# RuntimeTag


**Source:** `waylay.services.registry.models.runtime_tag`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A string that references a tag | 
**color** | **str** | Color associated with the tag in an UI. | 
**description** | **str** | Description of the tag | [optional] 


## Example

```python
from waylay.services.registry.models.runtime_tag import RuntimeTag

runtime_tag = RuntimeTag(name=..., color=..., description=...)

# Create from JSON
runtime_tag = RuntimeTag.from_json('{ "name": ..., "color": ..., "description": ... }')

# Export to dictionary
runtime_tag_dict = runtime_tag.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


