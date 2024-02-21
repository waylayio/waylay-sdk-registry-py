# LegacyPlugCreateQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_async** | **bool** | If this is set to &lt;code&gt;true&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. Otherwise, the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to False]
**dry_run** | **bool** | If set to &lt;code&gt;true&lt;/true&gt;, only validates the incoming request. | [optional] 
**scale_to_zero** | **bool** | If set to &lt;code&gt;true&lt;/true&gt;, scales the function to zero after successful deployment. | [optional] 

## Example

```python
from waylay.services.registry.models.legacy_plug_create_query import LegacyPlugCreateQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LegacyPlugCreateQuery from a JSON string
legacy_plug_create_query_instance = LegacyPlugCreateQuery.from_json(json)
# print the JSON string representation of the object
print LegacyPlugCreateQuery.to_json()

# convert the object into a dict
legacy_plug_create_query_dict = legacy_plug_create_query_instance.to_dict()
# create an instance of LegacyPlugCreateQuery from a dict
legacy_plug_create_query_form_dict = legacy_plug_create_query.from_dict(legacy_plug_create_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


