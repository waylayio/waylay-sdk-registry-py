# AsyncQueryDefaultTrue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.async_query_default_true import AsyncQueryDefaultTrue

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncQueryDefaultTrue from a JSON string
async_query_default_true_instance = AsyncQueryDefaultTrue.from_json(json)
# print the JSON string representation of the object
print AsyncQueryDefaultTrue.to_json()

# convert the object into a dict
async_query_default_true_dict = async_query_default_true_instance.to_dict()
# create an instance of AsyncQueryDefaultTrue from a dict
async_query_default_true_form_dict = async_query_default_true.from_dict(async_query_default_true_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


