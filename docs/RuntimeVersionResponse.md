# RuntimeVersionResponse

: Runtime Version Found

**Source:** `waylay.services.registry.models.runtime_version_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**RuntimeSummaryResponseEmbedded**](RuntimeSummaryResponseEmbedded.md) |  | [optional] 
**runtime** | [**CompiledRuntimeVersion**](CompiledRuntimeVersion.md) |  | 


## Example

```python
from waylay.services.registry.models.runtime_version_response import (
    RuntimeVersionResponse,
)

runtime_version_response = RuntimeVersionResponse(embedded=..., runtime=...)

# Create from JSON
runtime_version_response = RuntimeVersionResponse.from_json(
    '{ "_embedded": ..., "runtime": ... }'
)

# Export to dictionary
runtime_version_response_dict = runtime_version_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


