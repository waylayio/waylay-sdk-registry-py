# GetWebscriptResponseV2

Webscript Found

**Source:** `waylay.services.registry.models.get_webscript_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**GetPlugResponseV2Embedded**](GetPlugResponseV2Embedded.md) |  | [optional] 
**entity** | [**WebscriptResponseV2**](WebscriptResponseV2.md) |  | 
**links** | [**GetWebscriptResponseV2Links**](GetWebscriptResponseV2Links.md) |  | 


## Example

```python
from waylay.services.registry.models.get_webscript_response_v2 import (
    GetWebscriptResponseV2,
)

get_webscript_response_v2 = GetWebscriptResponseV2(embedded=..., entity=..., links=...)

# Create from JSON
get_webscript_response_v2 = GetWebscriptResponseV2.from_json(
    '{ "_embedded": ..., "entity": ..., "_links": ... }'
)

# Export to dictionary
get_webscript_response_v2_dict = get_webscript_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


