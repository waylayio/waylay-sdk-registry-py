# JobSubmittedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | 
**links** | [**JobHALLinks**](JobHALLinks.md) |  | 

## Example

```python
from waylay.services.registry.models.job_submitted_response import JobSubmittedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobSubmittedResponse from a JSON string
job_submitted_response_instance = JobSubmittedResponse.from_json(json)
# print the JSON string representation of the object
print JobSubmittedResponse.to_json()

# convert the object into a dict
job_submitted_response_dict = job_submitted_response_instance.to_dict()
# create an instance of JobSubmittedResponse from a dict
job_submitted_response_form_dict = job_submitted_response.from_dict(job_submitted_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


