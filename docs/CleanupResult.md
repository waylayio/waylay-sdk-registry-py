# CleanupResult

The result data for a completed cleanup job.

**Source:** `waylay.services.registry.models.cleanup_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_job** | [**JobReference**](JobReference.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.cleanup_result import CleanupResult

cleanup_result = CleanupResult(scheduled_job=...)

# Create from JSON
cleanup_result = CleanupResult.from_json('{ "scheduledJob": ... }')

# Export to dictionary
cleanup_result_dict = cleanup_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


