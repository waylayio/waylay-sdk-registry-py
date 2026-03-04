# ProtectByNameResponseV2

Protection changed.

**Source:** `waylay.services.registry.models.protect_by_name_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**versions** | **List[str]** | The versions that were protected or unprotected. | 


## Example

```python
from waylay.services.registry.models.protect_by_name_response_v2 import (
    ProtectByNameResponseV2,
)

protect_by_name_response_v2 = ProtectByNameResponseV2(message=..., versions=...)

# Create from JSON
protect_by_name_response_v2 = ProtectByNameResponseV2.from_json(
    '{ "message": ..., "versions": ... }'
)

# Export to dictionary
protect_by_name_response_v2_dict = protect_by_name_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


