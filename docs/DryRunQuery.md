# DryRunQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | If set to &lt;code&gt;true&lt;/code&gt;, validates the deployment conditions, but does not change anything. | [optional] 

## Example

```python
from waylay.services.registry.models.dry_run_query import DryRunQuery

# TODO update the JSON string below
json = "{}"
# create an instance of DryRunQuery from a JSON string
dry_run_query_instance = DryRunQuery.from_json(json)
# print the JSON string representation of the object
print DryRunQuery.to_json()

# convert the object into a dict
dry_run_query_dict = dry_run_query_instance.to_dict()
# create an instance of DryRunQuery from a dict
dry_run_query_form_dict = dry_run_query.from_dict(dry_run_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


