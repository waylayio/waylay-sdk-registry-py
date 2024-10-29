# TagOrTagReference

A reference to a tag, or tag object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A string that references a tag | 
**color** | **str** | Color associated with the tag in an UI. | 

## Example

```python
from waylay.services.registry.models.tag_or_tag_reference import TagOrTagReference

# TODO update the JSON string below
json = "{}"
# create an instance of TagOrTagReference from a JSON string
tag_or_tag_reference_instance = TagOrTagReference.from_json(json)
# print the JSON string representation of the object
print TagOrTagReference.to_json()

# convert the object into a dict
tag_or_tag_reference_dict = tag_or_tag_reference_instance.to_dict()
# create an instance of TagOrTagReference from a dict
tag_or_tag_reference_form_dict = tag_or_tag_reference.from_dict(tag_or_tag_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


