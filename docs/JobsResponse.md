# JobsResponse

Jobs Found

**Source:** `waylay.services.registry.models.jobs_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The page size used for this query result. | [optional] 
**jobs** | [**List[AnyJobStatusSummary]**](AnyJobStatusSummary.md) | Listing of jobs that satisfy the query. | 


## Example

```python
from waylay.services.registry.models.jobs_response import JobsResponse

jobs_response = JobsResponse(limit=..., jobs=...)

# Create from JSON
jobs_response = JobsResponse.from_json('{ "limit": ..., "jobs": ... }')

# Export to dictionary
jobs_response_dict = jobs_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


