# BatchResult


**Source:** `waylay.services.registry.models.batch_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_count** | **float** |  | [optional] 


## Example

```python
from waylay.services.registry.models.batch_result import BatchResult

batch_result = BatchResult(job_count=...)

# Create from JSON
batch_result = BatchResult.from_json('{ "jobCount": ... }')

# Export to dictionary
batch_result_dict = batch_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


