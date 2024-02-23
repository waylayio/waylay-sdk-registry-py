# LegacyPlugRequestMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**required_properties** | [**List[LegacyRequiredPropertiesInner]**](LegacyRequiredPropertiesInner.md) |  | [optional] 
**supported_states** | **List[str]** |  | [optional] 
**raw_data** | [**List[LegacyPlugRequestMetadataRawDataInner]**](LegacyPlugRequestMetadataRawDataInner.md) |  | [optional] 
**configuration** | [**List[LegacyConfigurationObject]**](LegacyConfigurationObject.md) |  | [optional] 
**author** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**documentation** | [**LegacyPlugRequestMetadataDocumentation**](LegacyPlugRequestMetadataDocumentation.md) |  | [optional] 
**documentation_url** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_plug_request_metadata import LegacyPlugRequestMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugRequestMetadata from a JSON string
legacy_plug_request_metadata_instance = LegacyPlugRequestMetadata.from_json(json)
# print the JSON string representation of the object
print LegacyPlugRequestMetadata.to_json()

# convert the object into a dict
legacy_plug_request_metadata_dict = legacy_plug_request_metadata_instance.to_dict()
# create an instance of LegacyPlugRequestMetadata from a dict
legacy_plug_request_metadata_form_dict = legacy_plug_request_metadata.from_dict(legacy_plug_request_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


