# SchemaByIdParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**schema_id** | **str** | Schema id | 

## Example

```python
from waylay.services.registry.models.schema_by_id_params import SchemaByIdParams

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaByIdParams from a JSON string
schema_by_id_params_instance = SchemaByIdParams.from_json(json)
# print the JSON string representation of the object
print SchemaByIdParams.to_json()

# convert the object into a dict
schema_by_id_params_dict = schema_by_id_params_instance.to_dict()
# create an instance of SchemaByIdParams from a dict
schema_by_id_params_form_dict = schema_by_id_params.from_dict(schema_by_id_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


