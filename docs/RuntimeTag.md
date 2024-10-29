# RuntimeTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A string that references a tag | 
**color** | **str** | Color associated with the tag in an UI. | 
**description** | **str** | Description of the tag | [optional] 

## Example

```python
from waylay.services.registry.models.runtime_tag import RuntimeTag

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeTag from a JSON string
runtime_tag_instance = RuntimeTag.from_json(json)
# print the JSON string representation of the object
print RuntimeTag.to_json()

# convert the object into a dict
runtime_tag_dict = runtime_tag_instance.to_dict()
# create an instance of RuntimeTag from a dict
runtime_tag_form_dict = runtime_tag.from_dict(runtime_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


