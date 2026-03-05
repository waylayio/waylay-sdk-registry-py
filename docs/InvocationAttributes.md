# InvocationAttributes


**Source:** `waylay.services.registry.models.invocation_attributes`




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

invocation_attributes = InvocationAttributes(
    auth=..., task_context=..., node_context=..., raw_data_context=..., callback=...
)

# Create from JSON
invocation_attributes = InvocationAttributes.from_json(
    '{ "auth": ..., "taskContext": ..., "nodeContext": ..., "rawDataContext": ..., "callback": ... }'
)

# Export to dictionary
invocation_attributes_dict = invocation_attributes.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


