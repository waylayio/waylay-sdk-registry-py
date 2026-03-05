# JobTypeVerify

A job that checks the health of a deployed function.

**Source:** `waylay.services.registry.models.job_type_verify`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**VERIFY** | `'verify'` |

## Example

```python
from waylay.services.registry.models.job_type_verify import JobTypeVerify

# Use enum by value
my_job_type_verify = JobTypeVerify.VERIFY
print(my_job_type_verify)  # Output: 'verify'

# Or by string value
my_job_type_verify = JobTypeVerify("verify")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


