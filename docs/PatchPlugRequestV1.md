# PatchPlugRequestV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**UserPlugMeta**](UserPlugMeta.md) |  | 

## Example

```python
from waylay.services.registry.models.patch_plug_request_v1 import PatchPlugRequestV1

# TODO update the JSON string below
json = "{}"
# create an instance of PatchPlugRequestV1 from a JSON string
patch_plug_request_v1_instance = PatchPlugRequestV1.from_json(json)
# print the JSON string representation of the object
print PatchPlugRequestV1.to_json()

# convert the object into a dict
patch_plug_request_v1_dict = patch_plug_request_v1_instance.to_dict()
# create an instance of PatchPlugRequestV1 from a dict
patch_plug_request_v1_form_dict = patch_plug_request_v1.from_dict(patch_plug_request_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


