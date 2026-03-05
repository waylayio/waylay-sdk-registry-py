# UpdateMetadataRequestV2


**Source:** `waylay.services.registry.models.update_metadata_request_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**author** | **str** | The author of the function. | [optional] 
**description** | **str** | A description of the function | [optional] 
**icon_url** | **str** | An url to an icon that represents this function. | [optional] 
**category** | **str** | A category for this function (Deprecated: use tags to categorise your functions) | [optional] 
**tags** | [**List[TagOrTagReference]**](TagOrTagReference.md) | During update, a (reference to a) tag - that does not yet exist, is created (using default attributes if not specified) - that does exist is not updated (even if tag attributes like &#x60;color&#x60; differ) | [optional] 


## Example

```python
from waylay.services.registry.models.update_metadata_request_v2 import (
    UpdateMetadataRequestV2,
)

update_metadata_request_v2 = UpdateMetadataRequestV2(
    author=..., description=..., icon_url=..., category=..., tags=...
)

# Create from JSON
update_metadata_request_v2 = UpdateMetadataRequestV2.from_json(
    '{ "author": ..., "description": ..., "iconURL": ..., "category": ..., "tags": ... }'
)

# Export to dictionary
update_metadata_request_v2_dict = update_metadata_request_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


