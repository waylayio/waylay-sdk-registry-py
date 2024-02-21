# ContentValidationListing

Content listing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[AssetSummaryWithHALLink]**](AssetSummaryWithHALLink.md) |  | 

## Example

```python
from waylay.services.registry.models.content_validation_listing import ContentValidationListing

# TODO update the JSON string below
json = "{}"
# create an instance of ContentValidationListing from a JSON string
content_validation_listing_instance = ContentValidationListing.from_json(json)
# print the JSON string representation of the object
print ContentValidationListing.to_json()

# convert the object into a dict
content_validation_listing_dict = content_validation_listing_instance.to_dict()
# create an instance of ContentValidationListing from a dict
content_validation_listing_form_dict = content_validation_listing.from_dict(content_validation_listing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


