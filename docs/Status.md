# Status

Status for a deployed function.

**Source:** `waylay.services.registry.models.status`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**REGISTERED** | `'registered'` |
**RUNNING** | `'running'` |
**PENDING** | `'pending'` |
**DEPLOYED** | `'deployed'` |
**UNHEALTHY** | `'unhealthy'` |
**FAILED** | `'failed'` |
**UNDEPLOYING** | `'undeploying'` |
**UNDEPLOYED** | `'undeployed'` |

## Example

```python
from waylay.services.registry.models.status import Status

# Use enum by value
my_status = Status.REGISTERED
print(my_status)  # Output: 'registered'

# Or by string value
my_status = Status("registered")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


