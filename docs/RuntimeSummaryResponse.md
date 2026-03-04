# RuntimeSummaryResponse

Runtimes Found

**Source:** `waylay.services.registry.models.runtime_summary_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**RuntimeSummaryResponseEmbedded**](RuntimeSummaryResponseEmbedded.md) |  | [optional] 
**runtimes** | [**List[RuntimeSummary]**](RuntimeSummary.md) |  | 


## Example

```python
from waylay.services.registry.models.runtime_summary_response import (
    RuntimeSummaryResponse,
)

runtime_summary_response = RuntimeSummaryResponse(embedded=..., runtimes=...)

# Create from JSON
runtime_summary_response = RuntimeSummaryResponse.from_json(
    '{ "_embedded": ..., "runtimes": ... }'
)

# Export to dictionary
runtime_summary_response_dict = runtime_summary_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


