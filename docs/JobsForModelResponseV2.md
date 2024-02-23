# JobsForModelResponseV2

Model Jobs Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[AnyJobForFunction]**](AnyJobForFunction.md) | Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity. | 
**function** | [**FunctionRef**](FunctionRef.md) |  | 
**links** | [**JobsForModelResponseV2Links**](JobsForModelResponseV2Links.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.jobs_for_model_response_v2 import JobsForModelResponseV2

# TODO update the JSON string below
json = "{}"
# create an instance of JobsForModelResponseV2 from a JSON string
jobs_for_model_response_v2_instance = JobsForModelResponseV2.from_json(json)
# print the JSON string representation of the object
print JobsForModelResponseV2.to_json()

# convert the object into a dict
jobs_for_model_response_v2_dict = jobs_for_model_response_v2_instance.to_dict()
# create an instance of JobsForModelResponseV2 from a dict
jobs_for_model_response_v2_form_dict = jobs_for_model_response_v2.from_dict(jobs_for_model_response_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


