# BatchArgs


**Source:** `waylay.services.registry.models.batch_args`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plug_name** | **str** |  | 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**child_type** | **str** |  | [optional] 


## Example

```python
from waylay.services.registry.models.batch_args import BatchArgs

batch_args = BatchArgs(plug_name=..., function_type=..., child_type=...)

# Create from JSON
batch_args = BatchArgs.from_json(
    '{ "plugName": ..., "functionType": ..., "childType": ... }'
)

# Export to dictionary
batch_args_dict = batch_args.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


