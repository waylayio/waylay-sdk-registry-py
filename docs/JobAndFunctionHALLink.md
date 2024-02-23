# JobAndFunctionHALLink

HAL links to related actions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | [**HALLink**](HALLink.md) |  | [optional] 
**job** | [**HALLink**](HALLink.md) |  | [optional] 
**plug** | [**HALLink**](HALLink.md) |  | 
**webscript** | [**HALLink**](HALLink.md) |  | 
**model** | [**HALLink**](HALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.job_and_function_hal_link import JobAndFunctionHALLink

# TODO update the JSON string below
json = "{}"
# create an instance of JobAndFunctionHALLink from a JSON string
job_and_function_hal_link_instance = JobAndFunctionHALLink.from_json(json)
# print the JSON string representation of the object
print JobAndFunctionHALLink.to_json()

# convert the object into a dict
job_and_function_hal_link_dict = job_and_function_hal_link_instance.to_dict()
# create an instance of JobAndFunctionHALLink from a dict
job_and_function_hal_link_form_dict = job_and_function_hal_link.from_dict(job_and_function_hal_link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


