# JobEventsHALLink

HAL links to related actions.

**Source:** `waylay.services.registry.models.job_events_hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLinks**](HALLinks.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.job_events_hal_link import JobEventsHALLink

job_events_hal_link = JobEventsHALLink(event=...)

# Create from JSON
job_events_hal_link = JobEventsHALLink.from_json('{ "event": ... }')

# Export to dictionary
job_events_hal_link_dict = job_events_hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


