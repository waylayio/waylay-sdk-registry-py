# MultipartFileUpload

A multi-part upload containing one or more file assets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filename** | **List[bytearray]** |  | [optional] 

## Example

```python
from waylay.services.registry.models.multipart_file_upload import MultipartFileUpload

# TODO update the JSON string below
json = "{}"
# create an instance of MultipartFileUpload from a JSON string
multipart_file_upload_instance = MultipartFileUpload.from_json(json)
# print the JSON string representation of the object
print MultipartFileUpload.to_json()

# convert the object into a dict
multipart_file_upload_dict = multipart_file_upload_instance.to_dict()
# create an instance of MultipartFileUpload from a dict
multipart_file_upload_form_dict = multipart_file_upload.from_dict(multipart_file_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


