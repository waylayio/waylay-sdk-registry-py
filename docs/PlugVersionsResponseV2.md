# PlugVersionsResponseV2

Plugs Versions Found

**Source:** `waylay.services.registry.models.plug_versions_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**GetPlugResponseV2Embedded**](GetPlugResponseV2Embedded.md) |  | [optional] 
**limit** | **float** | The page size used for this query result. | [optional] 
**count** | **float** | The total count of matching items, from which this result is one page. | 
**page** | **float** | The page number of a paged query result. | [optional] 
**entities** | [**List[PlugResponseV2]**](PlugResponseV2.md) | The specification and deployment status of the queried functions | 


## Example

```python
from waylay.services.registry.models.plug_versions_response_v2 import (
    PlugVersionsResponseV2,
)

plug_versions_response_v2 = PlugVersionsResponseV2(
    embedded=..., limit=..., count=..., page=..., entities=...
)

# Create from JSON
plug_versions_response_v2 = PlugVersionsResponseV2.from_json(
    '{ "_embedded": ..., "limit": ..., "count": ..., "page": ..., "entities": ... }'
)

# Export to dictionary
plug_versions_response_v2_dict = plug_versions_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


