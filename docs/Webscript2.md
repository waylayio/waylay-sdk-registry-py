# Webscript2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**webscript** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.webscript2 import Webscript2

# TODO update the JSON string below
json = "{}"
# create an instance of Webscript2 from a JSON string
webscript2_instance = Webscript2.from_json(json)
# print the JSON string representation of the object
print Webscript2.to_json()

# convert the object into a dict
webscript2_dict = webscript2_instance.to_dict()
# create an instance of Webscript2 from a dict
webscript2_form_dict = webscript2.from_dict(webscript2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


