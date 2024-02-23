# WithLimit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The page size used for this query result. | [optional] 

## Example

```python
from waylay.services.registry.models.with_limit import WithLimit

# TODO update the JSON string below
json = "{}"
# create an instance of WithLimit from a JSON string
with_limit_instance = WithLimit.from_json(json)
# print the JSON string representation of the object
print WithLimit.to_json()

# convert the object into a dict
with_limit_dict = with_limit_instance.to_dict()
# create an instance of WithLimit from a dict
with_limit_form_dict = with_limit.from_dict(with_limit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


