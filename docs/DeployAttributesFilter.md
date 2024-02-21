# DeployAttributesFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | Filter on the openfaas endpoint. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**image_name** | **str** | Filter on the container image name. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 
**storage_location** | **str** | Filter on the storageLocation. This is case-insensitive and supports wild-cards &#x60;?&#x60; (any one character) and &#x60;*&#x60; (any sequence of characters). | [optional] 

## Example

```python
from waylay.services.registry.models.deploy_attributes_filter import DeployAttributesFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DeployAttributesFilter from a JSON string
deploy_attributes_filter_instance = DeployAttributesFilter.from_json(json)
# print the JSON string representation of the object
print DeployAttributesFilter.to_json()

# convert the object into a dict
deploy_attributes_filter_dict = deploy_attributes_filter_instance.to_dict()
# create an instance of DeployAttributesFilter from a dict
deploy_attributes_filter_form_dict = deploy_attributes_filter.from_dict(deploy_attributes_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


