# WebscriptResponseWithInvokeLinkV2


**Source:** `waylay.services.registry.models.webscript_response_with_invoke_link_v2`




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
**deprecated** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is deprecated and removed from regular listings. | 
**draft** | **bool** | If &lt;code&gt;true&lt;/code&gt; this function is a draft function and it&#39;s assets are still mutable. | 
**revision** | **str** | The revision of the function. This will be &lt;code&gt;undefined&lt;/code&gt; when the plug is not a draft. | [optional] 
**webscript** | [**WebscriptManifest**](WebscriptManifest.md) |  | 
**secret** | **str** | The secret for this webscript deployment. This is &lt;code&gt;null&lt;/code&gt; when &lt;code&gt;allowHmac&#x3D;false&lt;/code&gt; in the webscript specificaton. | [optional] 
**links** | [**InvokeHALLink**](InvokeHALLink.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.webscript_response_with_invoke_link_v2 import (
    WebscriptResponseWithInvokeLinkV2,
)

webscript_response_with_invoke_link_v2 = WebscriptResponseWithInvokeLinkV2(
    created_by=...,
    created_at=...,
    updated_by=...,
    updated_at=...,
    updates=...,
    status=...,
    failure_reason=...,
    runtime=...,
    deprecated=...,
    draft=...,
    revision=...,
    webscript=...,
    secret=...,
    links=...,
)

# Create from JSON
webscript_response_with_invoke_link_v2 = WebscriptResponseWithInvokeLinkV2.from_json(
    '{ "createdBy": ..., "createdAt": ..., "updatedBy": ..., "updatedAt": ..., "updates": ..., "status": ..., "failureReason": ..., "runtime": ..., "deprecated": ..., "draft": ..., "revision": ..., "webscript": ..., "secret": ..., "_links": ... }'
)

# Export to dictionary
webscript_response_with_invoke_link_v2_dict = (
    webscript_response_with_invoke_link_v2.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


