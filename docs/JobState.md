# JobState

Allowed job states

**Source:** `waylay.services.registry.models.job_state`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**JobStateFinished**](JobStateFinished.md) | -
[**JobStateActive**](JobStateActive.md) | -
[**JobStateDelayed**](JobStateDelayed.md) | -
[**JobStateWaiting**](JobStateWaiting.md) | -
[**JobStateWaitingChildren**](JobStateWaitingChildren.md) | -
[**JobStatePrioritized**](JobStatePrioritized.md) | -

## Example

```python
from waylay.services.registry.models.job_state import JobState

# Use any of the accepted types (see table above)
my_job_state: JobState = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


