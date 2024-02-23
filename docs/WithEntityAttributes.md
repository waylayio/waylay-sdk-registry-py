# WithEntityAttributes


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

## Example

```python
from waylay.services.registry.models.with_entity_attributes import WithEntityAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of WithEntityAttributes from a JSON string
with_entity_attributes_instance = WithEntityAttributes.from_json(json)
# print the JSON string representation of the object
print WithEntityAttributes.to_json()

# convert the object into a dict
with_entity_attributes_dict = with_entity_attributes_instance.to_dict()
# create an instance of WithEntityAttributes from a dict
with_entity_attributes_form_dict = with_entity_attributes.from_dict(with_entity_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


