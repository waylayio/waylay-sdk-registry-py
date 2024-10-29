# RuntimeSummaryResponse

Runtimes Found

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**embedded** | [**RuntimeSummaryResponseEmbedded**](RuntimeSummaryResponseEmbedded.md) |  | [optional] 
**runtimes** | [**List[RuntimeSummary]**](RuntimeSummary.md) |  | 

## Example

```python
from waylay.services.registry.models.runtime_summary_response import RuntimeSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeSummaryResponse from a JSON string
runtime_summary_response_instance = RuntimeSummaryResponse.from_json(json)
# print the JSON string representation of the object
print RuntimeSummaryResponse.to_json()

# convert the object into a dict
runtime_summary_response_dict = runtime_summary_response_instance.to_dict()
# create an instance of RuntimeSummaryResponse from a dict
runtime_summary_response_form_dict = runtime_summary_response.from_dict(runtime_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


