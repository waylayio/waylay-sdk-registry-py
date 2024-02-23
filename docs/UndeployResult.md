# UndeployResult

The result data for a completed undeployment job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | **bool** |  | 
**assets** | **bool** |  | 
**registration** | **bool** |  | 

## Example

```python
from waylay.services.registry.models.undeploy_result import UndeployResult

# TODO update the JSON string below
json = "{}"
# create an instance of UndeployResult from a JSON string
undeploy_result_instance = UndeployResult.from_json(json)
# print the JSON string representation of the object
print UndeployResult.to_json()

# convert the object into a dict
undeploy_result_dict = undeploy_result_instance.to_dict()
# create an instance of UndeployResult from a dict
undeploy_result_form_dict = undeploy_result.from_dict(undeploy_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


