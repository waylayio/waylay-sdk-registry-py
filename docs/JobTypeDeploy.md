# JobTypeDeploy

A job that deploys a function image to the openfaas runtime.

**Source:** `waylay.services.registry.models.job_type_deploy`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**DEPLOY** | `'deploy'` |

## Example

```python
from waylay.services.registry.models.job_type_deploy import JobTypeDeploy

# Use enum by value
my_job_type_deploy = JobTypeDeploy.DEPLOY
print(my_job_type_deploy)  # Output: 'deploy'

# Or by string value
my_job_type_deploy = JobTypeDeploy("deploy")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


