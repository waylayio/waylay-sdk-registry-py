# JobHALLink


**Source:** `waylay.services.registry.models.job_hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | [**IHALLinkHref**](IHALLinkHref.md) |  | 
**job_type** | [**JobType**](JobType.md) |  | 


## Example

```python
from waylay.services.registry.models.job_hal_link import JobHALLink

job_hal_link = JobHALLink(href=..., job_type=...)

# Create from JSON
job_hal_link = JobHALLink.from_json('{ "href": ..., "jobType": ... }')

# Export to dictionary
job_hal_link_dict = job_hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


