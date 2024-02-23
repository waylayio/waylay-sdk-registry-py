# JobsResponse

Jobs Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The page size used for this query result. | [optional] 
**jobs** | [**List[AnyJobStatusSummary]**](AnyJobStatusSummary.md) | Listing of jobs that satisfy the query. | 

## Example

```python
from waylay.services.registry.models.jobs_response import JobsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JobsResponse from a JSON string
jobs_response_instance = JobsResponse.from_json(json)
# print the JSON string representation of the object
print JobsResponse.to_json()

# convert the object into a dict
jobs_response_dict = jobs_response_instance.to_dict()
# create an instance of JobsResponse from a dict
jobs_response_form_dict = jobs_response.from_dict(jobs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


