# JobsForPlugResponseV2Links

Link to the function entity.

**Source:** `waylay.services.registry.models.jobs_for_plug_response_v2_links`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plug** | [**HALLinks**](HALLinks.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.jobs_for_plug_response_v2_links import (
    JobsForPlugResponseV2Links,
)

jobs_for_plug_response_v2_links = JobsForPlugResponseV2Links(plug=...)

# Create from JSON
jobs_for_plug_response_v2_links = JobsForPlugResponseV2Links.from_json(
    '{ "plug": ... }'
)

# Export to dictionary
jobs_for_plug_response_v2_links_dict = jobs_for_plug_response_v2_links.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


