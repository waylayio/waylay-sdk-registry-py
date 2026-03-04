# Webscript1


**Source:** `waylay.services.registry.models.webscript1`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 
**webscript** | [**HALLinks**](HALLinks.md) |  | 


## Example

```python
from waylay.services.registry.models.webscript1 import Webscript1

webscript1 = Webscript1(event=..., job=..., webscript=...)

# Create from JSON
webscript1 = Webscript1.from_json('{ "event": ..., "job": ..., "webscript": ... }')

# Export to dictionary
webscript1_dict = webscript1.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


