# FailureReason


**Source:** `waylay.services.registry.models.failure_reason`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**log** | **List[str]** | Log lines associated with this failure. | 
**events** | **List[str]** | Events associated with this failure. | 
**cause** | **str** | Main cause for the failure. | [optional] 


## Example

```python
from waylay.services.registry.models.failure_reason import FailureReason

failure_reason = FailureReason(log=..., events=..., cause=...)

# Create from JSON
failure_reason = FailureReason.from_json('{ "log": ..., "events": ..., "cause": ... }')

# Export to dictionary
failure_reason_dict = failure_reason.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


