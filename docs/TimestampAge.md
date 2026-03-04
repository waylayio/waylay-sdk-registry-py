# TimestampAge

A timestamp expressed as a age relative to now

**Source:** `waylay.services.registry.models.timestamp_age`



## Union Type (Any Of)

This type allows any of the following:

Type | Description
------------ | -------------
**str** | An ISO8601 period expression
**str** | An duration expression. A numeric value without unit is interpreted as milliseconds.

## Example

```python
from waylay.services.registry.models.timestamp_age import TimestampAge

# Use any of the accepted types (see table above)
my_timestamp_age: TimestampAge = ...
```


[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


