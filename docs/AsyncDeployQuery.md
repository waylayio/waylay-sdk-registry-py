# AsyncDeployQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecate_previous** | [**DeprecatePreviousPolicy**](DeprecatePreviousPolicy.md) |  | [optional] 
**dry_run** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
**scale_to_zero** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. Saves computing resources when the function is not to be used immediately. | [optional] [default to False]

## Example

```python
from waylay.services.registry.models.async_deploy_query import AsyncDeployQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncDeployQuery from a JSON string
async_deploy_query_instance = AsyncDeployQuery.from_json(json)
# print the JSON string representation of the object
print AsyncDeployQuery.to_json()

# convert the object into a dict
async_deploy_query_dict = async_deploy_query_instance.to_dict()
# create an instance of AsyncDeployQuery from a dict
async_deploy_query_form_dict = async_deploy_query.from_dict(async_deploy_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


