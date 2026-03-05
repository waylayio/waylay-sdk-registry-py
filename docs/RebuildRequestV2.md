# RebuildRequestV2


**Source:** `waylay.services.registry.models.rebuild_request_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | [**FunctionDeployOverridesType**](FunctionDeployOverridesType.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.rebuild_request_v2 import RebuildRequestV2

rebuild_request_v2 = RebuildRequestV2(deploy=...)

# Create from JSON
rebuild_request_v2 = RebuildRequestV2.from_json('{ "deploy": ... }')

# Export to dictionary
rebuild_request_v2_dict = rebuild_request_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


