# InvokeHALLink


**Source:** `waylay.services.registry.models.invoke_hal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoke** | [**IHALLink**](IHALLink.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.invoke_hal_link import InvokeHALLink

invoke_hal_link = InvokeHALLink(invoke=...)

# Create from JSON
invoke_hal_link = InvokeHALLink.from_json('{ "invoke": ... }')

# Export to dictionary
invoke_hal_link_dict = invoke_hal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


