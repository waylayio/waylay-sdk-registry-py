# LanguageRelease

Description of the language or framework release used by a runtime (version).

**Source:** `waylay.services.registry.models.language_release`




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

language_release = LanguageRelease(name=..., version=..., title=..., description=...)

# Create from JSON
language_release = LanguageRelease.from_json(
    '{ "name": ..., "version": ..., "title": ..., "description": ... }'
)

# Export to dictionary
language_release_dict = language_release.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


