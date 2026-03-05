# NotifyResult

The result data for a change notification.

**Source:** `waylay.services.registry.models.notify_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**operation** | [**RequestOperation**](RequestOperation.md) |  | 


## Example

```python
from waylay.services.registry.models.notify_result import NotifyResult

notify_result = NotifyResult(operation=...)

# Create from JSON
notify_result = NotifyResult.from_json('{ "operation": ... }')

# Export to dictionary
notify_result_dict = notify_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


