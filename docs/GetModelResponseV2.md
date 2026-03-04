# GetModelResponseV2

Model Found

**Source:** `waylay.services.registry.models.get_model_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**GetPlugResponseV2Embedded**](GetPlugResponseV2Embedded.md) |  | [optional] 
**entity** | [**KfservingResponseV2**](KfservingResponseV2.md) |  | 
**links** | [**GetPlugResponseV2Links**](GetPlugResponseV2Links.md) |  | 


## Example

```python
from waylay.services.registry.models.get_model_response_v2 import GetModelResponseV2

get_model_response_v2 = GetModelResponseV2(embedded=..., entity=..., links=...)

# Create from JSON
get_model_response_v2 = GetModelResponseV2.from_json(
    '{ "_embedded": ..., "entity": ..., "_links": ... }'
)

# Export to dictionary
get_model_response_v2_dict = get_model_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


