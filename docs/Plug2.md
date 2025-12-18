# Plug2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**plug** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.plug2 import Plug2

# TODO update the JSON string below
json = "{}"
# create an instance of Plug2 from a JSON string
plug2_instance = Plug2.from_json(json)
# print the JSON string representation of the object
print Plug2.to_json()

# convert the object into a dict
plug2_dict = plug2_instance.to_dict()
# create an instance of Plug2 from a dict
plug2_form_dict = plug2.from_dict(plug2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


