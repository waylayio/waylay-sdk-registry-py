# InvocationAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth** | [**InvocationAttributesAuth**](InvocationAttributesAuth.md) |  | 
**task_context** | **bool** | Indicates whether the task context attributes should be provided in &#x60;options.task&#x60;. | 
**node_context** | **bool** | Indicates whether the node context attributes should be provided in &#x60;options.node&#x60;. | 
**raw_data_context** | **bool** | Indicates that the rawdata context attributes should be provided in &#x60;options.rawData&#x60;. | 
**callback** | **bool** | Indicates that the plug implementer intends to use the callback mechanism. | 

## Example

```python
from waylay.services.registry.models.invocation_attributes import InvocationAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of InvocationAttributes from a JSON string
invocation_attributes_instance = InvocationAttributes.from_json(json)
# print the JSON string representation of the object
print InvocationAttributes.to_json()

# convert the object into a dict
invocation_attributes_dict = invocation_attributes_instance.to_dict()
# create an instance of InvocationAttributes from a dict
invocation_attributes_form_dict = invocation_attributes.from_dict(invocation_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


