# FunctionTagsResponse

Function Tags Found

**Source:** `waylay.services.registry.models.function_tags_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) |  | 


## Example

```python
from waylay.services.registry.models.function_tags_response import FunctionTagsResponse

function_tags_response = FunctionTagsResponse(tags=...)

# Create from JSON
function_tags_response = FunctionTagsResponse.from_json('{ "tags": ... }')

# Export to dictionary
function_tags_response_dict = function_tags_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


