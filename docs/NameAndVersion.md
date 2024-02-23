# NameAndVersion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.name_and_version import NameAndVersion

# TODO update the JSON string below
json = "{}"
# create an instance of NameAndVersion from a JSON string
name_and_version_instance = NameAndVersion.from_json(json)
# print the JSON string representation of the object
print NameAndVersion.to_json()

# convert the object into a dict
name_and_version_dict = name_and_version_instance.to_dict()
# create an instance of NameAndVersion from a dict
name_and_version_form_dict = name_and_version.from_dict(name_and_version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


