# Verify


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**links** | [**JobHALLinks**](JobHALLinks.md) |  | [optional] 
**type** | [**VerifyType**](VerifyType.md) |  | 
**state** | [**JobStateResult**](JobStateResult.md) |  | 
**request** | [**VerifyArgs**](VerifyArgs.md) |  | [optional] 
**result** | [**VerifyResult**](VerifyResult.md) |  | [optional] 
**created_at** | **datetime** | The timestamp of creation of this job | 
**created_by** | **str** | The user that created this job | 
**operation** | **str** | Request operation | 
**function** | [**FunctionRef**](FunctionRef.md) |  | [optional] 
**job** | [**JobStatus**](JobStatus.md) |  | [optional] 
**failure_reason** | [**FailureReason**](FailureReason.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.verify import Verify

# TODO update the JSON string below
json = "{}"
# create an instance of Verify from a JSON string
verify_instance = Verify.from_json(json)
# print the JSON string representation of the object
print Verify.to_json()

# convert the object into a dict
verify_dict = verify_instance.to_dict()
# create an instance of Verify from a dict
verify_form_dict = verify.from_dict(verify_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


