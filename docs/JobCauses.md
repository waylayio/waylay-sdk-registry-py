# JobCauses

The motivations for including or excluding a job in response to a <em>rebuild</em> request.

**Source:** `waylay.services.registry.models.job_causes`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**JobCause**](JobCause.md) |  | [optional] 
**deploy** | [**JobCause**](JobCause.md) |  | [optional] 
**verify** | [**JobCause**](JobCause.md) |  | [optional] 
**undeploy** | [**JobCause**](JobCause.md) |  | [optional] 
**scale** | [**JobCause**](JobCause.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.job_causes import JobCauses

job_causes = JobCauses(build=..., deploy=..., verify=..., undeploy=..., scale=...)

# Create from JSON
job_causes = JobCauses.from_json(
    '{ "build": ..., "deploy": ..., "verify": ..., "undeploy": ..., "scale": ... }'
)

# Export to dictionary
job_causes_dict = job_causes.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


