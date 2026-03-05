# JobStateWaitingChildren

The job is waiting for child jobs to be completed.

**Source:** `waylay.services.registry.models.job_state_waiting_children`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**WAITING_MINUS_CHILDREN** | `'waiting-children'` |

## Example

```python
from waylay.services.registry.models.job_state_waiting_children import (
    JobStateWaitingChildren,
)

# Use enum by value
my_job_state_waiting_children = JobStateWaitingChildren.WAITING_MINUS_CHILDREN
print(my_job_state_waiting_children)  # Output: 'waiting-children'

# Or by string value
my_job_state_waiting_children = JobStateWaitingChildren("waiting-children")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


