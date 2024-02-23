# LegacyDocumentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_states** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | 
**configuration** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | 
**raw_data** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | 

## Example

```python
from waylay.services.registry.models.legacy_documentation import LegacyDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDocumentation from a JSON string
legacy_documentation_instance = LegacyDocumentation.from_json(json)
# print the JSON string representation of the object
print LegacyDocumentation.to_json()

# convert the object into a dict
legacy_documentation_dict = legacy_documentation_instance.to_dict()
# create an instance of LegacyDocumentation from a dict
legacy_documentation_form_dict = legacy_documentation.from_dict(legacy_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


