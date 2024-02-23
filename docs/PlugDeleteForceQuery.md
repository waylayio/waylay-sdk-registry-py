# PlugDeleteForceQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 

## Example

```python
from waylay.services.registry.models.plug_delete_force_query import PlugDeleteForceQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PlugDeleteForceQuery from a JSON string
plug_delete_force_query_instance = PlugDeleteForceQuery.from_json(json)
# print the JSON string representation of the object
print PlugDeleteForceQuery.to_json()

# convert the object into a dict
plug_delete_force_query_dict = plug_delete_force_query_instance.to_dict()
# create an instance of PlugDeleteForceQuery from a dict
plug_delete_force_query_form_dict = plug_delete_force_query.from_dict(plug_delete_force_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


