# UndeployJobStatusType

The type of the background task.

**Source:** `waylay.services.registry.models.undeploy_job_status_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UNDEPLOY** | `'undeploy'` |

## Example

```python
from waylay.services.registry.models.undeploy_job_status_type import (
    UndeployJobStatusType,
)

# Use enum by value
my_undeploy_job_status_type = UndeployJobStatusType.UNDEPLOY
print(my_undeploy_job_status_type)  # Output: 'undeploy'

# Or by string value
my_undeploy_job_status_type = UndeployJobStatusType("undeploy")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


