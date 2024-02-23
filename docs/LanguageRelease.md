# LanguageRelease

Description of the language or framework release used by a runtime (version).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Short technical name of the language or framework used. | 
**version** | **str** | Release version of the language or framework. | 
**title** | **str** | Display title. | 
**description** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.language_release import LanguageRelease

# TODO update the JSON string below
json = "{}"
# create an instance of LanguageRelease from a JSON string
language_release_instance = LanguageRelease.from_json(json)
# print the JSON string representation of the object
print LanguageRelease.to_json()

# convert the object into a dict
language_release_dict = language_release_instance.to_dict()
# create an instance of LanguageRelease from a dict
language_release_form_dict = language_release.from_dict(language_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


