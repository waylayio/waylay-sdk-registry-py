# GetPlugResponseV2Embedded

Embedded representations of the referenced tags.

**Source:** `waylay.services.registry.models.get_plug_response_v2_embedded`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) | Record of &lt;tag key, tag representation&gt; pairs. | [optional] 


## Example

```python
from waylay.services.registry.models.get_plug_response_v2_embedded import (
    GetPlugResponseV2Embedded,
)

get_plug_response_v2_embedded = GetPlugResponseV2Embedded(tags=...)

# Create from JSON
get_plug_response_v2_embedded = GetPlugResponseV2Embedded.from_json('{ "tags": ... }')

# Export to dictionary
get_plug_response_v2_embedded_dict = get_plug_response_v2_embedded.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


