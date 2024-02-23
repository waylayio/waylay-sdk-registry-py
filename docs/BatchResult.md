# BatchResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_count** | **float** |  | [optional] 

## Example

```python
from waylay.services.registry.models.batch_result import BatchResult

# TODO update the JSON string below
json = "{}"
# create an instance of BatchResult from a JSON string
batch_result_instance = BatchResult.from_json(json)
# print the JSON string representation of the object
print BatchResult.to_json()

# convert the object into a dict
batch_result_dict = batch_result_instance.to_dict()
# create an instance of BatchResult from a dict
batch_result_form_dict = batch_result.from_dict(batch_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


