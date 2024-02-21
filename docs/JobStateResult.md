# JobStateResult

All reported job states

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from waylay.services.registry.models.job_state_result import JobStateResult

# TODO update the JSON string below
json = "{}"
# create an instance of JobStateResult from a JSON string
job_state_result_instance = JobStateResult.from_json(json)
# print the JSON string representation of the object
print JobStateResult.to_json()

# convert the object into a dict
job_state_result_dict = job_state_result_instance.to_dict()
# create an instance of JobStateResult from a dict
job_state_result_form_dict = job_state_result.from_dict(job_state_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


