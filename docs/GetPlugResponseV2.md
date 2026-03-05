# GetPlugResponseV2

Plug Found

**Source:** `waylay.services.registry.models.get_plug_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**GetPlugResponseV2Embedded**](GetPlugResponseV2Embedded.md) |  | [optional] 
**entity** | [**PlugWithInvocationResponseV2**](PlugWithInvocationResponseV2.md) |  | 
**links** | [**GetPlugResponseV2Links**](GetPlugResponseV2Links.md) |  | 


## Example

```python
from waylay.services.registry.models.get_plug_response_v2 import GetPlugResponseV2

get_plug_response_v2 = GetPlugResponseV2(embedded=..., entity=..., links=...)

# Create from JSON
get_plug_response_v2 = GetPlugResponseV2.from_json(
    '{ "_embedded": ..., "entity": ..., "_links": ... }'
)

# Export to dictionary
get_plug_response_v2_dict = get_plug_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


