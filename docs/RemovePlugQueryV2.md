# RemovePlugQueryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
**force** | **bool** | If &lt;code&gt;true&lt;/code&gt;, the plug version(s) will be undeployed and removed. Otherwise, the plug version(s) will only be &lt;code&gt;deprecated&lt;/code&gt;, i.e removed from regular listings. | [optional] 
**undeploy** | **bool** | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function for the plug: it becomes no longer available for invocation. * does NOT remove the plug from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the plug can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug version(s) as _deprecated_: the plug remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 

## Example

```python
from waylay.services.registry.models.remove_plug_query_v2 import RemovePlugQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of RemovePlugQueryV2 from a JSON string
remove_plug_query_v2_instance = RemovePlugQueryV2.from_json(json)
# print the JSON string representation of the object
print RemovePlugQueryV2.to_json()

# convert the object into a dict
remove_plug_query_v2_dict = remove_plug_query_v2_instance.to_dict()
# create an instance of RemovePlugQueryV2 from a dict
remove_plug_query_v2_form_dict = remove_plug_query_v2.from_dict(remove_plug_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


