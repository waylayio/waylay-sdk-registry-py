# PatchInterfaceQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 

## Example

```python
from waylay.services.registry.models.patch_interface_query import PatchInterfaceQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PatchInterfaceQuery from a JSON string
patch_interface_query_instance = PatchInterfaceQuery.from_json(json)
# print the JSON string representation of the object
print PatchInterfaceQuery.to_json()

# convert the object into a dict
patch_interface_query_dict = patch_interface_query_instance.to_dict()
# create an instance of PatchInterfaceQuery from a dict
patch_interface_query_form_dict = patch_interface_query.from_dict(patch_interface_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


