# JobQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 
**type** | [**List[JobTypeSchema]**](JobTypeSchema.md) | Filter on job type | [optional] 
**state** | [**List[JobStateResult]**](JobStateResult.md) | Filter on job state | [optional] 
**function_type** | [**List[FunctionType]**](FunctionType.md) | Filter on function type | [optional] 
**created_before** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 
**created_after** | [**TimestampSpec**](TimestampSpec.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.job_query import JobQuery

# TODO update the JSON string below
json = "{}"
# create an instance of JobQuery from a JSON string
job_query_instance = JobQuery.from_json(json)
# print the JSON string representation of the object
print JobQuery.to_json()

# convert the object into a dict
job_query_dict = job_query_instance.to_dict()
# create an instance of JobQuery from a dict
job_query_form_dict = job_query.from_dict(job_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


