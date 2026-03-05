# FileUpload

A single asset file.

**Source:** `waylay.services.registry.models.file_upload`




## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** |  | [optional] 


## Example

```python
from waylay.services.registry.models.file_upload import FileUpload

file_upload = FileUpload(file=...)

# Create from JSON
file_upload = FileUpload.from_json('{ "file": ... }')

# Export to dictionary
file_upload_dict = file_upload.to_dict()
```



[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


