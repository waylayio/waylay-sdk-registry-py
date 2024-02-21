# AnyFunctionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The user that created this entity. | 
**created_at** | **datetime** | The timestamp at which this entity was created. | 
**updated_by** | **str** | The user that last updated this entity. | 
**updated_at** | **datetime** | The timestamp at which this entity was last updated. | 
**updates** | [**List[UpdateRecord]**](UpdateRecord.md) | The audit logs corresponding to the latest modifying operations on this entity. | 
**status** | [**Status**](Status.md) |  | 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 
**runtime** | [**RuntimeAttributes**](RuntimeAttributes.md) |  | 
**deprecated** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is deprecated and removed from regular listings. | 
**draft** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is a draft function and it&#39;s assets are still mutable. | 
**plug** | [**PlugManifest**](PlugManifest.md) |  | 
**model** | [**KFServingManifest**](KFServingManifest.md) |  | 
**webscript** | [**WebscriptManifest**](WebscriptManifest.md) |  | 
**secret** | **str** | The secret for this webscript deployment. This is &lt;code&gt;null&lt;/code&gt; when &lt;code&gt;allowHmac&#x3D;false&lt;/code&gt; in the webscript specificaton. | [optional] 

## Example

```python
from waylay.services.registry.models.any_function_response import AnyFunctionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AnyFunctionResponse from a JSON string
any_function_response_instance = AnyFunctionResponse.from_json(json)
# print the JSON string representation of the object
print AnyFunctionResponse.to_json()

# convert the object into a dict
any_function_response_dict = any_function_response_instance.to_dict()
# create an instance of AnyFunctionResponse from a dict
any_function_response_form_dict = any_function_response.from_dict(any_function_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


