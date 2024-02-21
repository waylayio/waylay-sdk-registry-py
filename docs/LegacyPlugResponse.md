# LegacyPlugResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**author** | **str** |  | [optional] 
**category** | **str** |  | [optional] 
**icon_url** | **str** |  | [optional] 
**documentation_url** | **str** |  | [optional] 
**is_deprecated** | **bool** |  | 
**description** | **str** |  | [optional] 
**states** | **List[str]** |  | [optional] 
**raw_data** | **List[object]** |  | [optional] 
**media_type** | [**MediaType**](MediaType.md) |  | 
**configuration** | [**List[LegacyConfigurationResponseObject]**](LegacyConfigurationResponseObject.md) |  | [optional] 
**commands** | **List[str]** |  | 
**status** | [**Status**](Status.md) |  | 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 
**metadata** | [**LegacyPlugResponseMetadata**](LegacyPlugResponseMetadata.md) |  | 

## Example

```python
from waylay.services.registry.models.legacy_plug_response import LegacyPlugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugResponse from a JSON string
legacy_plug_response_instance = LegacyPlugResponse.from_json(json)
# print the JSON string representation of the object
print LegacyPlugResponse.to_json()

# convert the object into a dict
legacy_plug_response_dict = legacy_plug_response_instance.to_dict()
# create an instance of LegacyPlugResponse from a dict
legacy_plug_response_form_dict = legacy_plug_response.from_dict(legacy_plug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


