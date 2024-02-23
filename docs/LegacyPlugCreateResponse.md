# LegacyPlugCreateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status_code** | **float** |  | 
**uri** | **str** |  | 
**entity** | [**LegacyPlugScriptResponse**](LegacyPlugScriptResponse.md) |  | 

## Example

```python
from waylay.services.registry.models.legacy_plug_create_response import LegacyPlugCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugCreateResponse from a JSON string
legacy_plug_create_response_instance = LegacyPlugCreateResponse.from_json(json)
# print the JSON string representation of the object
print LegacyPlugCreateResponse.to_json()

# convert the object into a dict
legacy_plug_create_response_dict = legacy_plug_create_response_instance.to_dict()
# create an instance of LegacyPlugCreateResponse from a dict
legacy_plug_create_response_form_dict = legacy_plug_create_response.from_dict(legacy_plug_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


