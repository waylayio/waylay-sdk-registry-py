# RegistryErrorResponse


**Source:** `waylay.services.registry.models.registry_error_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **str** |  | 
**status_code** | **float** |  | 
**data** | **Dict[str, str]** |  | [optional] 


## Example

```python
from waylay.services.registry.models.registry_error_response import (
    RegistryErrorResponse,
)

registry_error_response = RegistryErrorResponse(
    error=..., code=..., status_code=..., data=...
)

# Create from JSON
registry_error_response = RegistryErrorResponse.from_json(
    '{ "error": ..., "code": ..., "statusCode": ..., "data": ... }'
)

# Export to dictionary
registry_error_response_dict = registry_error_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


