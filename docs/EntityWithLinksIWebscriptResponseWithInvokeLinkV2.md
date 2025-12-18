# EntityWithLinksIWebscriptResponseWithInvokeLinkV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**AltEmbeddedVersionIWebscriptResponseWithInvokeLinkV2**](AltEmbeddedVersionIWebscriptResponseWithInvokeLinkV2.md) |  | [optional] 
**links** | [**InvokeHALLink**](InvokeHALLink.md) |  | [optional] 
**created_by** | **str** | The user that created this entity. | 
**created_at** | **datetime** | The timestamp at which this entity was created. | 
**updated_by** | **str** | The user that last updated this entity. | 
**updated_at** | **datetime** | The timestamp at which this entity was last updated. | 
**updates** | [**List[UpdateRecord]**](UpdateRecord.md) | The audit logs corresponding to the latest modifying operations on this entity. Omitted in listing operations. | [optional] 
**status** | [**Status**](Status.md) |  | 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 
**runtime** | [**RuntimeAttributes**](RuntimeAttributes.md) |  | 
**deprecated** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is deprecated and removed from regular listings. | 
**draft** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is a draft function and it&#39;s assets are still mutable. | 
**revision** | **str** | The revision of the function. This will be &lt;code&gt;undefined&lt;/code&gt; when the plug is not a draft. | [optional] 
**webscript** | [**WebscriptManifest**](WebscriptManifest.md) |  | 
**secret** | **str** | The secret for this webscript deployment. This is &lt;code&gt;null&lt;/code&gt; when &lt;code&gt;allowHmac&#x3D;false&lt;/code&gt; in the webscript specificaton. | [optional] 

## Example

```python
from waylay.services.registry.models.entity_with_links_i_webscript_response_with_invoke_link_v2 import EntityWithLinksIWebscriptResponseWithInvokeLinkV2

# TODO update the JSON string below
json = "{}"
# create an instance of EntityWithLinksIWebscriptResponseWithInvokeLinkV2 from a JSON string
entity_with_links_i_webscript_response_with_invoke_link_v2_instance = EntityWithLinksIWebscriptResponseWithInvokeLinkV2.from_json(json)
# print the JSON string representation of the object
print EntityWithLinksIWebscriptResponseWithInvokeLinkV2.to_json()

# convert the object into a dict
entity_with_links_i_webscript_response_with_invoke_link_v2_dict = entity_with_links_i_webscript_response_with_invoke_link_v2_instance.to_dict()
# create an instance of EntityWithLinksIWebscriptResponseWithInvokeLinkV2 from a dict
entity_with_links_i_webscript_response_with_invoke_link_v2_form_dict = entity_with_links_i_webscript_response_with_invoke_link_v2.from_dict(entity_with_links_i_webscript_response_with_invoke_link_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


