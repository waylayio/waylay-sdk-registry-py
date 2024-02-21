# LegacyPlugRequestMetadataDocumentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**supported_states** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | [optional] 
**configuration** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | [optional] 
**raw_data** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | [optional] 
**description** | **str** |  | [optional] 
**states** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug states. | [optional] 
**input** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug input parameters. | [optional] 
**output** | [**List[DocumentationProperty]**](DocumentationProperty.md) | Documentation of the plug response parameters. | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_plug_request_metadata_documentation import LegacyPlugRequestMetadataDocumentation

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugRequestMetadataDocumentation from a JSON string
legacy_plug_request_metadata_documentation_instance = LegacyPlugRequestMetadataDocumentation.from_json(json)
# print the JSON string representation of the object
print LegacyPlugRequestMetadataDocumentation.to_json()

# convert the object into a dict
legacy_plug_request_metadata_documentation_dict = legacy_plug_request_metadata_documentation_instance.to_dict()
# create an instance of LegacyPlugRequestMetadataDocumentation from a dict
legacy_plug_request_metadata_documentation_form_dict = legacy_plug_request_metadata_documentation.from_dict(legacy_plug_request_metadata_documentation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


