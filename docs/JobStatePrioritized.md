# JobStatePrioritized

The job has been queued for execution with priority, but might be waiting because of rate limiting.

**Source:** `waylay.services.registry.models.job_state_prioritized`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**PRIORITIZED** | `'prioritized'` |

## Example

```python
from waylay.services.registry.models.job_state_prioritized import JobStatePrioritized

# Use enum by value
my_job_state_prioritized = JobStatePrioritized.PRIORITIZED
print(my_job_state_prioritized)  # Output: 'prioritized'

# Or by string value
my_job_state_prioritized = JobStatePrioritized("prioritized")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


