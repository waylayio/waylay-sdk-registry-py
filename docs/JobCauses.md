# JobCauses

The motivations for including or excluding a job in response to a <em>rebuild</em> request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build** | [**JobCause**](JobCause.md) |  | [optional] 
**deploy** | [**JobCause**](JobCause.md) |  | [optional] 
**verify** | [**JobCause**](JobCause.md) |  | [optional] 
**undeploy** | [**JobCause**](JobCause.md) |  | [optional] 
**scale** | [**JobCause**](JobCause.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_causes import JobCauses

# TODO update the JSON string below
json = "{}"
# create an instance of JobCauses from a JSON string
job_causes_instance = JobCauses.from_json(json)
# print the JSON string representation of the object
print JobCauses.to_json()

# convert the object into a dict
job_causes_dict = job_causes_instance.to_dict()
# create an instance of JobCauses from a dict
job_causes_form_dict = job_causes.from_dict(job_causes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


