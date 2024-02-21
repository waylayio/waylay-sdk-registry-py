# JobsHALLink


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**HALLink**](HALLink.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.jobs_hal_link import JobsHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of JobsHALLink from a JSON string
jobs_hal_link_instance = JobsHALLink.from_json(json)
# print the JSON string representation of the object
print JobsHALLink.to_json()

# convert the object into a dict
jobs_hal_link_dict = jobs_hal_link_instance.to_dict()
# create an instance of JobsHALLink from a dict
jobs_hal_link_form_dict = jobs_hal_link.from_dict(jobs_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


