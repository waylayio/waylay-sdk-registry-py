# DelayedEventSSEEvent

The job queue event that trigged this message

**Source:** `waylay.services.registry.models.delayed_event_sse_event`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DELAYED** | `'delayed'` |

## Example

```python
from waylay.services.registry.models.delayed_event_sse_event import DelayedEventSSEEvent

# Use enum by value
my_delayed_event_sse_event = DelayedEventSSEEvent.DELAYED
print(my_delayed_event_sse_event)  # Output: 'delayed'

# Or by string value
my_delayed_event_sse_event = DelayedEventSSEEvent("delayed")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


