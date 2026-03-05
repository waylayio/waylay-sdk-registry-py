# JobsForPlugResponseV2

Plug Jobs Found

**Source:** `waylay.services.registry.models.jobs_for_plug_response_v2`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**jobs** | [**List[AnyJobForFunction]**](AnyJobForFunction.md) | Listing of jobs related to the function deployment. This includes active jobs, and the most recently failed job (per type) that was archived on the entity. | 
**function** | [**FunctionRef**](FunctionRef.md) |  | 
**links** | [**JobsForPlugResponseV2Links**](JobsForPlugResponseV2Links.md) |  | [optional] 


## Example

```python
from waylay.services.registry.models.jobs_for_plug_response_v2 import (
    JobsForPlugResponseV2,
)

jobs_for_plug_response_v2 = JobsForPlugResponseV2(jobs=..., function=..., links=...)

# Create from JSON
jobs_for_plug_response_v2 = JobsForPlugResponseV2.from_json(
    '{ "jobs": ..., "function": ..., "_links": ... }'
)

# Export to dictionary
jobs_for_plug_response_v2_dict = jobs_for_plug_response_v2.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


