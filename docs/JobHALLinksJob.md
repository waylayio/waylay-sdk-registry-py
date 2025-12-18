# JobHALLinksJob

Link to the job status page for the related entity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | [**HALLinkHref**](HALLinkHref.md) |  | 
**job_type** | [**JobType**](JobType.md) |  | 

## Example

```python
from waylay.services.registry.models.job_hal_links_job import JobHALLinksJob

# TODO update the JSON string below
json = "{}"
# create an instance of JobHALLinksJob from a JSON string
job_hal_links_job_instance = JobHALLinksJob.from_json(json)
# print the JSON string representation of the object
print JobHALLinksJob.to_json()

# convert the object into a dict
job_hal_links_job_dict = job_hal_links_job_instance.to_dict()
# create an instance of JobHALLinksJob from a dict
job_hal_links_job_form_dict = job_hal_links_job.from_dict(job_hal_links_job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


