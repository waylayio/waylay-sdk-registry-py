# JobStatusHALLink

HAL links to related actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**JobHALLinksJob**](JobHALLinksJob.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_status_hal_link import JobStatusHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusHALLink from a JSON string
job_status_hal_link_instance = JobStatusHALLink.from_json(json)
# print the JSON string representation of the object
print JobStatusHALLink.to_json()

# convert the object into a dict
job_status_hal_link_dict = job_status_hal_link_instance.to_dict()
# create an instance of JobStatusHALLink from a dict
job_status_hal_link_form_dict = job_status_hal_link.from_dict(job_status_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


