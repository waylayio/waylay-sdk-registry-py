# PublishFunctionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chown** | **bool** | If set, ownership of the draft function is transferred to the current user. | [optional] [default to False]
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**author** | **str** | Optionally changes the author metadata when updating a function. | [optional] 
**deprecate_previous** | [**DeprecatePreviousPolicy**](DeprecatePreviousPolicy.md) |  | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.publish_function_query import PublishFunctionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PublishFunctionQuery from a JSON string
publish_function_query_instance = PublishFunctionQuery.from_json(json)
# print the JSON string representation of the object
print PublishFunctionQuery.to_json()

# convert the object into a dict
publish_function_query_dict = publish_function_query_instance.to_dict()
# create an instance of PublishFunctionQuery from a dict
publish_function_query_form_dict = publish_function_query.from_dict(publish_function_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


