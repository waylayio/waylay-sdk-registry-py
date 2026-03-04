# JobType


**Source:** `waylay.services.registry.models.job_type`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BUILD** | `'build'` |
**DEPLOY** | `'deploy'` |
**VERIFY** | `'verify'` |
**UNDEPLOY** | `'undeploy'` |
**BATCH** | `'batch'` |
**SCALE** | `'scale'` |
**CLEANUP** | `'cleanup'` |
**NOTIFY** | `'notify'` |

## Example

```python
from waylay.services.registry.models.job_type import JobType

# Use enum by value
my_job_type = JobType.BUILD
print(my_job_type)  # Output: 'build'

# Or by string value
my_job_type = JobType("build")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


