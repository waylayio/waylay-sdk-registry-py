# UpdateDraftQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scale_to_zero** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, after successful deployment, the deployed function will be scaled to zero. This saves computing resources when the function is not to be used immediately. | [optional] [default to False]
**deploy** | **bool** | Indicates that a function should be _deployed_ when its assets are valid.  * If &#x60;true&#x60; (default), jobs to build and deploy the function will be initiated after it is checked that the assets are valid. Invalid assets lead to a validation error, and the function and its assets are not created or updated. * If &#x60;false&#x60;, the uploaded assets are stored and the function is created/updated in &#x60;registered&#x60; state. Asset validation errors are only returned as warning, and stored as &#x60;failureReason&#x60; on the function entity. Use an _asset update_ or _rebuild_ to initiate a build and deploy at a later stage. | [optional] [default to True]
**chown** | **bool** | If set, ownership of the draft function is transferred to the current user. | [optional] [default to False]
**comment** | **str** | An optional user-specified comment corresponding to the operation. | [optional] 
**author** | **str** | Optionally changes the author metadata when updating a function. | [optional] 
**var_async** | **bool** | Unless this is set to &lt;code&gt;false&lt;/code&gt;, the server will start the required job actions asynchronously and return a &lt;code&gt;202&lt;/code&gt; &lt;em&gt;Accepted&lt;/em&gt; response. If &lt;code&gt;false&lt;/code&gt; the request will block until the job actions are completed, or a timeout occurs. | [optional] [default to True]

## Example

```python
from waylay.services.registry.models.update_draft_query import UpdateDraftQuery

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDraftQuery from a JSON string
update_draft_query_instance = UpdateDraftQuery.from_json(json)
# print the JSON string representation of the object
print UpdateDraftQuery.to_json()

# convert the object into a dict
update_draft_query_dict = update_draft_query_instance.to_dict()
# create an instance of UpdateDraftQuery from a dict
update_draft_query_form_dict = update_draft_query.from_dict(update_draft_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


