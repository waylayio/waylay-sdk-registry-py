# ForceDeleteQueryV1


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | If this is set to &lt;code&gt;true&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. Otherwise, the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to False]
**force** | **bool** | If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 

## Example

```python
from waylay.services.registry.models.force_delete_query_v1 import ForceDeleteQueryV1

# TODO update the JSON string below
json = "{}"
# create an instance of ForceDeleteQueryV1 from a JSON string
force_delete_query_v1_instance = ForceDeleteQueryV1.from_json(json)
# print the JSON string representation of the object
print ForceDeleteQueryV1.to_json()

# convert the object into a dict
force_delete_query_v1_dict = force_delete_query_v1_instance.to_dict()
# create an instance of ForceDeleteQueryV1 from a dict
force_delete_query_v1_form_dict = force_delete_query_v1.from_dict(force_delete_query_v1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


