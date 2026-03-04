# WaitingChildrenEventSSEEvent

The job queue event that trigged this message

**Source:** `waylay.services.registry.models.waiting_children_event_sse_event`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**WAITING_MINUS_CHILDREN** | `'waiting-children'` |

## Example

```python
from waylay.services.registry.models.waiting_children_event_sse_event import (
    WaitingChildrenEventSSEEvent,
)

# Use enum by value
my_waiting_children_event_sse_event = (
    WaitingChildrenEventSSEEvent.WAITING_MINUS_CHILDREN
)
print(my_waiting_children_event_sse_event)  # Output: 'waiting-children'

# Or by string value
my_waiting_children_event_sse_event = WaitingChildrenEventSSEEvent("waiting-children")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


