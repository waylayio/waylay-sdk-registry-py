# JobsForModelResponseV2Links

Link to the function entity.

**Source:** `waylay.services.registry.models.jobs_for_model_response_v2_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | [**HALLinks**](HALLinks.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.jobs_for_model_response_v2_links import (
    JobsForModelResponseV2Links,
)

jobs_for_model_response_v2_links = JobsForModelResponseV2Links(model=...)

# Create from JSON
jobs_for_model_response_v2_links = JobsForModelResponseV2Links.from_json(
    '{ "model": ... }'
)

# Export to dictionary
jobs_for_model_response_v2_links_dict = jobs_for_model_response_v2_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


