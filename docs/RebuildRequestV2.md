# RebuildRequestV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.rebuild_request_v2 import RebuildRequestV2

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildRequestV2 from a JSON string
rebuild_request_v2_instance = RebuildRequestV2.from_json(json)
# print the JSON string representation of the object
print RebuildRequestV2.to_json()

# convert the object into a dict
rebuild_request_v2_dict = rebuild_request_v2_instance.to_dict()
# create an instance of RebuildRequestV2 from a dict
rebuild_request_v2_form_dict = rebuild_request_v2.from_dict(rebuild_request_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


