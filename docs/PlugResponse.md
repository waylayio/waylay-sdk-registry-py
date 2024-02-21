# PlugResponse


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
**is_deprecated** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.plug_response import PlugResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlugResponse from a JSON string
plug_response_instance = PlugResponse.from_json(json)
# print the JSON string representation of the object
print PlugResponse.to_json()

# convert the object into a dict
plug_response_dict = plug_response_instance.to_dict()
# create an instance of PlugResponse from a dict
plug_response_form_dict = plug_response.from_dict(plug_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


