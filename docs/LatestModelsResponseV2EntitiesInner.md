# LatestModelsResponseV2EntitiesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**AltVersionHALLink**](AltVersionHALLink.md) |  | 
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
**model** | [**KFServingManifest**](KFServingManifest.md) |  | 

## Example

```python
from waylay.services.registry.models.latest_models_response_v2_entities_inner import LatestModelsResponseV2EntitiesInner

# TODO update the JSON string below
json = "{}"
# create an instance of LatestModelsResponseV2EntitiesInner from a JSON string
latest_models_response_v2_entities_inner_instance = LatestModelsResponseV2EntitiesInner.from_json(json)
# print the JSON string representation of the object
print LatestModelsResponseV2EntitiesInner.to_json()

# convert the object into a dict
latest_models_response_v2_entities_inner_dict = latest_models_response_v2_entities_inner_instance.to_dict()
# create an instance of LatestModelsResponseV2EntitiesInner from a dict
latest_models_response_v2_entities_inner_form_dict = latest_models_response_v2_entities_inner.from_dict(latest_models_response_v2_entities_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


