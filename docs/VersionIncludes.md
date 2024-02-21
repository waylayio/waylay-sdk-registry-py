# VersionIncludes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_draft** | **bool** | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**include_deprecated** | **bool** | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 

## Example

```python
from waylay.services.registry.models.version_includes import VersionIncludes

# TODO update the JSON string below
json = "{}"
# create an instance of VersionIncludes from a JSON string
version_includes_instance = VersionIncludes.from_json(json)
# print the JSON string representation of the object
print VersionIncludes.to_json()

# convert the object into a dict
version_includes_dict = version_includes_instance.to_dict()
# create an instance of VersionIncludes from a dict
version_includes_form_dict = version_includes.from_dict(version_includes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


