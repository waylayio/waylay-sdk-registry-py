# JobTypeUndeploy

A job that undeploys a deployed function and removes it from the registry.

**Source:** `waylay.services.registry.models.job_type_undeploy`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**UNDEPLOY** | `'undeploy'` |

## Example

```python
from waylay.services.registry.models.job_type_undeploy import JobTypeUndeploy

# Use enum by value
my_job_type_undeploy = JobTypeUndeploy.UNDEPLOY
print(my_job_type_undeploy)  # Output: 'undeploy'

# Or by string value
my_job_type_undeploy = JobTypeUndeploy("undeploy")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


