# JobStatusAndEntityHALLinks

HAL links to related actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**HALLink**](HALLink.md) |  | [optional] 
**plug** | [**HALLink**](HALLink.md) |  | 
**webscript** | [**HALLink**](HALLink.md) |  | 
**model** | [**HALLink**](HALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.job_status_and_entity_hal_links import JobStatusAndEntityHALLinks

# TODO update the JSON string below
json = "{}"
# create an instance of JobStatusAndEntityHALLinks from a JSON string
job_status_and_entity_hal_links_instance = JobStatusAndEntityHALLinks.from_json(json)
# print the JSON string representation of the object
print JobStatusAndEntityHALLinks.to_json()

# convert the object into a dict
job_status_and_entity_hal_links_dict = job_status_and_entity_hal_links_instance.to_dict()
# create an instance of JobStatusAndEntityHALLinks from a dict
job_status_and_entity_hal_links_form_dict = job_status_and_entity_hal_links.from_dict(job_status_and_entity_hal_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


