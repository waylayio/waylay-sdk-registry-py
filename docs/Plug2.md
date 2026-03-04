# Plug2


**Source:** `waylay.services.registry.models.plug2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**plug** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.plug2 import Plug2

plug2 = Plug2(job=..., plug=...)

# Create from JSON
plug2 = Plug2.from_json('{ "job": ..., "plug": ... }')

# Export to dictionary
plug2_dict = plug2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


