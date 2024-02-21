# Model2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**HALLink**](HALLink.md) |  | [optional] 
**model** | [**HALLink**](HALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.model2 import Model2

# TODO update the JSON string below
json = "{}"
# create an instance of Model2 from a JSON string
model2_instance = Model2.from_json(json)
# print the JSON string representation of the object
print Model2.to_json()

# convert the object into a dict
model2_dict = model2_instance.to_dict()
# create an instance of Model2 from a dict
model2_form_dict = model2.from_dict(model2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


