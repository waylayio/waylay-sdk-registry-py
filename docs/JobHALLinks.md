# JobHALLinks

HAL links to related actions.

**Source:** `waylay.services.registry.models.job_hal_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.job_hal_links import JobHALLinks

job_hal_links = JobHALLinks(event=..., job=...)

# Create from JSON
job_hal_links = JobHALLinks.from_json('{ "event": ..., "job": ... }')

# Export to dictionary
job_hal_links_dict = job_hal_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


