# RuntimeVersionStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deprecated** | **bool** | If true, the function uses a deprecated runtime. | 
**upgradable** | **bool** | If true, a newer runtime for this function is available using the &#x60;rebuild&#x60; API. | 

## Example

```python
from waylay.services.registry.models.runtime_version_status import RuntimeVersionStatus

# TODO update the JSON string below
json = "{}"
# create an instance of RuntimeVersionStatus from a JSON string
runtime_version_status_instance = RuntimeVersionStatus.from_json(json)
# print the JSON string representation of the object
print RuntimeVersionStatus.to_json()

# convert the object into a dict
runtime_version_status_dict = runtime_version_status_instance.to_dict()
# create an instance of RuntimeVersionStatus from a dict
runtime_version_status_form_dict = runtime_version_status.from_dict(runtime_version_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


