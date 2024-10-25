# RuntimeSummaryResponseEmbedded

Embedded representations of the referenced tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[RuntimeTag]**](RuntimeTag.md) | Record of &lt;tag key, tag representation&gt; pairs. | [optional] 

## Example

```python
from waylay.services.registry.models.runtime_summary_response_embedded import RuntimeSummaryResponseEmbedded

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeSummaryResponseEmbedded from a JSON string
runtime_summary_response_embedded_instance = RuntimeSummaryResponseEmbedded.from_json(json)
# print the JSON string representation of the object
print RuntimeSummaryResponseEmbedded.to_json()

# convert the object into a dict
runtime_summary_response_embedded_dict = runtime_summary_response_embedded_instance.to_dict()
# create an instance of RuntimeSummaryResponseEmbedded from a dict
runtime_summary_response_embedded_form_dict = runtime_summary_response_embedded.from_dict(runtime_summary_response_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


