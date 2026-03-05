# UndeployedResponseV2

Undeployed

**Source:** `waylay.services.registry.models.undeployed_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**versions** | **List[str]** | The versions that were deprecated, undeployed and/or removed. | 


## Example

```python
from waylay.services.registry.models.undeployed_response_v2 import UndeployedResponseV2

undeployed_response_v2 = UndeployedResponseV2(message=..., versions=...)

# Create from JSON
undeployed_response_v2 = UndeployedResponseV2.from_json(
    '{ "message": ..., "versions": ... }'
)

# Export to dictionary
undeployed_response_v2_dict = undeployed_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


