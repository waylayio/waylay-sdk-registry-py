# RootPageResponse

Status Page

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the service. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**enabled** | **object** | Description of the features enabled on this service deployment. | 
**revision** | **str** | Revision of the service source code. | 

## Example

```python
from waylay.services.registry.models.root_page_response import RootPageResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RootPageResponse from a JSON string
root_page_response_instance = RootPageResponse.from_json(json)
# print the JSON string representation of the object
print RootPageResponse.to_json()

# convert the object into a dict
root_page_response_dict = root_page_response_instance.to_dict()
# create an instance of RootPageResponse from a dict
root_page_response_form_dict = root_page_response.from_dict(root_page_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


