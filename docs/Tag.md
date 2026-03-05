# Tag

One or more tags can be assigned to a function entity to facilitate grouping and searching.

**Source:** `waylay.services.registry.models.tag`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A string that references a tag | 
**color** | **str** | Color associated with the tag in an UI. | 


## Example

```python
from waylay.services.registry.models.tag import Tag

tag = Tag(name=..., color=...)

# Create from JSON
tag = Tag.from_json('{ "name": ..., "color": ... }')

# Export to dictionary
tag_dict = tag.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


