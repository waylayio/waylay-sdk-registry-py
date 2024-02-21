# FileUpload

A single asset file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 

## Example

```python
from waylay.services.registry.models.file_upload import FileUpload

# TODO update the JSON string below
json = "{}"
# create an instance of FileUpload from a JSON string
file_upload_instance = FileUpload.from_json(json)
# print the JSON string representation of the object
print FileUpload.to_json()

# convert the object into a dict
file_upload_dict = file_upload_instance.to_dict()
# create an instance of FileUpload from a dict
file_upload_form_dict = file_upload.from_dict(file_upload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


