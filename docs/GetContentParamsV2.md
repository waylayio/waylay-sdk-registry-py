# GetContentParamsV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wildcard** | **str** | Full path or path prefix of the asset within the archive | 
**name** | **str** | The name of the function. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.get_content_params_v2 import GetContentParamsV2

# TODO update the JSON string below
json = "{}"
# create an instance of GetContentParamsV2 from a JSON string
get_content_params_v2_instance = GetContentParamsV2.from_json(json)
# print the JSON string representation of the object
print GetContentParamsV2.to_json()

# convert the object into a dict
get_content_params_v2_dict = get_content_params_v2_instance.to_dict()
# create an instance of GetContentParamsV2 from a dict
get_content_params_v2_form_dict = get_content_params_v2.from_dict(get_content_params_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


