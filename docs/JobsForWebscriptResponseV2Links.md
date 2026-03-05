# JobsForWebscriptResponseV2Links

Link to the function entity.

**Source:** `waylay.services.registry.models.jobs_for_webscript_response_v2_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webscript** | [**HALLinks**](HALLinks.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.jobs_for_webscript_response_v2_links import (
    JobsForWebscriptResponseV2Links,
)

jobs_for_webscript_response_v2_links = JobsForWebscriptResponseV2Links(webscript=...)

# Create from JSON
jobs_for_webscript_response_v2_links = JobsForWebscriptResponseV2Links.from_json(
    '{ "webscript": ... }'
)

# Export to dictionary
jobs_for_webscript_response_v2_links_dict = (
    jobs_for_webscript_response_v2_links.to_dict()
)
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


