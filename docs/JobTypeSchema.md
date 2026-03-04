# JobTypeSchema


**Source:** `waylay.services.registry.models.job_type_schema`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
[**JobTypeBuild**](JobTypeBuild.md) | -
[**JobTypeDeploy**](JobTypeDeploy.md) | -
[**JobTypeVerify**](JobTypeVerify.md) | -
[**JobTypeUndeploy**](JobTypeUndeploy.md) | -
[**JobTypeScale**](JobTypeScale.md) | -
[**JobTypeBatch**](JobTypeBatch.md) | -
[**JobTypeNotify**](JobTypeNotify.md) | -

## Example

```python
from waylay.services.registry.models.job_type_schema import JobTypeSchema

# Use any of the accepted types (see table above)
my_job_type_schema: JobTypeSchema = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


