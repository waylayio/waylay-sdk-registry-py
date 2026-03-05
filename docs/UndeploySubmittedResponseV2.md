# UndeploySubmittedResponseV2

Undeployment Initiated

**Source:** `waylay.services.registry.models.undeploy_submitted_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 
**versions** | **List[str]** | The versions for which undeployment and/or removal is initiated. | 


## Example

```python
from waylay.services.registry.models.undeploy_submitted_response_v2 import (
    UndeploySubmittedResponseV2,
)

undeploy_submitted_response_v2 = UndeploySubmittedResponseV2(
    message=..., links=..., versions=...
)

# Create from JSON
undeploy_submitted_response_v2 = UndeploySubmittedResponseV2.from_json(
    '{ "message": ..., "_links": ..., "versions": ... }'
)

# Export to dictionary
undeploy_submitted_response_v2_dict = undeploy_submitted_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


