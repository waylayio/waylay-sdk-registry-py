# AsyncVerifyQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
**scale_to_zero** | **bool** | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 

## Example

```python
from waylay.services.registry.models.async_verify_query import AsyncVerifyQuery

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncVerifyQuery from a JSON string
async_verify_query_instance = AsyncVerifyQuery.from_json(json)
# print the JSON string representation of the object
print AsyncVerifyQuery.to_json()

# convert the object into a dict
async_verify_query_dict = async_verify_query_instance.to_dict()
# create an instance of AsyncVerifyQuery from a dict
async_verify_query_form_dict = async_verify_query.from_dict(async_verify_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


