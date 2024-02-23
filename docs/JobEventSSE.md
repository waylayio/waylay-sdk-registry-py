# JobEventSSE


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** | The job queue event that trigged this message | 
**data** | [**JobEventResponseWaitingChildrenEventData**](JobEventResponseWaitingChildrenEventData.md) |  | 

## Example

```python
from waylay.services.registry.models.job_event_sse import JobEventSSE

# TODO update the JSON string below
json = "{}"
# create an instance of JobEventSSE from a JSON string
job_event_sse_instance = JobEventSSE.from_json(json)
# print the JSON string representation of the object
print JobEventSSE.to_json()

# convert the object into a dict
job_event_sse_dict = job_event_sse_instance.to_dict()
# create an instance of JobEventSSE from a dict
job_event_sse_form_dict = job_event_sse.from_dict(job_event_sse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


