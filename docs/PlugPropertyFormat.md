# PlugPropertyFormat


**Source:** `waylay.services.registry.models.plug_property_format`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**PlugPropertyFormatType**](PlugPropertyFormatType.md) |  | 
**values** | **List[object]** | The enumerated value domain when &lt;code&gt;type&#x3D;\&quot;enum\&quot;&lt;/code&gt; | [optional] 


## Example

```python
from waylay.services.registry.models.plug_property_format import PlugPropertyFormat

plug_property_format = PlugPropertyFormat(type=..., values=...)

# Create from JSON
plug_property_format = PlugPropertyFormat.from_json('{ "type": ..., "values": ... }')

# Export to dictionary
plug_property_format_dict = plug_property_format.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


