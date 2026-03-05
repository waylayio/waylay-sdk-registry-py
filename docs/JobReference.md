# JobReference


**Source:** `waylay.services.registry.models.job_reference`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobType**](JobType.md) |  | 
**id** | **str** |  | [optional] 


## Example

```python
from waylay.services.registry.models.job_reference import JobReference

job_reference = JobReference(type=..., id=...)

# Create from JSON
job_reference = JobReference.from_json('{ "type": ..., "id": ... }')

# Export to dictionary
job_reference_dict = job_reference.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


