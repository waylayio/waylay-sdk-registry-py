# VerifyQueryV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_to_zero** | **bool** | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 

## Example

```python
from waylay.services.registry.models.verify_query_v1 import VerifyQueryV1

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyQueryV1 from a JSON string
verify_query_v1_instance = VerifyQueryV1.from_json(json)
# print the JSON string representation of the object
print VerifyQueryV1.to_json()

# convert the object into a dict
verify_query_v1_dict = verify_query_v1_instance.to_dict()
# create an instance of VerifyQueryV1 from a dict
verify_query_v1_form_dict = verify_query_v1.from_dict(verify_query_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


