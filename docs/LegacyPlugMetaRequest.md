# LegacyPlugMetaRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from waylay.services.registry.models.legacy_plug_meta_request import LegacyPlugMetaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugMetaRequest from a JSON string
legacy_plug_meta_request_instance = LegacyPlugMetaRequest.from_json(json)
# print the JSON string representation of the object
print LegacyPlugMetaRequest.to_json()

# convert the object into a dict
legacy_plug_meta_request_dict = legacy_plug_meta_request_instance.to_dict()
# create an instance of LegacyPlugMetaRequest from a dict
legacy_plug_meta_request_form_dict = legacy_plug_meta_request.from_dict(legacy_plug_meta_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


