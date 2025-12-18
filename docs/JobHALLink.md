# JobHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | [**HALLinkHref**](HALLinkHref.md) |  | 
**job_type** | [**JobType**](JobType.md) |  | 

## Example

```python
from waylay.services.registry.models.job_hal_link import JobHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of JobHALLink from a JSON string
job_hal_link_instance = JobHALLink.from_json(json)
# print the JSON string representation of the object
print JobHALLink.to_json()

# convert the object into a dict
job_hal_link_dict = job_hal_link_instance.to_dict()
# create an instance of JobHALLink from a dict
job_hal_link_form_dict = job_hal_link.from_dict(job_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


