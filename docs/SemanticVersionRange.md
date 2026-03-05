# SemanticVersionRange

A range of semantic versions. See https://devhints.io/semver

**Source:** `waylay.services.registry.models.semantic_version_range`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**str** | -
**str** | A semantic version with _exactly_ a `major`, `minor` and `patch` specifier. No `pre-release` or `build` identifiers are allowed. See https://semver.org

## Example

```python
from waylay.services.registry.models.semantic_version_range import SemanticVersionRange

# Use any of the accepted types (see table above)
my_semantic_version_range: SemanticVersionRange = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


