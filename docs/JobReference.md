# JobReference


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobType**](JobType.md) |  | 
**id** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_reference import JobReference

# TODO update the JSON string below
json = "{}"
# create an instance of JobReference from a JSON string
job_reference_instance = JobReference.from_json(json)
# print the JSON string representation of the object
print JobReference.to_json()

# convert the object into a dict
job_reference_dict = job_reference_instance.to_dict()
# create an instance of JobReference from a dict
job_reference_form_dict = job_reference.from_dict(job_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


