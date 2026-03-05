# RuntimeVersionInfo

A summary of a selected version for a runtime

**Source:** `waylay.services.registry.models.runtime_version_info`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | If true, the function uses a deprecated runtime. | 
**upgradable** | **bool** | If true, a newer runtime for this function is available using the &#x60;rebuild&#x60; API. | 
**version** | **str** | A semantic version with _exactly_ a &#x60;major&#x60;, &#x60;minor&#x60; and &#x60;patch&#x60; specifier. No &#x60;pre-release&#x60; or &#x60;build&#x60; identifiers are allowed. See https://semver.org | 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**tags** | **List[str]** |  | [optional] 


## Example

```python
from waylay.services.registry.models.runtime_version_info import RuntimeVersionInfo

runtime_version_info = RuntimeVersionInfo(
    deprecated=..., upgradable=..., version=..., title=..., description=..., tags=...
)

# Create from JSON
runtime_version_info = RuntimeVersionInfo.from_json(
    '{ "deprecated": ..., "upgradable": ..., "version": ..., "title": ..., "description": ..., "tags": ... }'
)

# Export to dictionary
runtime_version_info_dict = runtime_version_info.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


