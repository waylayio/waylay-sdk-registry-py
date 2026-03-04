# Webscript2


**Source:** `waylay.services.registry.models.webscript2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**webscript** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.webscript2 import Webscript2

webscript2 = Webscript2(job=..., webscript=...)

# Create from JSON
webscript2 = Webscript2.from_json('{ "job": ..., "webscript": ... }')

# Export to dictionary
webscript2_dict = webscript2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


