# RequestOperation

A modifying operation on the function.

**Source:** `waylay.services.registry.models.request_operation`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**CREATE** | `'create'` |
**METADATA_MINUS_UPDATE** | `'metadata-update'` |
**ASSETS_MINUS_UPDATE** | `'assets-update'` |
**REBUILD** | `'rebuild'` |
**VERIFY** | `'verify'` |
**PUBLISH** | `'publish'` |
**DEPRECATE** | `'deprecate'` |
**UNDEPLOY** | `'undeploy'` |
**UNDEPRECATE** | `'undeprecate'` |
**PROTECT** | `'protect'` |
**UNPROTECT** | `'unprotect'` |

## Example

```python
from waylay.services.registry.models.request_operation import RequestOperation

# Use enum by value
my_request_operation = RequestOperation.CREATE
print(my_request_operation)  # Output: 'create'

# Or by string value
my_request_operation = RequestOperation("create")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


