# StatusExclude

Any status value with a `-` postfix appended, excludes that status as a filter.

**Source:** `waylay.services.registry.models.status_exclude`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**REGISTERED_MINUS** | `'registered-'` |
**RUNNING_MINUS** | `'running-'` |
**PENDING_MINUS** | `'pending-'` |
**DEPLOYED_MINUS** | `'deployed-'` |
**UNHEALTHY_MINUS** | `'unhealthy-'` |
**FAILED_MINUS** | `'failed-'` |
**UNDEPLOYING_MINUS** | `'undeploying-'` |
**UNDEPLOYED_MINUS** | `'undeployed-'` |

## Example

```python
from waylay.services.registry.models.status_exclude import StatusExclude

# Use enum by value
my_status_exclude = StatusExclude.REGISTERED_MINUS
print(my_status_exclude)  # Output: 'registered-'

# Or by string value
my_status_exclude = StatusExclude("registered-")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


