# AsyncDeployQueryV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
**dry_run** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
**scale_to_zero** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default to False]

## Example

```python
from waylay.services.registry.models.async_deploy_query_v1 import AsyncDeployQueryV1

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncDeployQueryV1 from a JSON string
async_deploy_query_v1_instance = AsyncDeployQueryV1.from_json(json)
# print the JSON string representation of the object
print AsyncDeployQueryV1.to_json()

# convert the object into a dict
async_deploy_query_v1_dict = async_deploy_query_v1_instance.to_dict()
# create an instance of AsyncDeployQueryV1 from a dict
async_deploy_query_v1_form_dict = async_deploy_query_v1.from_dict(async_deploy_query_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


