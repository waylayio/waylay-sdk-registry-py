# ProtectByNameResponseV2

Protection changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**versions** | **List[str]** | The versions that were protected or unprotected. | 

## Example

```python
from waylay.services.registry.models.protect_by_name_response_v2 import ProtectByNameResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectByNameResponseV2 from a JSON string
protect_by_name_response_v2_instance = ProtectByNameResponseV2.from_json(json)
# print the JSON string representation of the object
print ProtectByNameResponseV2.to_json()

# convert the object into a dict
protect_by_name_response_v2_dict = protect_by_name_response_v2_instance.to_dict()
# create an instance of ProtectByNameResponseV2 from a dict
protect_by_name_response_v2_form_dict = protect_by_name_response_v2.from_dict(protect_by_name_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


