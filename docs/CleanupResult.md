# CleanupResult

The result data for a completed cleanup job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scheduled_job** | [**JobReference**](JobReference.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.cleanup_result import CleanupResult

# TODO update the JSON string below
json = "{}"
# create an instance of CleanupResult from a JSON string
cleanup_result_instance = CleanupResult.from_json(json)
# print the JSON string representation of the object
print CleanupResult.to_json()

# convert the object into a dict
cleanup_result_dict = cleanup_result_instance.to_dict()
# create an instance of CleanupResult from a dict
cleanup_result_form_dict = cleanup_result.from_dict(cleanup_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


