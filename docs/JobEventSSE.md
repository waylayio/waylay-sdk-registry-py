# JobEventSSE


**Source:** `waylay.services.registry.models.job_event_sse`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**ActiveEventSSE**](ActiveEventSSE.md) | -
[**CompletedEventSSE**](CompletedEventSSE.md) | -
[**FailedEventSSE**](FailedEventSSE.md) | -
[**DelayedEventSSE**](DelayedEventSSE.md) | -
[**WaitingEventSSE**](WaitingEventSSE.md) | -
[**WaitingChildrenEventSSE**](WaitingChildrenEventSSE.md) | -

## Example

```python
from waylay.services.registry.models.job_event_sse import JobEventSSE

# Use any of the accepted types (see table above)
my_job_event_sse: JobEventSSE = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


