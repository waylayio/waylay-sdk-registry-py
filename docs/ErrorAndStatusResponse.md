# ErrorAndStatusResponse


**Source:** `waylay.services.registry.models.error_and_status_response`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**status_code** | **float** |  | 


## Example

```python
from waylay.services.registry.models.error_and_status_response import (
    ErrorAndStatusResponse,
)

error_and_status_response = ErrorAndStatusResponse(error=..., status_code=...)

# Create from JSON
error_and_status_response = ErrorAndStatusResponse.from_json(
    '{ "error": ..., "statusCode": ... }'
)

# Export to dictionary
error_and_status_response_dict = error_and_status_response.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


