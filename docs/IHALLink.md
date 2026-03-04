# IHALLink


**Source:** `waylay.services.registry.models.ihal_link`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**href** | [**IHALLinkHref**](IHALLinkHref.md) |  | 


## Example

```python
from waylay.services.registry.models.ihal_link import IHALLink

ihal_link = IHALLink(href=...)

# Create from JSON
ihal_link = IHALLink.from_json('{ "href": ... }')

# Export to dictionary
ihal_link_dict = ihal_link.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


