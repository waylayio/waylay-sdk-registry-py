# SchemaParams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**role** | [**AssetRole**](AssetRole.md) |  | 

## Example

```python
from waylay.services.registry.models.schema_params import SchemaParams

# TODO update the JSON string below
json = "{}"
# create an instance of SchemaParams from a JSON string
schema_params_instance = SchemaParams.from_json(json)
# print the JSON string representation of the object
print SchemaParams.to_json()

# convert the object into a dict
schema_params_dict = schema_params_instance.to_dict()
# create an instance of SchemaParams from a dict
schema_params_form_dict = schema_params.from_dict(schema_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


