# InvokableWebscriptResponseEntityWebscript


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**private** | **bool** |  | 
**allow_hmac** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.invokable_webscript_response_entity_webscript import InvokableWebscriptResponseEntityWebscript

# TODO update the JSON string below
json = "{}"
# create an instance of InvokableWebscriptResponseEntityWebscript from a JSON string
invokable_webscript_response_entity_webscript_instance = InvokableWebscriptResponseEntityWebscript.from_json(json)
# print the JSON string representation of the object
print InvokableWebscriptResponseEntityWebscript.to_json()

# convert the object into a dict
invokable_webscript_response_entity_webscript_dict = invokable_webscript_response_entity_webscript_instance.to_dict()
# create an instance of InvokableWebscriptResponseEntityWebscript from a dict
invokable_webscript_response_entity_webscript_form_dict = invokable_webscript_response_entity_webscript.from_dict(invokable_webscript_response_entity_webscript_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


