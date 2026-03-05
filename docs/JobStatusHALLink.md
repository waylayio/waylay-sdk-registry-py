# JobStatusHALLink

HAL links to related actions.

**Source:** `waylay.services.registry.models.job_status_hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.job_status_hal_link import JobStatusHALLink

job_status_hal_link = JobStatusHALLink(job=...)

# Create from JSON
job_status_hal_link = JobStatusHALLink.from_json('{ "job": ... }')

# Export to dictionary
job_status_hal_link_dict = job_status_hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


