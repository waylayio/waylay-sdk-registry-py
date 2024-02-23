# JobHALLinks

HAL links to related actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLink**](HALLink.md) |  | [optional] 
**job** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_hal_links import JobHALLinks

# TODO update the JSON string below
json = "{}"
# create an instance of JobHALLinks from a JSON string
job_hal_links_instance = JobHALLinks.from_json(json)
# print the JSON string representation of the object
print JobHALLinks.to_json()

# convert the object into a dict
job_hal_links_dict = job_hal_links_instance.to_dict()
# create an instance of JobHALLinks from a dict
job_hal_links_form_dict = job_hal_links.from_dict(job_hal_links_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


