# LegacyDocumentationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** |  | [optional] 
**supported_states** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | 
**configuration** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | 
**raw_data** | [**List[DocumentationProperty]**](DocumentationProperty.md) |  | 

## Example

```python
from waylay.services.registry.models.legacy_documentation_request import LegacyDocumentationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyDocumentationRequest from a JSON string
legacy_documentation_request_instance = LegacyDocumentationRequest.from_json(json)
# print the JSON string representation of the object
print LegacyDocumentationRequest.to_json()

# convert the object into a dict
legacy_documentation_request_dict = legacy_documentation_request_instance.to_dict()
# create an instance of LegacyDocumentationRequest from a dict
legacy_documentation_request_form_dict = legacy_documentation_request.from_dict(legacy_documentation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


