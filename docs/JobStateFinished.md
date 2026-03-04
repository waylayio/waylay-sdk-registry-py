# JobStateFinished

The job completed successfully or with failure.

**Source:** `waylay.services.registry.models.job_state_finished`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**JobStateCompleted**](JobStateCompleted.md) | -
[**JobStateFailed**](JobStateFailed.md) | -

## Example

```python
from waylay.services.registry.models.job_state_finished import JobStateFinished

# Use any of the accepted types (see table above)
my_job_state_finished: JobStateFinished = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


