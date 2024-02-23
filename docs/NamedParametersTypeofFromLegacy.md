# NamedParametersTypeofFromLegacy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**LegacyPlugMetaRequest**](LegacyPlugMetaRequest.md) |  | 
**current_interface** | [**PlugInterface**](PlugInterface.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.named_parameters_typeof_from_legacy import NamedParametersTypeofFromLegacy

# TODO update the JSON string below
json = "{}"
# create an instance of NamedParametersTypeofFromLegacy from a JSON string
named_parameters_typeof_from_legacy_instance = NamedParametersTypeofFromLegacy.from_json(json)
# print the JSON string representation of the object
print NamedParametersTypeofFromLegacy.to_json()

# convert the object into a dict
named_parameters_typeof_from_legacy_dict = named_parameters_typeof_from_legacy_instance.to_dict()
# create an instance of NamedParametersTypeofFromLegacy from a dict
named_parameters_typeof_from_legacy_form_dict = named_parameters_typeof_from_legacy.from_dict(named_parameters_typeof_from_legacy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


