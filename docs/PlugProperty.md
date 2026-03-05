# PlugProperty

Interface specification of a plug property.

**Source:** `waylay.services.registry.models.plug_property`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of a plug input or output property. | 
**data_type** | [**PlugPropertyDataType**](PlugPropertyDataType.md) |  | [optional] 
**mandatory** | **bool** | If &lt;code&gt;true&lt;/code&gt; this property is required. | [optional] 
**format** | [**PlugPropertyFormat**](PlugPropertyFormat.md) |  | [optional] 
**default_value** | **object** |  | [optional] 


## Example

```python
from waylay.services.registry.models.plug_property import PlugProperty

plug_property = PlugProperty(
    name=..., data_type=..., mandatory=..., format=..., default_value=...
)

# Create from JSON
plug_property = PlugProperty.from_json(
    '{ "name": ..., "dataType": ..., "mandatory": ..., "format": ..., "defaultValue": ... }'
)

# Export to dictionary
plug_property_dict = plug_property.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


