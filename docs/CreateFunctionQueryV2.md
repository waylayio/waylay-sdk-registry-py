# CreateFunctionQueryV2


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deploy** | **bool** | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default to True]
**author** | **str** | Optionally changes the author metadata when updating a function. | [optional] 
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**scale_to_zero** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default to False]
**deprecate_previous** | [**DeprecatePreviousPolicy**](DeprecatePreviousPolicy.md) |  | [optional] 
**dry_run** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]
**version** | [**SemanticVersionRange**](SemanticVersionRange.md) |  | [optional] 
**name** | **str** | If set, the value will be used as the function name instead of the one specified in the manifest. | [optional] 
**draft** | **bool** | If set, the created function will be a draft function and its assets are still mutable. A build and deploy is initiated only in the case when all necessary assets are present and valid. | [optional] [default to False]
**runtime** | **str** | A name reference with optional version range: &#x60;&lt;name&gt;[@&lt;versionRange&gt;]&#x60;.  References (a version range of) a named and versioned entity like _function_ or _runtime_. | [optional] 
**copy_from** | [**CreateFunctionQueryV2Copy**](CreateFunctionQueryV2Copy.md) |  | [optional] 

## Example

```python
from waylay.services.registry.models.create_function_query_v2 import CreateFunctionQueryV2

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFunctionQueryV2 from a JSON string
create_function_query_v2_instance = CreateFunctionQueryV2.from_json(json)
# print the JSON string representation of the object
print CreateFunctionQueryV2.to_json()

# convert the object into a dict
create_function_query_v2_dict = create_function_query_v2_instance.to_dict()
# create an instance of CreateFunctionQueryV2 from a dict
create_function_query_v2_form_dict = create_function_query_v2.from_dict(create_function_query_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


