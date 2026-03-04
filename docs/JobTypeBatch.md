# JobTypeBatch

A job that groups other jobs as a parent.

**Source:** `waylay.services.registry.models.job_type_batch`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**BATCH** | `'batch'` |

## Example

```python
from waylay.services.registry.models.job_type_batch import JobTypeBatch

# Use enum by value
my_job_type_batch = JobTypeBatch.BATCH
print(my_job_type_batch)  # Output: 'batch'

# Or by string value
my_job_type_batch = JobTypeBatch("batch")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


