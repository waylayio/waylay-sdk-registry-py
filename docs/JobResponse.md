# JobResponse

Job Found

**Source:** `waylay.services.registry.models.job_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**AnyJobStatus**](AnyJobStatus.md) |  | 
**links** | [**JobEventsAndFunctionHALLink**](JobEventsAndFunctionHALLink.md) |  | 


## Example

```python
from waylay.services.registry.models.job_response import JobResponse

job_response = JobResponse(job=..., links=...)

# Create from JSON
job_response = JobResponse.from_json('{ "job": ..., "_links": ... }')

# Export to dictionary
job_response_dict = job_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


