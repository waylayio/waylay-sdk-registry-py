# PlugMeta


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

# TODO update the JSON string below
json = "{}"
# create an instance of PlugMeta from a JSON string
plug_meta_instance = PlugMeta.from_json(json)
# print the JSON string representation of the object
print PlugMeta.to_json()

# convert the object into a dict
plug_meta_dict = plug_meta_instance.to_dict()
# create an instance of PlugMeta from a dict
plug_meta_form_dict = plug_meta.from_dict(plug_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


