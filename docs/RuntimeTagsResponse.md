# RuntimeTagsResponse

Runtime Tags Found

**Source:** `waylay.services.registry.models.runtime_tags_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[RuntimeTag]**](RuntimeTag.md) |  | 


## Example

```python
from waylay.services.registry.models.runtime_tags_response import RuntimeTagsResponse

runtime_tags_response = RuntimeTagsResponse(tags=...)

# Create from JSON
runtime_tags_response = RuntimeTagsResponse.from_json('{ "tags": ... }')

# Export to dictionary
runtime_tags_response_dict = runtime_tags_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


