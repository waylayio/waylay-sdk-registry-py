# NamedParametersTypeofFromLegacyDocumentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**legacy_documentation** | [**LegacyPlugRequestMetadataDocumentation**](LegacyPlugRequestMetadataDocumentation.md) |  | [optional] 
**current_interface** | [**PlugInterface**](PlugInterface.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.named_parameters_typeof_from_legacy_documentation import NamedParametersTypeofFromLegacyDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of NamedParametersTypeofFromLegacyDocumentation from a JSON string
named_parameters_typeof_from_legacy_documentation_instance = NamedParametersTypeofFromLegacyDocumentation.from_json(json)
# print the JSON string representation of the object
print NamedParametersTypeofFromLegacyDocumentation.to_json()

# convert the object into a dict
named_parameters_typeof_from_legacy_documentation_dict = named_parameters_typeof_from_legacy_documentation_instance.to_dict()
# create an instance of NamedParametersTypeofFromLegacyDocumentation from a dict
named_parameters_typeof_from_legacy_documentation_form_dict = named_parameters_typeof_from_legacy_documentation.from_dict(named_parameters_typeof_from_legacy_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


