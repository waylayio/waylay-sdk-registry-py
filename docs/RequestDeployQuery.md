# RequestDeployQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | **bool** | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.request_deploy_query import RequestDeployQuery

# TODO update the JSON string below
json = "{}"
# create an instance of RequestDeployQuery from a JSON string
request_deploy_query_instance = RequestDeployQuery.from_json(json)
# print the JSON string representation of the object
print RequestDeployQuery.to_json()

# convert the object into a dict
request_deploy_query_dict = request_deploy_query_instance.to_dict()
# create an instance of RequestDeployQuery from a dict
request_deploy_query_form_dict = request_deploy_query.from_dict(request_deploy_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


