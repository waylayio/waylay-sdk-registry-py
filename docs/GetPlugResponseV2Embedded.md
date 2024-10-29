# GetPlugResponseV2Embedded

Embedded representations of the referenced tags.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | [**List[Tag]**](Tag.md) | Record of &lt;tag key, tag representation&gt; pairs. | [optional] 

## Example

```python
from waylay.services.registry.models.get_plug_response_v2_embedded import GetPlugResponseV2Embedded

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlugResponseV2Embedded from a JSON string
get_plug_response_v2_embedded_instance = GetPlugResponseV2Embedded.from_json(json)
# print the JSON string representation of the object
print GetPlugResponseV2Embedded.to_json()

# convert the object into a dict
get_plug_response_v2_embedded_dict = get_plug_response_v2_embedded_instance.to_dict()
# create an instance of GetPlugResponseV2Embedded from a dict
get_plug_response_v2_embedded_form_dict = get_plug_response_v2_embedded.from_dict(get_plug_response_v2_embedded_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


