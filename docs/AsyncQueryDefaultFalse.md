# AsyncQueryDefaultFalse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | If this is set to &lt;code&gt;true&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. Otherwise, the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to False]

## Example

```python
from waylay.services.registry.models.async_query_default_false import AsyncQueryDefaultFalse

# TODO update the JSON string below
json = "{}"
# create an instance of AsyncQueryDefaultFalse from a JSON string
async_query_default_false_instance = AsyncQueryDefaultFalse.from_json(json)
# print the JSON string representation of the object
print AsyncQueryDefaultFalse.to_json()

# convert the object into a dict
async_query_default_false_dict = async_query_default_false_instance.to_dict()
# create an instance of AsyncQueryDefaultFalse from a dict
async_query_default_false_form_dict = async_query_default_false.from_dict(async_query_default_false_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


