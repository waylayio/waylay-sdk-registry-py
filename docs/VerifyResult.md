# VerifyResult

The result data for a completed verification job.

**Source:** `waylay.services.registry.models.verify_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | **bool** | If true, the deployment check succeeded. | 
**replicas** | **float** | The number of replicas this function was running at the time of the check. | [optional] 


## Example

```python
from waylay.services.registry.models.verify_result import VerifyResult

verify_result = VerifyResult(healthy=..., replicas=...)

# Create from JSON
verify_result = VerifyResult.from_json('{ "healthy": ..., "replicas": ... }')

# Export to dictionary
verify_result_dict = verify_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


