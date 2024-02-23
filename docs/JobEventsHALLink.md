# JobEventsHALLink

HAL links to related actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_events_hal_link import JobEventsHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventsHALLink from a JSON string
job_events_hal_link_instance = JobEventsHALLink.from_json(json)
# print the JSON string representation of the object
print JobEventsHALLink.to_json()

# convert the object into a dict
job_events_hal_link_dict = job_events_hal_link_instance.to_dict()
# create an instance of JobEventsHALLink from a dict
job_events_hal_link_form_dict = job_events_hal_link.from_dict(job_events_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


