# UserPlugMeta

Plug metadata that the user can update as `metadata`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The author of the function. | [optional] 
**description** | **str** | A description of the function | [optional] 
**icon_url** | **str** | An url to an icon that represents this function. | [optional] 
**category** | **str** | A category for this function (Deprecated: use tags to categorise your functions) | [optional] 
**documentation_url** | **str** | External url that document this function. | [optional] 
**tags** | [**List[Tag]**](Tag.md) | Tags associated with this function. | [optional] 
**friendly_name** | **str** | Display title for this function. | [optional] 

## Example

```python
from waylay.services.registry.models.user_plug_meta import UserPlugMeta

# TODO update the JSON string below
json = "{}"
# create an instance of UserPlugMeta from a JSON string
user_plug_meta_instance = UserPlugMeta.from_json(json)
# print the JSON string representation of the object
print UserPlugMeta.to_json()

# convert the object into a dict
user_plug_meta_dict = user_plug_meta_instance.to_dict()
# create an instance of UserPlugMeta from a dict
user_plug_meta_form_dict = user_plug_meta.from_dict(user_plug_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


