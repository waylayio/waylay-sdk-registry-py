# JobResponse

Job Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job** | [**AnyJobStatus**](AnyJobStatus.md) |  | 
**links** | [**JobEventsAndFunctionHALLink**](JobEventsAndFunctionHALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.job_response import JobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobResponse from a JSON string
job_response_instance = JobResponse.from_json(json)
# print the JSON string representation of the object
print JobResponse.to_json()

# convert the object into a dict
job_response_dict = job_response_instance.to_dict()
# create an instance of JobResponse from a dict
job_response_form_dict = job_response.from_dict(job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


