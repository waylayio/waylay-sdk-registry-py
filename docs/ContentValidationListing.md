# ContentValidationListing

Content listing

**Source:** `waylay.services.registry.models.content_validation_listing`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetSummaryWithHALLink]**](AssetSummaryWithHALLink.md) |  | 


## Example

```python
from waylay.services.registry.models.content_validation_listing import (
    ContentValidationListing,
)

content_validation_listing = ContentValidationListing(assets=...)

# Create from JSON
content_validation_listing = ContentValidationListing.from_json('{ "assets": ... }')

# Export to dictionary
content_validation_listing_dict = content_validation_listing.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


