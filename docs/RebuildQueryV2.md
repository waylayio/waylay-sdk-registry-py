# RebuildQueryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_to_zero** | **bool** | Indicates whether the function needs to be scaled down after successful verification. If not set, the function is scaled to zero only if it was not active before this command. | [optional] 
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**dry_run** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, checks whether rebuild jobs are needed, but do not start any jobs. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
**upgrade** | [**RebuildPolicy**](RebuildPolicy.md) |  | [optional] 
**force_version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | [optional] 
**ignore_checks** | **bool** | If set to true, checks that normally prevent a rebuild are overriden. These checks include: * function state in &#x60;pending&#x60;, &#x60;running&#x60;, &#x60;failed&#x60; or &#x60;undeployed&#x60; * backoff period due to recent failures * usage of deprecated dependencies * running jobs on entity * the &#x60;dryRun&#x60; option | [optional] 
**skip_rebuild** | **bool** | If set, the function will not be rebuild. Always uses the current runtime version when re-deploying/re-verifying the function. | [optional] 

## Example

```python
from waylay.services.registry.models.rebuild_query_v2 import RebuildQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of RebuildQueryV2 from a JSON string
rebuild_query_v2_instance = RebuildQueryV2.from_json(json)
# print the JSON string representation of the object
print RebuildQueryV2.to_json()

# convert the object into a dict
rebuild_query_v2_dict = rebuild_query_v2_instance.to_dict()
# create an instance of RebuildQueryV2 from a dict
rebuild_query_v2_form_dict = rebuild_query_v2.from_dict(rebuild_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


