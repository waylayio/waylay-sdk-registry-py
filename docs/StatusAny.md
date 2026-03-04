# StatusAny

Includes *all* statuses (including `undeployed`) as a filter

**Source:** `waylay.services.registry.models.status_any`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**ANY** | `'any'` |

## Example

```python
from waylay.services.registry.models.status_any import StatusAny

# Use enum by value
my_status_any = StatusAny.ANY
print(my_status_any)  # Output: 'any'

# Or by string value
my_status_any = StatusAny("any")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


