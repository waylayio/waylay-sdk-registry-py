# InvocationAttributesAuth

Indicates what credentials are passed to provide a Waylay authorization context.

**Source:** `waylay.services.registry.models.invocation_attributes_auth`

## Enum Values

Name | Value | Description
------------ | ------------- | -------------
**WAYLAY** | `'waylay'` |
**NONE** | `'none'` |

## Example

```python
from waylay.services.registry.models.invocation_attributes_auth import (
    InvocationAttributesAuth,
)

# Use enum by value
my_invocation_attributes_auth = InvocationAttributesAuth.WAYLAY
print(my_invocation_attributes_auth)  # Output: 'waylay'

# Or by string value
my_invocation_attributes_auth = InvocationAttributesAuth("waylay")
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


