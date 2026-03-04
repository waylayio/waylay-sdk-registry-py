# CreatePlugsCopy


**Source:** `waylay.services.registry.models.create_plugs_copy`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**str** | A name reference with optional version range: `<name>[@<versionRange>]`.  References (a version range of) a named and versioned entity like _function_ or _runtime_.
[**ExampleReference**](ExampleReference.md) | -

## Example

```python
from waylay.services.registry.models.create_plugs_copy import CreatePlugsCopy

# Use any of the accepted types (see table above)
my_create_plugs_copy: CreatePlugsCopy = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


