# UpdateTagsRequestV2


**Source:** `waylay.services.registry.models.update_tags_request_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[TagOrTagReference]**](TagOrTagReference.md) | During update, a (reference to a) tag - that does not yet exist, is created (using default attributes if not specified) - that does exist is **not** updated (even if tag attributes like &#x60;color&#x60; differ) | 


## Example

```python
from waylay.services.registry.models.update_tags_request_v2 import UpdateTagsRequestV2

update_tags_request_v2 = UpdateTagsRequestV2(tags=...)

# Create from JSON
update_tags_request_v2 = UpdateTagsRequestV2.from_json('{ "tags": ... }')

# Export to dictionary
update_tags_request_v2_dict = update_tags_request_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


