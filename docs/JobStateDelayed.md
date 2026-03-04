# JobStateDelayed

The job has been delayed for retry after a failure.

**Source:** `waylay.services.registry.models.job_state_delayed`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DELAYED** | `'delayed'` |

## Example

```python
from waylay.services.registry.models.job_state_delayed import JobStateDelayed

# Use enum by value
my_job_state_delayed = JobStateDelayed.DELAYED
print(my_job_state_delayed)  # Output: 'delayed'

# Or by string value
my_job_state_delayed = JobStateDelayed("delayed")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


