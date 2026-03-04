# FailedEventSSEEvent

The job queue event that trigged this message

**Source:** `waylay.services.registry.models.failed_event_sse_event`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**FAILED** | `'failed'` |

## Example

```python
from waylay.services.registry.models.failed_event_sse_event import FailedEventSSEEvent

# Use enum by value
my_failed_event_sse_event = FailedEventSSEEvent.FAILED
print(my_failed_event_sse_event)  # Output: 'failed'

# Or by string value
my_failed_event_sse_event = FailedEventSSEEvent("failed")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


