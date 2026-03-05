# RuntimeSummaryResponseEmbedded

Embedded representations of the referenced tags.

**Source:** `waylay.services.registry.models.runtime_summary_response_embedded`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[RuntimeTag]**](RuntimeTag.md) | Record of &lt;tag key, tag representation&gt; pairs. | [optional] 


## Example

```python
from waylay.services.registry.models.runtime_summary_response_embedded import (
    RuntimeSummaryResponseEmbedded,
)

runtime_summary_response_embedded = RuntimeSummaryResponseEmbedded(tags=...)

# Create from JSON
runtime_summary_response_embedded = RuntimeSummaryResponseEmbedded.from_json(
    '{ "tags": ... }'
)

# Export to dictionary
runtime_summary_response_embedded_dict = runtime_summary_response_embedded.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


