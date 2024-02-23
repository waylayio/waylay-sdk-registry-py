# WebscriptResponse

Successful Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 
**name** | **str** | The logical name for the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**runtime** | **str** |  | 
**runtime_version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**metadata** | [**FunctionMeta**](FunctionMeta.md) |  | 
**created_by** | **str** | The user that created this entity. | 
**created_at** | **datetime** | The timestamp at which this entity was created. | 
**updated_by** | **str** | The user that last updated this entity. | 
**updated_at** | **datetime** | The timestamp at which this entity was last updated. | 
**status** | [**Status**](Status.md) |  | 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 
**links** | [**List[JobHALLinks]**](JobHALLinks.md) | Links to related entities. | [optional] 
**secret** | **str** |  | 

## Example

```python
from waylay.services.registry.models.webscript_response import WebscriptResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WebscriptResponse from a JSON string
webscript_response_instance = WebscriptResponse.from_json(json)
# print the JSON string representation of the object
print WebscriptResponse.to_json()

# convert the object into a dict
webscript_response_dict = webscript_response_instance.to_dict()
# create an instance of WebscriptResponse from a dict
webscript_response_form_dict = webscript_response.from_dict(webscript_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


