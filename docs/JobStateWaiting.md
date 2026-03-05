# JobStateWaiting

The job has been queued for execution, but might be waiting because of rate limiting.

**Source:** `waylay.services.registry.models.job_state_waiting`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**WAITING** | `'waiting'` |

## Example

```python
from waylay.services.registry.models.job_state_waiting import JobStateWaiting

# Use enum by value
my_job_state_waiting = JobStateWaiting.WAITING
print(my_job_state_waiting)  # Output: 'waiting'

# Or by string value
my_job_state_waiting = JobStateWaiting("waiting")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


