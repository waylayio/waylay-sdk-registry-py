# BatchArgs


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plug_name** | **str** |  | 
**function_type** | [**FunctionType**](FunctionType.md) |  | 
**child_type** | **str** |  | [optional] 

## Example

```python
from waylay.services.registry.models.batch_args import BatchArgs

# TODO update the JSON string below
json = "{}"
# create an instance of BatchArgs from a JSON string
batch_args_instance = BatchArgs.from_json(json)
# print the JSON string representation of the object
print BatchArgs.to_json()

# convert the object into a dict
batch_args_dict = batch_args_instance.to_dict()
# create an instance of BatchArgs from a dict
batch_args_form_dict = batch_args.from_dict(batch_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


