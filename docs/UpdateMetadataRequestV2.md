# UpdateMetadataRequestV2


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
from waylay.services.registry.models.update_metadata_request_v2 import UpdateMetadataRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateMetadataRequestV2 from a JSON string
update_metadata_request_v2_instance = UpdateMetadataRequestV2.from_json(json)
# print the JSON string representation of the object
print UpdateMetadataRequestV2.to_json()

# convert the object into a dict
update_metadata_request_v2_dict = update_metadata_request_v2_instance.to_dict()
# create an instance of UpdateMetadataRequestV2 from a dict
update_metadata_request_v2_form_dict = update_metadata_request_v2.from_dict(update_metadata_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


