# ResourceLimits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory** | **str** |  | [optional] 
**cpu** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.resource_limits import ResourceLimits

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceLimits from a JSON string
resource_limits_instance = ResourceLimits.from_json(json)
# print the JSON string representation of the object
print ResourceLimits.to_json()

# convert the object into a dict
resource_limits_dict = resource_limits_instance.to_dict()
# create an instance of ResourceLimits from a dict
resource_limits_form_dict = resource_limits.from_dict(resource_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


