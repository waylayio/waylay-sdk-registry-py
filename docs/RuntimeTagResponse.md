# RuntimeTagResponse

Runtime Tag Found

**Source:** `waylay.services.registry.models.runtime_tag_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | [**RuntimeTag**](RuntimeTag.md) |  | 


## Example

```python
from waylay.services.registry.models.runtime_tag_response import RuntimeTagResponse

runtime_tag_response = RuntimeTagResponse(tag=...)

# Create from JSON
runtime_tag_response = RuntimeTagResponse.from_json('{ "tag": ... }')

# Export to dictionary
runtime_tag_response_dict = runtime_tag_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


