# Webscript1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**webscript** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.webscript1 import Webscript1

# TODO update the JSON string below
json = "{}"
# create an instance of Webscript1 from a JSON string
webscript1_instance = Webscript1.from_json(json)
# print the JSON string representation of the object
print Webscript1.to_json()

# convert the object into a dict
webscript1_dict = webscript1_instance.to_dict()
# create an instance of Webscript1 from a dict
webscript1_form_dict = webscript1.from_dict(webscript1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


