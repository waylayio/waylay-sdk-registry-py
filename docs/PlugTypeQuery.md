# PlugTypeQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugType**](PlugType.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.plug_type_query import PlugTypeQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PlugTypeQuery from a JSON string
plug_type_query_instance = PlugTypeQuery.from_json(json)
# print the JSON string representation of the object
print PlugTypeQuery.to_json()

# convert the object into a dict
plug_type_query_dict = plug_type_query_instance.to_dict()
# create an instance of PlugTypeQuery from a dict
plug_type_query_form_dict = plug_type_query.from_dict(plug_type_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


