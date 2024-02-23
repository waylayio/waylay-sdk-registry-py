# SemanticVersionRange

A range of semantic versions. See https://devhints.io/semver

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange

# TODO update the JSON string below
json = "{}"
# create an instance of SemanticVersionRange from a JSON string
semantic_version_range_instance = SemanticVersionRange.from_json(json)
# print the JSON string representation of the object
print SemanticVersionRange.to_json()

# convert the object into a dict
semantic_version_range_dict = semantic_version_range_instance.to_dict()
# create an instance of SemanticVersionRange from a dict
semantic_version_range_form_dict = semantic_version_range.from_dict(semantic_version_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


