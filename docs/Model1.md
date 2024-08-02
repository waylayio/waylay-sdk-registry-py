# Model1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**HALLinks**](HALLinks.md) |  | [optional] 
**model** | [**HALLinks**](HALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.model1 import Model1

# TODO update the JSON string below
json = "{}"
# create an instance of Model1 from a JSON string
model1_instance = Model1.from_json(json)
# print the JSON string representation of the object
print Model1.to_json()

# convert the object into a dict
model1_dict = model1_instance.to_dict()
# create an instance of Model1 from a dict
model1_form_dict = model1.from_dict(model1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


