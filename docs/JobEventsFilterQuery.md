# JobEventsFilterQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**JobType**](JobType.md) |  | [optional] 
**id** | **str** | The id of the job. | [optional] 
**children** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, the event stream will include events of the job&#39;s dependants. E.g., when subscribing to a verify job with &#x60;children&#x3D;true&#x60;, you will also receive the events of the underlying build and deploy jobs. Defaults to &lt;code&gt;false&lt;/code&gt;. | [optional] 

## Example

```python
from waylay.services.registry.models.job_events_filter_query import JobEventsFilterQuery

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventsFilterQuery from a JSON string
job_events_filter_query_instance = JobEventsFilterQuery.from_json(json)
# print the JSON string representation of the object
print JobEventsFilterQuery.to_json()

# convert the object into a dict
job_events_filter_query_dict = job_events_filter_query_instance.to_dict()
# create an instance of JobEventsFilterQuery from a dict
job_events_filter_query_form_dict = job_events_filter_query.from_dict(job_events_filter_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


