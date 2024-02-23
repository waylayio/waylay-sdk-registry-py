# LimitQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | The maximum number of items to be return from this query. Has a deployment-defined default and maximum value. | [optional] 

## Example

```python
from waylay.services.registry.models.limit_query import LimitQuery

# TODO update the JSON string below
json = "{}"
# create an instance of LimitQuery from a JSON string
limit_query_instance = LimitQuery.from_json(json)
# print the JSON string representation of the object
print LimitQuery.to_json()

# convert the object into a dict
limit_query_dict = limit_query_instance.to_dict()
# create an instance of LimitQuery from a dict
limit_query_form_dict = limit_query.from_dict(limit_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


