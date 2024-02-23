# LegacyPlugRequestMetadataDocumentationAnyOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_states** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | [optional] 
**configuration** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | [optional] 
**raw_data** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_plug_request_metadata_documentation_any_of import LegacyPlugRequestMetadataDocumentationAnyOf

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugRequestMetadataDocumentationAnyOf from a JSON string
legacy_plug_request_metadata_documentation_any_of_instance = LegacyPlugRequestMetadataDocumentationAnyOf.from_json(json)
# print the JSON string representation of the object
print LegacyPlugRequestMetadataDocumentationAnyOf.to_json()

# convert the object into a dict
legacy_plug_request_metadata_documentation_any_of_dict = legacy_plug_request_metadata_documentation_any_of_instance.to_dict()
# create an instance of LegacyPlugRequestMetadataDocumentationAnyOf from a dict
legacy_plug_request_metadata_documentation_any_of_form_dict = legacy_plug_request_metadata_documentation_any_of.from_dict(legacy_plug_request_metadata_documentation_any_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


