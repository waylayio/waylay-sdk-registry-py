# VerifyResult

The result data for a completed verification job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | **bool** | If true, the deployment check succeeded. | 
**replicas** | **float** | The number of replicas this function was running at the time of the check. | [optional] 

## Example

```python
from waylay.services.registry.models.verify_result import VerifyResult

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyResult from a JSON string
verify_result_instance = VerifyResult.from_json(json)
# print the JSON string representation of the object
print VerifyResult.to_json()

# convert the object into a dict
verify_result_dict = verify_result_instance.to_dict()
# create an instance of VerifyResult from a dict
verify_result_form_dict = verify_result.from_dict(verify_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


