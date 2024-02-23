# KFServingDeleteQueryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**force** | **bool** | If &lt;code&gt;true&lt;/code&gt;, the function version will be immediately undeployed and removed.  Otherwise, the removal will be delayed to allow current invocations to end. During that period, the function is marked _deprecated_. | [optional] 
**undeploy** | **bool** | If &#x60;true&#x60;, the &#x60;DELETE&#x60; operation * undeploys the (openfaas) function: it becomes no longer available for invocation. * does NOT remove the function from registry: it stays in an &#x60;undeployed&#x60; status.  All assets and definitions are retained, so the version can be restored later with a  _rebuild_ action.  If &#x60;false&#x60;, the &#x60;DELETE&#x60; operation * _only_ marks the plug function as _deprecated_, the function remains active but is removed from the default listings.   This also applies to _draft_ versions.  This parameter is incompatible with &#x60;force&#x3D;true&#x60;.  If not set the default behaviour applies: * _draft_ versions are _undeployed_ and _removed_ from registry. * non-_draft_ versions are marked _deprecated_ only. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.kf_serving_delete_query_v2 import KFServingDeleteQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of KFServingDeleteQueryV2 from a JSON string
kf_serving_delete_query_v2_instance = KFServingDeleteQueryV2.from_json(json)
# print the JSON string representation of the object
print KFServingDeleteQueryV2.to_json()

# convert the object into a dict
kf_serving_delete_query_v2_dict = kf_serving_delete_query_v2_instance.to_dict()
# create an instance of KFServingDeleteQueryV2 from a dict
kf_serving_delete_query_v2_form_dict = kf_serving_delete_query_v2.from_dict(kf_serving_delete_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


