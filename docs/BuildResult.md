# BuildResult


**Source:** `waylay.services.registry.models.build_result`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **str** | SHA digest of the built image. | 
**log** | **List[str]** | Detailed logs of the build steps. | [optional] 
**status** | **str** | Outcome of the build. | [optional] 


## Example

```python
from waylay.services.registry.models.build_result import BuildResult

build_result = BuildResult(digest=..., log=..., status=...)

# Create from JSON
build_result = BuildResult.from_json('{ "digest": ..., "log": ..., "status": ... }')

# Export to dictionary
build_result_dict = build_result.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


