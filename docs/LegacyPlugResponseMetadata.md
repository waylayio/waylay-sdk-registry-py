# LegacyPlugResponseMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documentation** | [**LegacyDocumentation**](LegacyDocumentation.md) |  | [optional] 
**author** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**tags** | [**List[Tag]**](Tag.md) |  | [optional] 
**icon_url** | **str** |  | [optional] 
**friendly_name** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_plug_response_metadata import LegacyPlugResponseMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugResponseMetadata from a JSON string
legacy_plug_response_metadata_instance = LegacyPlugResponseMetadata.from_json(json)
# print the JSON string representation of the object
print LegacyPlugResponseMetadata.to_json()

# convert the object into a dict
legacy_plug_response_metadata_dict = legacy_plug_response_metadata_instance.to_dict()
# create an instance of LegacyPlugResponseMetadata from a dict
legacy_plug_response_metadata_form_dict = legacy_plug_response_metadata.from_dict(legacy_plug_response_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


