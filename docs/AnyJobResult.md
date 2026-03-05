# AnyJobResult


**Source:** `waylay.services.registry.models.any_job_result`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**BuildResult**](BuildResult.md) | -
[**DeployResult**](DeployResult.md) | -
[**VerifyResult**](VerifyResult.md) | -
[**UndeployResult**](UndeployResult.md) | -
**object** | The result data for a completed scale job.
[**BatchResult**](BatchResult.md) | -
[**CleanupResult**](CleanupResult.md) | -
[**NotifyResult**](NotifyResult.md) | -

## Example

```python
from waylay.services.registry.models.any_job_result import AnyJobResult

# Use any of the accepted types (see table above)
my_any_job_result: AnyJobResult = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


