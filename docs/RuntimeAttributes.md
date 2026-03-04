# RuntimeAttributes


**Source:** `waylay.services.registry.models.runtime_attributes`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | If true, the function uses a deprecated runtime. | 
**upgradable** | **bool** | If true, a newer runtime for this function is available using the &#x60;rebuild&#x60; API. | 
**name** | **str** |  | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 


## Example

```python
from waylay.services.registry.models.runtime_attributes import RuntimeAttributes

runtime_attributes = RuntimeAttributes(
    deprecated=..., upgradable=..., name=..., version=...
)

# Create from JSON
runtime_attributes = RuntimeAttributes.from_json(
    '{ "deprecated": ..., "upgradable": ..., "name": ..., "version": ... }'
)

# Export to dictionary
runtime_attributes_dict = runtime_attributes.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


