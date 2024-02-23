# RuntimeAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | If true, the function uses a deprecated runtime. | 
**upgradable** | **bool** | If true, a newer runtime for this function is available using the &#x60;rebuild&#x60; API. | 
**name** | **str** |  | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 

## Example

```python
from waylay.services.registry.models.runtime_attributes import RuntimeAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeAttributes from a JSON string
runtime_attributes_instance = RuntimeAttributes.from_json(json)
# print the JSON string representation of the object
print RuntimeAttributes.to_json()

# convert the object into a dict
runtime_attributes_dict = runtime_attributes_instance.to_dict()
# create an instance of RuntimeAttributes from a dict
runtime_attributes_form_dict = runtime_attributes.from_dict(runtime_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


