# PlugMeta


**Source:** `waylay.services.registry.models.plug_meta`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The author of the function. | [optional] 
**description** | **str** | A description of the function | [optional] 
**icon_url** | **str** | An url to an icon that represents this function. | [optional] 
**category** | **str** | A category for this function (Deprecated: use tags to categorise your functions) | [optional] 
**documentation_url** | **str** | External url that document this function. | [optional] 
**friendly_name** | **str** | Display title for this function. | [optional] 
**tags** | [**List[TagOrTagReference]**](TagOrTagReference.md) | Tag references or tag objects associated with this function. See &#x60;showTags&#x60; query parameter on how referenced tags are displayed. During update, a (reference to a) tag - that does not yet exist, is created (using default attributes if not specified) - that does exist is not updated (even if tag attributes like &#x60;color&#x60; differ) | [optional] 
**documentation** | [**Documentation**](Documentation.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.plug_meta import PlugMeta

plug_meta = PlugMeta(
    author=...,
    description=...,
    icon_url=...,
    category=...,
    documentation_url=...,
    friendly_name=...,
    tags=...,
    documentation=...,
)

# Create from JSON
plug_meta = PlugMeta.from_json(
    '{ "author": ..., "description": ..., "iconURL": ..., "category": ..., "documentationURL": ..., "friendlyName": ..., "tags": ..., "documentation": ... }'
)

# Export to dictionary
plug_meta_dict = plug_meta.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


