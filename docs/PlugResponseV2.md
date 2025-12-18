# PlugResponseV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_by** | **str** | The user that created this entity. | 
**created_at** | **datetime** | The timestamp at which this entity was created. | 
**updated_by** | **str** | The user that last updated this entity. | 
**updated_at** | **datetime** | The timestamp at which this entity was last updated. | 
**updates** | [**List[UpdateRecord]**](UpdateRecord.md) | The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations. | [optional] 
**status** | [**Status**](Status.md) |  | 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 
**runtime** | [**RuntimeAttributes**](RuntimeAttributes.md) |  | 
**deprecated** | **bool** | If &lt;code&gt;true&lt;/code&gt; this plug is removed from regular listings, as a result of a &lt;code&gt;DELETE&lt;/code&gt; with &lt;code&gt;force&#x3D;false&lt;/code&gt;. | 
**draft** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is a draft function and it&#39;s assets are still mutable. | 
**revision** | **str** | The revision of the function. This will be &lt;code&gt;undefined&lt;/code&gt; when the plug is not a draft. | [optional] 
**plug** | [**PlugManifest**](PlugManifest.md) |  | 

## Example

```python
from waylay.services.registry.models.plug_response_v2 import PlugResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of PlugResponseV2 from a JSON string
plug_response_v2_instance = PlugResponseV2.from_json(json)
# print the JSON string representation of the object
print PlugResponseV2.to_json()

# convert the object into a dict
plug_response_v2_dict = plug_response_v2_instance.to_dict()
# create an instance of PlugResponseV2 from a dict
plug_response_v2_form_dict = plug_response_v2.from_dict(plug_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


