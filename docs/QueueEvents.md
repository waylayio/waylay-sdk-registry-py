# QueueEvents


**Source:** `waylay.services.registry.models.queue_events`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COMPLETED** | `'completed'` |
**FAILED** | `'failed'` |
**ACTIVE** | `'active'` |
**DELAYED** | `'delayed'` |
**WAITING** | `'waiting'` |
**WAITING_MINUS_CHILDREN** | `'waiting-children'` |
**ADDED** | `'added'` |
**CLEANED** | `'cleaned'` |
**DRAINED** | `'drained'` |
**ERROR** | `'error'` |
**PAUSED** | `'paused'` |
**PROGRESS** | `'progress'` |
**REMOVED** | `'removed'` |
**RESUMED** | `'resumed'` |
**RETRIES_MINUS_EXHAUSTED** | `'retries-exhausted'` |
**STALLED** | `'stalled'` |

## Example

```python
from waylay.services.registry.models.queue_events import QueueEvents

# Use enum by value
my_queue_events = QueueEvents.COMPLETED
print(my_queue_events)  # Output: 'completed'

# Or by string value
my_queue_events = QueueEvents("completed")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


