# CompletedEventSSEEvent

The job queue event that trigged this message

**Source:** `waylay.services.registry.models.completed_event_sse_event`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**COMPLETED** | `'completed'` |

## Example

```python
from waylay.services.registry.models.completed_event_sse_event import (
    CompletedEventSSEEvent,
)

# Use enum by value
my_completed_event_sse_event = CompletedEventSSEEvent.COMPLETED
print(my_completed_event_sse_event)  # Output: 'completed'

# Or by string value
my_completed_event_sse_event = CompletedEventSSEEvent("completed")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


