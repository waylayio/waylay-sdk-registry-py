# WebscriptLatestVersionQueryV2

Webscript latest named version query.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include_draft** | **bool** | Configures the inclusion of _draft_ versions when selecting latest versions per name. By default, draft versions are only considered when no other versions are available. If set to &#x60;true&#x60;, draft versions are **included**. If set to &#x60;false&#x60;, draft versions are **excluded**. | [optional] 
**include_deprecated** | **bool** | Configures the inclusion of _deprecated_ versions when selecting latest versions per name. By default, deprecated versions are only considered when no other versions are available. If set to &#x60;true&#x60;, deprecated versions are **included**. If set to &#x60;false&#x60;, deprecated versions are **excluded**. | [optional] 

## Example

```python
from waylay.services.registry.models.webscript_latest_version_query_v2 import WebscriptLatestVersionQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of WebscriptLatestVersionQueryV2 from a JSON string
webscript_latest_version_query_v2_instance = WebscriptLatestVersionQueryV2.from_json(json)
# print the JSON string representation of the object
print WebscriptLatestVersionQueryV2.to_json()

# convert the object into a dict
webscript_latest_version_query_v2_dict = webscript_latest_version_query_v2_instance.to_dict()
# create an instance of WebscriptLatestVersionQueryV2 from a dict
webscript_latest_version_query_v2_form_dict = webscript_latest_version_query_v2.from_dict(webscript_latest_version_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


