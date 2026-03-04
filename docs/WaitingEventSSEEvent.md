# WaitingEventSSEEvent

The job queue event that trigged this message

**Source:** `waylay.services.registry.models.waiting_event_sse_event`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**WAITING** | `'waiting'` |

## Example

```python
from waylay.services.registry.models.waiting_event_sse_event import WaitingEventSSEEvent

# Use enum by value
my_waiting_event_sse_event = WaitingEventSSEEvent.WAITING
print(my_waiting_event_sse_event)  # Output: 'waiting'

# Or by string value
my_waiting_event_sse_event = WaitingEventSSEEvent("waiting")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


