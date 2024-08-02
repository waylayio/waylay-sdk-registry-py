# Plug


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**plug** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.plug import Plug

# TODO update the JSON string below
json = "{}"
# create an instance of Plug from a JSON string
plug_instance = Plug.from_json(json)
# print the JSON string representation of the object
print Plug.to_json()

# convert the object into a dict
plug_dict = plug_instance.to_dict()
# create an instance of Plug from a dict
plug_form_dict = plug.from_dict(plug_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


