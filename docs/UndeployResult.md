# UndeployResult

The result data for a completed undeployment job.

**Source:** `waylay.services.registry.models.undeploy_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | **bool** |  | 
**assets** | **bool** |  | 
**registration** | **bool** |  | 
**image** | **bool** |  | 


## Example

```python
from waylay.services.registry.models.undeploy_result import UndeployResult

undeploy_result = UndeployResult(
    deployment=..., assets=..., registration=..., image=...
)

# Create from JSON
undeploy_result = UndeployResult.from_json(
    '{ "deployment": ..., "assets": ..., "registration": ..., "image": ... }'
)

# Export to dictionary
undeploy_result_dict = undeploy_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


