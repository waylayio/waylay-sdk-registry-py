# PlugDeleteQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**force** | **bool** | If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 
**undeploy** | **bool** | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 

## Example

```python
from waylay.services.registry.models.plug_delete_query import PlugDeleteQuery

# TODO update the JSON string below
json = "{}"
# create an instance of PlugDeleteQuery from a JSON string
plug_delete_query_instance = PlugDeleteQuery.from_json(json)
# print the JSON string representation of the object
print PlugDeleteQuery.to_json()

# convert the object into a dict
plug_delete_query_dict = plug_delete_query_instance.to_dict()
# create an instance of PlugDeleteQuery from a dict
plug_delete_query_form_dict = plug_delete_query.from_dict(plug_delete_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


