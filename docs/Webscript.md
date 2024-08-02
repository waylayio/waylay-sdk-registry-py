# Webscript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**webscript** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.webscript import Webscript

# TODO update the JSON string below
json = "{}"
# create an instance of Webscript from a JSON string
webscript_instance = Webscript.from_json(json)
# print the JSON string representation of the object
print Webscript.to_json()

# convert the object into a dict
webscript_dict = webscript_instance.to_dict()
# create an instance of Webscript from a dict
webscript_form_dict = webscript.from_dict(webscript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


