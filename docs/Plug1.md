# Plug1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**HALLinks**](HALLinks.md) |  | [optional] 
**plug** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.plug1 import Plug1

# TODO update the JSON string below
json = "{}"
# create an instance of Plug1 from a JSON string
plug1_instance = Plug1.from_json(json)
# print the JSON string representation of the object
print Plug1.to_json()

# convert the object into a dict
plug1_dict = plug1_instance.to_dict()
# create an instance of Plug1 from a dict
plug1_form_dict = plug1.from_dict(plug1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


